# Rzut ukośny — od ruchu idealnego do oporu powietrza

*Raport obliczeniowy z wyprowadzeniem równań, symulacją numeryczną i wykresami.*

**Temat:** ruch ciała rzuconego pod kątem do poziomu.  
**Dane początkowe:** prędkość $v_0=36\,\mathrm{m/s}$, kąt $\alpha=02^\circ=2^\circ$.  
**Metoda:** rozwiązanie analityczne bez oporu oraz numeryczne rozwiązanie równań ruchu z oporem kwadratowym.  
**Charakter wyników:** ilustracja modelowa, nie pomiar laboratoryjny.

Rzut ukośny można rozłożyć na dwa ruchy: poziomy i pionowy. Bez oporu powietrza są one niezależne, a tor jest parabolą. Opór zależy od wektora prędkości, więc w modelu z powietrzem składowe ruchu są sprzężone, a równania rozwiązuje się numerycznie.

## Spis treści

1. [Cel i model fizyczny](#1-cel-i-model-fizyczny)
2. [Rzut bez oporu powietrza](#2-rzut-bez-oporu-powietrza)
3. [Rzut z oporem powietrza](#3-rzut-z-oporem-powietrza)
4. [Wyniki i interpretacja wykresów](#4-wyniki-i-interpretacja-wykresów)
5. [Metoda numeryczna i kontrola wyników](#5-metoda-numeryczna-i-kontrola-wyników)
6. [Kod i odtwarzanie wykresów](#6-kod-i-odtwarzanie-wykresów)
7. [Wnioski](#7-wnioski)

---

## 1. Cel i model fizyczny

### 1.1. Układ współrzędnych i założenia

Początek układu współrzędnych umieszczono w punkcie wyrzutu. Oś $x$ jest pozioma i skierowana w kierunku rzutu, a oś $y$ pionowa i skierowana do góry. Podłoże jest poziome, zatem punkt lądowania ma wysokość $y=0$.

Przyjęto następujące założenia:

- przyspieszenie grawitacyjne jest stałe i wynosi $g=9{,}81\,\mathrm{m/s^2}$;
- prędkość początkowa ma wartość $v_0=36\,\mathrm{m/s}$ i tworzy z poziomem kąt $2^\circ$;
- wiatr nie występuje, a gęstość powietrza i współczynnik oporu są stałe;
- ciało zamodelowano jako gładką kulę o stałej masie i średnicy;
- pominięto obrót (efekt Magnusa), siłę nośną, siłę wyporu Archimedesa i zmianę wysokości terenu;
- w modelu z oporem uwzględniono opór kwadratowy (prawo Rayleigha), odpowiedni dla ruchu kuli w powietrzu przy rozpatrywanych liczbach Reynoldsa.

Zapis „02” zinterpretowano jako kąt dwóch stopni ($2^\circ$). W obliczeniach numerycznych kąt wyrażono w radianach:

$$
\alpha = 2^\circ\frac{\pi}{180^\circ} = 0{,}0349066\,\mathrm{rad}.
$$

![Porównanie toru rzutu bez oporu i z oporem kwadratowym](files/rzut_ukosny/tor_ruchu.png)

*Rysunek 1. Tor dla obu modeli. Skala pionowa została powiększona dla czytelności; różnice zasięgu są pokazane w skali poziomej.*

### 1.2. Symbole i jednostki

| Symbol | Znaczenie | Jednostka SI |
| :--- | :--- | :---: |
| $t$ | czas od wyrzutu | $\mathrm{s}$ |
| $x$, $y$ | położenie poziome i wysokość | $\mathrm{m}$ |
| $v_x$, $v_y$, $v$ | składowe i wartość prędkości | $\mathrm{m/s}$ |
| $a_x$, $a_y$ | składowe przyspieszenia | $\mathrm{m/s^2}$ |
| $m$ | masa ciała | $\mathrm{kg}$ |
| $g$ | przyspieszenie grawitacyjne | $\mathrm{m/s^2}$ |
| $\alpha$ | kąt wyrzutu | $\mathrm{rad}$ (w danych także $^\circ$) |
| $\rho$ | gęstość powietrza | $\mathrm{kg/m^3}$ |
| $C_D$ | bezwymiarowy współczynnik oporu | $-$ |
| $A$ | pole przekroju poprzecznego | $\mathrm{m^2}$ |
| $c$ | współczynnik w prawie oporu $F_D=c v^2$ | $\mathrm{kg/m}$ |
| $k=c/m$ | parametr w równaniu przyspieszenia oporu | $\mathrm{m^{-1}}$ |
| $H$, $R$ | maksymalna wysokość i zasięg | $\mathrm{m}$ |
| $E_k$, $E_p$, $E_m$ | energia kinetyczna, potencjalna i mechaniczna | $\mathrm{J}$ |

## 2. Rzut bez oporu powietrza

### 2.1. Rozłożenie prędkości początkowej

W chwili początkowej $t=0$ wektor prędkości $\vec v_0$ tworzy z poziomem kąt $\alpha$. Jego składowe wzdłuż osi układu współrzędnych wynoszą:

$$
v_{x0} = v_0\cos\alpha,
\qquad
v_{y0} = v_0\sin\alpha.
$$

Dla przyjętych danych początkowych ($v_0=36\,\mathrm{m/s}$, $\alpha=2^\circ$):

$$
v_{x0} = 36\cos(2^\circ) = 35{,}9781\,\mathrm{m/s},
\qquad
v_{y0} = 36\sin(2^\circ) = 1{,}25638\,\mathrm{m/s}.
$$

### 2.2. Równania ruchu i ich wyprowadzenie

W próżni (przy pominięciu oporów powietrza) jedyną siłą działającą na ciało po wyrzucie jest stała siła grawitacji $\vec F_g = (0, -mg)$, skierowana pionowo w dół. Z drugiej zasady dynamiki Newtona $m\vec a = \vec F_g$ wynika:

$$
m\ddot{x} = 0,
\qquad
m\ddot{y} = -mg,
$$

stąd równania przyspieszeń przyjmują postać:

$$
\ddot{x} = 0,
\qquad
\ddot{y} = -g.
$$

Ruch w kierunku poziomym jest ruchem jednostajnym prostoliniowym ze stałą prędkością $v_{x0}$ ($a_x = 0$), natomiast ruch w kierunku pionowym jest ruchem jednostajnie zmiennym ze stałym przyspieszeniem ziemskim skierowanym w dół ($a_y = -g$).

Po scałkowaniu równań przyspieszenia z uwzględnieniem warunków początkowych $x(0)=0$, $y(0)=0$, $\dot{x}(0)=v_{x0}$ oraz $\dot{y}(0)=v_{y0}$ równania prędkości mają postać:

$$
v_x(t) = v_{x0},
\qquad
v_y(t) = v_{y0}-gt,
$$

natomiast równania położenia:

$$
\begin{aligned}
x(t) &= v_{x0}t = v_0\cos\alpha\,t, \\
y(t) &= v_{y0}t - \frac{1}{2}gt^2 = v_0\sin\alpha\,t - \frac{1}{2}gt^2.
\end{aligned}
$$

Równanie toru wyznacza się poprzez eliminację czasu $t$. Z równania ruchu poziomego wyznacza się czas $t = x/(v_0\cos\alpha)$ i podstawia do równania współrzędnej pionowej $y(t)$:

$$
y(x) = x\tan\alpha - \frac{gx^2}{2v_0^2\cos^2\alpha}.
$$

Równanie to przedstawia parabolę o ramionach skierowanych w dół (współczynnik przy $x^2$ jest ujemny). Kształt toru jest bezpośrednią konsekwencją złożenia jednostajnego ruchu w poziomie oraz jednostajnie zmiennego ruchu w pionie.

### 2.3. Czas wznoszenia, maksymalna wysokość i zasięg

W fazie wznoszenia składowa pionowa prędkości $v_y(t) = v_{y0} - gt$ jest dodatnia, a jej zwrot jest przeciwny do przyspieszenia grawitacyjnego, co oznacza ruch jednostajnie opóźniony. Grawitacja nieustannie zmniejsza prędkość pionową ze stałą szybkością $g$, aż w najwyższym punkcie toru (wierzchołku paraboli) zostaje ona zredukowana do zera ($v_y = 0$). W tym punkcie wektor prędkości ciała staje się ściśle poziomy: $\vec v(t_{\mathrm{wzn}}) = (v_{x0}, 0)$.

Z warunku zerowania składowej pionowej prędkości $v_y(t_{\mathrm{wzn}}) = v_{y0} - gt_{\mathrm{wzn}} = 0$ wyznacza się czas wznoszenia:

$$
t_{\mathrm{wzn}} = \frac{v_0\sin\alpha}{g}.
$$

Natychmiast po minięciu wierzchołka paraboli, pod nieprzerwanym działaniem przyspieszenia grawitacyjnego $a_y = -g$, składowa pionowa prędkości przyjmuje wartości ujemne ($v_y < 0$), a ciało przechodzi w fazę opadania ruchem jednostajnie przyspieszonym.

Gdy punkty wyrzutu i lądowania znajdują się na tej samej wysokości ($y=0$), z równania $y(T) = v_{y0}T - \frac{1}{2}gT^2 = 0$ (dla $T > 0$) wynika, że faza wznoszenia i opadania trwają tyle samo, a całkowity czas lotu wynosi:

$$
T = 2 t_{\mathrm{wzn}} = \frac{2v_0\sin\alpha}{g}.
$$

Maksymalna wysokość wzniesienia $H$ odpowiada położeniu pionowemu w chwili $t_{\mathrm{wzn}}$:

$$
H = y(t_{\mathrm{wzn}}) = \frac{v_0^2\sin^2\alpha}{2g}.
$$

Zasięg rzutu $R$ to odległość pozioma przebyta przez ciało do momentu upadku na podłoże w chwili $T$:

$$
R = x(T) = v_0\cos\alpha\,T = \frac{v_0^2\sin(2\alpha)}{g}.
$$

W chwili lądowania ($t=T$) składowa pozioma wynosi nadal $v_x(T) = v_{x0}$, natomiast pionowa $v_y(T) = -v_{y0}$. Wartość prędkości końcowej wynosi $v(T) = \sqrt{v_{x0}^2 + (-v_{y0})^2} = v_0$, co jest w pełni zgodne z zasadą zachowania energii mechanicznej w polu potencjalnym przy braku oporów ruchu.

Dla danych początkowych $\alpha=2^\circ$ i $v_0=36\,\mathrm{m/s}$ model analityczny daje:

| Wielkość | Wzór | Wynik |
| :--- | :--- | ---: |
| Czas wznoszenia $t_{\mathrm{wzn}}$ | $v_0\sin\alpha/g$ | $0{,}128071\,\mathrm{s}$ |
| Czas lotu $T$ | $2v_0\sin\alpha/g$ | $0{,}256143\,\mathrm{s}$ |
| Maksymalna wysokość $H$ | $v_0^2\sin^2\alpha/(2g)$ | $0{,}080453\,\mathrm{m}$ |
| Zasięg $R$ | $v_0^2\sin(2\alpha)/g$ | $9{,}21553\,\mathrm{m}$ |

### 2.4. Prędkość i przyspieszenie w locie idealnym

Wartość chwilowej prędkości ciała w dowolnym momencie lotu wynosi:

$$
v(t) = \sqrt{v_x^2(t)+v_y^2(t)} = \sqrt{(v_0\cos\alpha)^2+(v_0\sin\alpha-gt)^2}.
$$

Wektor przyspieszenia jest niezmienny przez cały czas trwania ruchu i wynosi $\vec a(t) = (0, -g)$:

$$
a_x = 0,
\qquad
a_y = -g = -9{,}81\,\mathrm{m/s^2}.
$$

Prędkość osiąga minimum równe $v_{\min} = v_{x0} = v_0\cos\alpha$ w najwyższym punkcie toru, natomiast w punktach wyrzutu i lądowania osiąga maksimum równe $v_0$.

## 3. Rzut z oporem powietrza

### 3.1. Prawo oporu kwadratowego

Dla kuli poruszającej się w powietrzu wartość siły oporu określa zależność:

$$
F_D = \frac{1}{2}\rho C_D A v^2,
\qquad
v = \sqrt{v_x^2+v_y^2}.
$$

Siła ma zwrot przeciwny do wektora prędkości, co w ujęciu wektorowym ma postać:

$$
\vec F_D = -\frac{1}{2}\rho C_D A\,v\,\vec v.
$$

Wprowadzając oznaczenia pomocnicze:

$$
c = \frac{1}{2}\rho C_D A,
\qquad
k = \frac{c}{m} = \frac{\rho C_D A}{2m}.
$$

Równanie ruchu Newtona przyjmuje wówczas postać:

$$
m\frac{d\vec v}{dt} = m\vec g - cv\vec v,
\qquad
\frac{d\vec v}{dt} = \vec g - kv\vec v,
$$

gdzie $\vec g=(0,-g)$. Układ równań w rzutach na osie ma postać:

$$
\begin{aligned}
\dot{x} &= v_x, & \dot{y} &= v_y, \\
\dot{v}_x &= -k\sqrt{v_x^2+v_y^2}\,v_x, & \dot{v}_y &= -g-k\sqrt{v_x^2+v_y^2}\,v_y.
\end{aligned}
$$

Z fizycznego punktu widzenia obecność modułu prędkości całkowitej $v = \sqrt{v_x^2+v_y^2}$ w obu równaniach oznacza, że ruch w kierunku poziomym i pionowym nie może być rozpatrywany niezależnie — następuje nieliniowe sprzężenie obu składowych. Ponadto układ równań różniczkowych staje się nieliniowy i nie posiada ścisłego rozwiązania analitycznego w funkcjach elementarnych.

Wpływ oporu powietrza na poszczególne fazy lotu charakteryzuje się wyraźną asymetrią fizyczną:
1. **W fazie wznoszenia ($v_y > 0$):** pionowa składowa siły oporu $F_{Dy} = -c v v_y$ działa w dół, a więc zgodnie z grawitacją. Wypadkowe pionowe opóźnienie wynosi $|a_y| = g + k v v_y > g$, co powoduje szybsze wygaszanie prędkości pionowej niż w próżni.
2. **W apogeum toru ($v_y = 0$):** składowa pionowa prędkości chwilowo się zeruje, a opór działa wyłącznie w kierunku poziomym ($F_D = F_{Dx}$). W tym punkcie przyspieszenie pionowe wynosi ściśle $a_y = -g$.
3. **W fazie opadania ($v_y < 0$):** pionowa składowa siły oporu $F_{Dy} = -c v v_y > 0$ działa w górę, przeciwdziałając przyspieszeniu grawitacyjnemu. Wypadkowe przyspieszenie pionowe jest wówczas mniejsze co do modułu niż przyspieszenie ziemskie: $|a_y| = g - k v |v_y| < g$.

### 3.2. Parametry modelu oporu

Do obliczeń przyjęto parametry kuli zbliżone do piłki:

| Parametr | Wartość | Jednostka SI |
| :--- | ---: | :---: |
| Masa $m$ | $0{,}145$ | $\mathrm{kg}$ |
| Średnica $d$ | $0{,}073$ | $\mathrm{m}$ |
| Gęstość powietrza $\rho$ | $1{,}225$ | $\mathrm{kg/m^3}$ |
| Współczynnik oporu $C_D$ | $0{,}47$ | $1$ |
| Przyspieszenie grawitacyjne $g$ | $9{,}81$ | $\mathrm{m/s^2}$ |

Pole przekroju poprzecznego kuli wynosi:

$$
A = \pi\left(\frac{d}{2}\right)^2 = \pi(0{,}0365\,\mathrm{m})^2 = 0{,}00418539\,\mathrm{m^2}.
$$

Wartości współczynników wynoszą:

$$
c = \frac{1}{2}\rho C_D A = 0{,}00120412\,\mathrm{kg/m},
\qquad
k = \frac{c}{m} = 0{,}00830944\,\mathrm{m^{-1}}.
$$

Są to założone parametry modelowe. Rzeczywisty współczynnik $C_D$ może zależeć m.in. od kształtu, chropowatości, rotacji oraz liczby Reynoldsa.

### 3.3. Bilans energii i dysypacja

Całkowita energia mechaniczna ciała w jednorodnym polu grawitacyjnym jest sumą energii kinetycznej ruchu postępowego i energii potencjalnej grawitacji:

$$
E_m = E_k + E_p = \frac{1}{2}mv^2 + mgy.
$$

Siła oporu aerodynamicznego $\vec F_D$ jest nieliniową siłą dysypatywną, która wykonuje nad poruszającym się ciałem pracę ujemną. Szybkość utraty energii mechanicznej (moc siły oporu) określa iloczyn skalarny wektora siły i wektora prędkości:

$$
\frac{dE_m}{dt} = \vec F_D\cdot\vec v = -cv^3 = -\frac{1}{2}\rho C_D A\,v^3 \le 0.
$$

Pochodna ta jest stale ujemna dla każdego stanu ruchu ($v > 0$). Energia mechaniczna układu monotonicznie maleje w czasie — zostaje nieodwracalnie rozproszona (zdysypowana), przekształcając się w energię kinetyczną zawirowań powietrza oraz energię wewnętrzną (ciepło) ośrodka i ciała. W modelu idealnym siły dysypatywne nie występują, a suma $E_k+E_p$ pozostaje ściśle stała.

## 4. Wyniki i interpretacja wykresów

Numeryczne rozwiązanie równań z oporem daje następujące przybliżone wyniki:

| Wielkość | Bez oporu | Z oporem kwadratowym |
| :--- | ---: | ---: |
| Czas lotu | $0{,}256143\,\mathrm{s}$ | $0{,}252954\,\mathrm{s}$ |
| Maksymalna wysokość | $0{,}080453\,\mathrm{m}$ | $0{,}078474\,\mathrm{m}$ |
| Zasięg | $9{,}21553\,\mathrm{m}$ | $8{,}77305\,\mathrm{m}$ |
| Szybkość przy lądowaniu | $36{,}0000\,\mathrm{m/s}$ | $33{,}4706\,\mathrm{m/s}$ |

W modelu idealnym prędkość przy lądowaniu ma dokładnie taką samą wartość jak prędkość początkowa ($v(T) = v_0$), ponieważ ciało wraca na ten sam poziom odniesienia ($y=0$), a energia mechaniczna jest zachowana. W modelu z oporem siła aerodynamiczna wykonuje pracę ujemną, wskutek czego prędkość uderzenia o podłoże maleje do ok. $33{,}47\,\mathrm{m/s}$, a zasięg ulega skróceniu o ok. $4{,}8\%$.

![Położenie poziome i wysokość w funkcji czasu w obu modelach](files/rzut_ukosny/polozenie_czas.png)

*Rysunek 2. Przebiegi współrzędnych $x(t)$ oraz $y(t)$. Opór powietrza powoduje nieliniowe hamowanie ruchu poziomego oraz skrócenie czasu trwania lotu i maksymalnej wysokości.*

![Składowe prędkości poziomej i pionowej w funkcji czasu](files/rzut_ukosny/predkosc_czas.png)

*Rysunek 3. Składowe prędkości: bez oporu $v_x$ jest stałe, a $v_y$ maleje ściśle liniowo. Z oporem $v_x$ maleje monotonicznie wskutek hamowania, a $v_y$ osiąga zero w apogeum i kończy lot z mniejszą wartością bezwzględną przy lądowaniu.*

![Składowe przyspieszenia z oporem i porównanie pionowego przyspieszenia z g](files/rzut_ukosny/przyspieszenie_czas.png)

*Rysunek 4. Ewolucja składowych przyspieszenia: przyspieszenie poziome $a_x$ jest stale ujemne. Przyspieszenie pionowe w fazie wznoszenia przekracza co do modułu $g$ ($a_y < -g$), w apogeum wynosi dokładnie $-g$, a w fazie opadania jest mniejsze co do modułu ($a_y > -g$).*

![Energia kinetyczna, potencjalna i suma mechaniczna w modelu z oporem](files/rzut_ukosny/energia.png)

*Rysunek 5. Bilans energetyczny w locie z oporem: energia mechaniczna monotonicznie maleje o ok. $12{,}74\,\mathrm{J}$ (ok. $13{,}6\%$ energii początkowej) wskutek pracy siły oporu.*

![Portret fazowy prędkości z oporem oraz bez oporu](files/rzut_ukosny/portret_fazowy.png)

*Rysunek 6. Portret fazowy składowych prędkości $(v_x, v_y)$: pionowy odcinek odpowiada ruchowi idealnemu ($v_x = \mathrm{const}$), natomiast krzywa wygięta w lewo odzwierciedla jednoczesne wygaszanie obu składowych prędkości przez opór.*

Przy małym kącie wyrzutu ($2^\circ$) składowa początkowej prędkości skierowana do góry wynosi zaledwie $1{,}26\,\mathrm{m/s}$, podczas gdy składowa pozioma wynosi prawie $36\,\mathrm{m/s}$. Lot charakteryzuje się krótkim czasem trwania ($T \approx 0{,}25\,\mathrm{s}$) oraz bardzo niskim pułapem ($H \approx 8\,\mathrm{cm}$). Mimo to siła oporu działa nieprzerwanie, redukując głównie pęd poziomy ciała i skracając zasięg rzutu.

## 5. Metoda numeryczna i kontrola wyników

Wektor stanu układu ma postać:

$$
\mathbf{s}(t) =
\begin{pmatrix}
x & y & v_x & v_y \\
\end{pmatrix}^{\mathsf T},
\qquad
\dot{\mathbf{s}} = \mathbf{f}(\mathbf{s}).
$$

Równania ruchu z oporem rozwiązano klasyczną metodą Rungego–Kutty czwartego rzędu (RK4). Dla kroku $\Delta t$ i prawej strony $\mathbf{f}$ kolejne współczynniki nachylenia wynoszą:

$$
\begin{aligned}
\mathbf{k}_1 &= \mathbf{f}(\mathbf{s}_n), \\
\mathbf{k}_2 &= \mathbf{f}\left(\mathbf{s}_n+\frac{\Delta t}{2}\mathbf{k}_1\right), \\
\mathbf{k}_3 &= \mathbf{f}\left(\mathbf{s}_n+\frac{\Delta t}{2}\mathbf{k}_2\right), \\
\mathbf{k}_4 &= \mathbf{f}\left(\mathbf{s}_n+\Delta t\,\mathbf{k}_3\right),
\end{aligned}
$$

a nowy stan w kolejnym kroku wyznacza wzór:

$$
\mathbf{s}_{n+1} = \mathbf{s}_n + \frac{\Delta t}{6}(\mathbf{k}_1+2\mathbf{k}_2+2\mathbf{k}_3+\mathbf{k}_4).
$$

W skrypcie użyto $\Delta t=2\cdot10^{-4}\,\mathrm{s}$. Obliczenia kończą się, gdy wysokość po raz pierwszy spadnie poniżej zera. Położenie i czas uderzenia są interpolowane liniowo pomiędzy ostatnim punktem nad podłożem a pierwszym punktem pod nim, dzięki czemu punkt końcowy odpowiada $y=0$.

Model bez oporu nie wymaga całkowania numerycznego: jego rozwiązanie analityczne służy tu także jako porównanie. Wartości tabelaryczne są zaokrąglone; zmiana kroku całkowania może zmienić ostatnie cyfry wyniku modelu z oporem. Parametry oporu są przybliżone, więc wynik symulacji należy interpretować jako ilustrację modelu, a nie dokładną prognozę lotu dowolnego ciała.

## 6. Kod i odtwarzanie wykresów

Wykresy utworzono lokalnie za pomocą Pythona, NumPy i Matplotlib. Pełny skrypt jest również dostępny jako [`generuj_wykresy.py`](generuj_wykresy.py). W katalogu raportu należy uruchomić:

```bash
python -m pip install numpy matplotlib
python generuj_wykresy.py
```

Skrypt zapisuje sześć obrazów PNG do `files/rzut_ukosny/`. Poniżej znajduje się kompletny kod użyty do ich wygenerowania.

```python
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
```

## 7. Wnioski

1. W modelu idealnym (bez oporu powietrza) ruch poziomy i pionowy są niezależne: składowa pozioma jest ruchem jednostajnym prostoliniowym ($v_x = \mathrm{const}$), a składowa pionowa ruchem jednostajnie zmiennym pod wpływem stałego przyspieszenia grawitacyjnego $a_y = -g$. W najwyższym punkcie toru prędkość pionowa pod wpływem grawitacji zostaje zredukowana do zera ($v_y = 0$), po czym następuje faza przyspieszonego opadania.
2. W modelu rzeczywistym z oporem kwadratowym składowe prędkości ulegają nieliniowemu sprzężeniu poprzez całkowitą szybkość $v = \sqrt{v_x^2 + v_y^2}$. Opór powietrza łamie symetrię paraboli, przekształcając tor w asymetryczną trajektorię balistyczną.
3. W fazie wznoszenia siła oporu działa w dół, sumując się z grawitacją ($|a_y| > g$). W apogeum toru opór pionowy znika ($a_y = -g$), natomiast w fazie opadania opór działa w górę, zmniejszając wypadkowe przyspieszenie ($|a_y| < g$).
4. Siła oporu ma charakter dysypatywny i wykonuje ujemną pracę nad ciałem, co prowadzi do monotonicznego spadku energii mechanicznej (w rozpatrywanym przypadku ubytek wynosi ok. $12{,}74\,\mathrm{J}$, czyli $13{,}6\%$ energii początkowej). Skutkuje to skróceniem zasięgu rzutu z $9{,}22\,\mathrm{m}$ do $8{,}77\,\mathrm{m}$ oraz obniżeniem prędkości przy uderzeniu w podłoże do $33{,}47\,\mathrm{m/s}$.
5. Zastosowanie numerycznej metody Rungego–Kutty IV rzędu (RK4) z krokiem $\Delta t = 2\cdot 10^{-4}\,\mathrm{s}$ oraz liniową interpolacją punktu uderzenia o podłoże ($y=0$) umożliwia dokładne wyznaczenie parametrów trajektorii i bilansu energetycznego układu, dla którego brak jest elementarnych rozwiązań analitycznych.
