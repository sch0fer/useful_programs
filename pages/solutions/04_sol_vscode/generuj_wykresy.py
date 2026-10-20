# -*- coding: utf-8 -*-
"""Generate the figures accompanying raport.md.

Run from this directory with: python generuj_wykresy.py
Dependencies: numpy and matplotlib.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


OUT = Path(__file__).resolve().parent / "files" / "rzut_ukosny"
OUT.mkdir(parents=True, exist_ok=True)

V0 = 36.0
ALPHA_DEG = 2.0
ALPHA = np.deg2rad(ALPHA_DEG)
G = 9.81
MASS = 0.145
DIAMETER = 0.073
RHO = 1.225
CD = 0.47
AREA = np.pi * (DIAMETER / 2.0) ** 2
DRAG_FACTOR = RHO * CD * AREA / (2.0 * MASS)
DT = 2.0e-4

BLUE, ORANGE, GREEN, PURPLE, INK = (
    "#2463A6",
    "#D47722",
    "#168578",
    "#8455A4",
    "#233044",
)
plt.rcParams.update(
    {
        "font.family": "DejaVu Sans",
        "font.size": 10,
        "axes.titlesize": 12,
        "axes.titleweight": "bold",
        "axes.labelcolor": INK,
        "text.color": INK,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.grid": True,
        "grid.alpha": 0.2,
        "lines.linewidth": 2.2,
        "figure.facecolor": "white",
        "savefig.facecolor": "white",
    }
)


def derivative(state):
    x, y, vx, vy = state
    speed = np.hypot(vx, vy)
    return np.array(
        [
            vx,
            vy,
            -DRAG_FACTOR * speed * vx,
            -G - DRAG_FACTOR * speed * vy,
        ]
    )


def simulate_with_drag():
    """Integrate motion with RK4 and interpolate the ground impact."""
    state = np.array(
        [0.0, 0.0, V0 * np.cos(ALPHA), V0 * np.sin(ALPHA)]
    )
    times = [0.0]
    states = [state.copy()]

    for _ in range(10000):
        previous = state.copy()
        k1 = derivative(state)
        k2 = derivative(state + 0.5 * DT * k1)
        k3 = derivative(state + 0.5 * DT * k2)
        k4 = derivative(state + DT * k3)
        state = state + (DT / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)
        time = times[-1] + DT

        if state[1] < 0.0:
            fraction = previous[1] / (previous[1] - state[1])
            state = previous + fraction * (state - previous)
            time = times[-1] + fraction * DT
            state[1] = 0.0
            times.append(time)
            states.append(state.copy())
            break

        times.append(time)
        states.append(state.copy())
    else:
        raise RuntimeError("Ground impact was not reached within the time limit.")

    return np.asarray(times), np.asarray(states)


def save(fig, filename):
    fig.savefig(OUT / filename, dpi=180, bbox_inches="tight")
    plt.close(fig)


def main():
    vx0 = V0 * np.cos(ALPHA)
    vy0 = V0 * np.sin(ALPHA)
    flight_time_ideal = 2.0 * vy0 / G
    time_ideal = np.linspace(0.0, flight_time_ideal, 500)
    x_ideal = vx0 * time_ideal
    y_ideal = vy0 * time_ideal - 0.5 * G * time_ideal**2
    vx_ideal = np.full_like(time_ideal, vx0)
    vy_ideal = vy0 - G * time_ideal

    time_drag, state_drag = simulate_with_drag()
    x_drag, y_drag, vx_drag, vy_drag = state_drag.T
    speed_drag = np.hypot(vx_drag, vy_drag)
    ax_drag = -DRAG_FACTOR * speed_drag * vx_drag
    ay_drag = -G - DRAG_FACTOR * speed_drag * vy_drag
    kinetic_drag = 0.5 * MASS * speed_drag**2
    potential_drag = MASS * G * y_drag
    energy_drag = kinetic_drag + potential_drag

    fig, ax = plt.subplots(figsize=(9, 4.7), layout="constrained")
    ax.plot(x_ideal, y_ideal, color=BLUE, label="Bez oporu")
    ax.plot(x_drag, y_drag, color=ORANGE, label="Opór kwadratowy")
    ax.scatter([0.0], [0.0], color=GREEN, zorder=3, label="Start")
    ax.scatter([x_ideal[-1], x_drag[-1]], [0.0, 0.0],
               color=[BLUE, ORANGE], zorder=3, s=35)
    ax.set(
        xlabel="Położenie poziome x [m]",
        ylabel="Wysokość y [m]",
        title="Tor ruchu: model idealny i z oporem powietrza",
    )
    ax.legend()
    ax.text(
        0.02,
        0.97,
        "Skala pionowa jest powiększona dla czytelności.",
        transform=ax.transAxes,
        va="top",
        fontsize=9,
        color=INK,
    )
    save(fig, "tor_ruchu.png")

    fig, axes = plt.subplots(1, 2, figsize=(10, 4.2), layout="constrained")
    axes[0].plot(time_ideal, x_ideal, color=BLUE, label="Bez oporu")
    axes[0].plot(time_drag, x_drag, color=ORANGE, label="Z oporem")
    axes[0].set(xlabel="Czas t [s]", ylabel="x [m]", title="Położenie poziome")
    axes[0].legend(fontsize=9)
    axes[1].plot(time_ideal, y_ideal, color=BLUE, label="Bez oporu")
    axes[1].plot(time_drag, y_drag, color=ORANGE, label="Z oporem")
    axes[1].set(xlabel="Czas t [s]", ylabel="y [m]", title="Wysokość")
    axes[1].legend(fontsize=9)
    fig.suptitle("Współrzędne w funkcji czasu")
    save(fig, "polozenie_czas.png")

    fig, axes = plt.subplots(1, 2, figsize=(10, 4.2), layout="constrained")
    axes[0].plot(time_ideal, vx_ideal, color=BLUE, label="Bez oporu")
    axes[0].plot(time_drag, vx_drag, color=ORANGE, label="Z oporem")
    axes[0].set(xlabel="Czas t [s]", ylabel="$v_x$ [m/s]", title="Składowa pozioma")
    axes[0].legend(fontsize=9)
    axes[1].plot(time_ideal, vy_ideal, color=BLUE, label="Bez oporu")
    axes[1].plot(time_drag, vy_drag, color=ORANGE, label="Z oporem")
    axes[1].axhline(0.0, color=INK, lw=0.8)
    axes[1].set(xlabel="Czas t [s]", ylabel="$v_y$ [m/s]", title="Składowa pionowa")
    axes[1].legend(fontsize=9)
    fig.suptitle("Składowe prędkości")
    save(fig, "predkosc_czas.png")

    fig, axes = plt.subplots(1, 2, figsize=(10, 4.2), layout="constrained")
    axes[0].plot(time_drag, ax_drag, color=PURPLE)
    axes[0].axhline(0.0, color=INK, lw=0.8)
    axes[0].set(xlabel="Czas t [s]", ylabel="$a_x$ [m/s²]",
                title="Przyspieszenie poziome z oporem")
    axes[1].plot(time_drag, ay_drag, color=GREEN, label="Z oporem")
    axes[1].axhline(-G, color=BLUE, ls="--", label="Bez oporu: $-g$")
    axes[1].set(xlabel="Czas t [s]", ylabel="$a_y$ [m/s²]",
                title="Przyspieszenie pionowe")
    axes[1].legend(fontsize=9)
    fig.suptitle("Przyspieszenie zmienia się wskutek oporu")
    save(fig, "przyspieszenie_czas.png")

    fig, ax = plt.subplots(figsize=(8.5, 4.5), layout="constrained")
    ax_potential = ax.twinx()
    kinetic_line, = ax.plot(
        time_drag, kinetic_drag, color=BLUE, label="Energia kinetyczna"
    )
    potential_line, = ax_potential.plot(
        time_drag, potential_drag, color=GREEN, label="Energia potencjalna"
    )
    energy_line, = ax.plot(
        time_drag, energy_drag, color=ORANGE, label="Suma mechaniczna"
    )
    ax.set(
        xlabel="Czas t [s]",
        ylabel="Energia kinetyczna i suma [J]",
        title="Energia mechaniczna maleje wskutek oporu",
    )
    ax_potential.set_ylabel("Energia potencjalna [J]", color=GREEN)
    ax_potential.tick_params(axis="y", labelcolor=GREEN)
    ax.legend(
        [kinetic_line, potential_line, energy_line],
        [line.get_label() for line in (kinetic_line, potential_line, energy_line)],
        loc="center right",
    )
    save(fig, "energia.png")

    fig, ax = plt.subplots(figsize=(7.5, 5.0), layout="constrained")
    ax.plot(vx_drag, vy_drag, color=PURPLE, label="Ruch z oporem")
    ax.plot(vx_ideal, vy_ideal, color=BLUE, ls="--", label="Ruch bez oporu")
    ax.scatter([vx0], [vy0], color=GREEN, zorder=3, label="Stan początkowy")
    ax.scatter([vx_drag[-1]], [vy_drag[-1]], color=ORANGE, zorder=3,
               label="Uderzenie z oporem")
    ax.set(
        xlabel="$v_x$ [m/s]",
        ylabel="$v_y$ [m/s]",
        title="Portret fazowy składowych prędkości",
    )
    ax.legend(fontsize=9)
    save(fig, "portret_fazowy.png")

    ideal_range = x_ideal[-1]
    ideal_height = float(np.max(y_ideal))
    impact_speed = float(speed_drag[-1])
    dissipated = float(energy_drag[0] - energy_drag[-1])
    print(f"v_x0 = {vx0:.6f} m/s; v_y0 = {vy0:.6f} m/s")
    print(f"Pole przekroju A = {AREA:.8f} m^2")
    print(f"Parametr oporu k = {DRAG_FACTOR:.8f} 1/m")
    print(f"Bez oporu: czas lotu = {flight_time_ideal:.6f} s")
    print(f"Bez oporu: zasięg = {ideal_range:.6f} m; h_max = {ideal_height:.6f} m")
    print(
        f"Z oporem: czas lotu = {time_drag[-1]:.6f} s; "
        f"zasięg = {x_drag[-1]:.6f} m; h_max = {np.max(y_drag):.6f} m"
    )
    print(f"Z oporem: prędkość przy uderzeniu = {impact_speed:.6f} m/s")
    print(f"Utrata energii mechanicznej = {dissipated:.6f} J")
    print(f"Zapisano 6 wykresów w: {OUT}")


if __name__ == "__main__":
    main()
