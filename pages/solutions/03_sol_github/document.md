# Can a metric be reconstructed from a connection?

For a given connection $\Gamma^\lambda_{\mu\nu}$, can we derive the metric
$g_{\mu\nu}$ standing behind it?

## Short answer

Sometimes, but not for an arbitrary connection. If $\Gamma$ is the
Levi-Civita connection of a metric, then the metric must satisfy

$$
\nabla_\lambda g_{\mu\nu}=0,
$$

or, in coordinates,

$$
\partial_\lambda g_{\mu\nu} = \Gamma^\rho_{\lambda\mu}g_{\rho\nu} + \Gamma^\rho_{\lambda\nu}g_{\mu\rho}.
$$

This is a linear, first-order system of partial differential equations for
the components of $g$. A solution must also be symmetric, non-degenerate,
and have the desired signature. In addition, a Levi-Civita connection must
be torsion-free:

$$
\Gamma^\lambda_{\mu\nu}=\Gamma^\lambda_{\nu\mu}.
$$

Thus, knowing a connection does not guarantee that a metric exists. When a
metric does exist, the connection usually determines it only up to an
overall nonzero constant:

$$
g_{\mu\nu}\longmapsto Cg_{\mu\nu},
$$

because a constant rescaling does not change the Christoffel symbols.

## Existence and integrability

Choose a symmetric matrix $g_{\mu\nu}(p)$ at one point $p$. The equation
$\nabla g=0$ parallel-transports this matrix to nearby points. The result is
independent of the path precisely when the chosen matrix is preserved by
the holonomy of the connection. For every closed loop based at $p$, with
parallel-transport matrix $P$, one needs

$$
P^T g(p)P=g(p).
$$

A useful local necessary condition follows by commuting two covariant
derivatives:

$$
0 = [\nabla_\alpha,\nabla_\beta]g_{\mu\nu} = -R^\rho{}_{\mu\alpha\beta}g_{\rho\nu} - R^\rho{}_{\nu\alpha\beta}g_{\mu\rho}.
$$

At a point, these are linear algebraic equations for the unknown entries of
$g_{\mu\nu}(p)$. Curvature transported from other points, or equivalently
the full holonomy condition, supplies the complete integrability test.
Consequently, a practical reconstruction procedure is:

1. Check that the connection is torsion-free.
2. Solve the curvature/holonomy constraints for a symmetric,
   non-degenerate $g(p)$ of the desired signature.
3. Integrate $\nabla_\lambda g_{\mu\nu}=0$ away from $p$.
4. Substitute the result into the Christoffel formula and verify that it
   reproduces the original connection.

The solution need not always be unique up to one constant. The set of all
parallel symmetric bilinear forms is a vector space. Reducible or flat
connections can preserve several independent metrics. For a generic
irreducible metric holonomy, however, the only freedom is the common
constant scale.

If the supplied connection has torsion, it cannot be the Levi-Civita
connection of any metric. It could still be compatible with a metric in a
theory with torsion, but then metric compatibility alone generally does not
select a unique metric.

## Test: the Schwarzschild connection

Work in Schwarzschild coordinates $(t,r,\theta,\phi)$, away from the
coordinate singularity at $r=2M$, and put

$$
f(r)=1-\frac{2M}{r}.
$$

Suppose that only the Schwarzschild connection is given. Some of its
nonzero coefficients are

$$
\begin{aligned}
\Gamma^t{}_{tr}&=\Gamma^t{}_{rt}=\frac{f'}{2f},
&\Gamma^r{}_{tt}&=\frac{ff'}{2},
&\Gamma^r{}_{rr}&=-\frac{f'}{2f},\\
\Gamma^r{}_{\theta\theta}&=-rf,
&\Gamma^r{}_{\phi\phi}&=-rf\sin^2\theta,
&\Gamma^\theta{}_{r\theta}&=\Gamma^\phi{}_{r\phi}=\frac1r,\\
\Gamma^\theta{}_{\phi\phi}&=-\sin\theta\cos\theta,
&\Gamma^\phi{}_{\theta\phi}&=\cot\theta.
\end{aligned}
$$

To try to reconstruct the starting metric, use a diagonal, static,
spherically symmetric ansatz in these coordinates:

$$
ds^2=-A(r)dt^2+B(r)dr^2+C(r)d\theta^2
+D(r)\sin^2\theta\,d\phi^2.
$$

The radial metric-compatibility equations give

$$
\frac{A'}{A}=2\Gamma^t{}_{rt}=\frac{f'}{f},
\qquad
\frac{B'}{B}=2\Gamma^r{}_{rr}=-\frac{f'}{f},
$$

and

$$
\frac{C'}{C}=2\Gamma^\theta{}_{r\theta}=\frac{2}{r},
\qquad
\frac{D'}{D}=2\Gamma^\phi{}_{r\phi}=\frac{2}{r}.
$$

Therefore,

$$
A=c_t f,\qquad B=\frac{c_r}{f},\qquad
C=c_\theta r^2,\qquad D=c_\phi r^2.
$$

The angular compatibility equation with indices
$(\lambda,\mu,\nu)=(\phi,\theta,\phi)$ gives

$$
0=\Gamma^\phi{}_{\phi\theta}g_{\phi\phi}
+\Gamma^\theta{}_{\phi\phi}g_{\theta\theta},
$$

so $c_\phi=c_\theta$. The equations for components that vanish in the
diagonal ansatz are also important. For example,

$$
0 = \nabla_t g_{tr} = -\Gamma^r{}_{tt}g_{rr}-\Gamma^t{}_{tr}g_{tt}
$$

implies $c_r=c_t$, while

$$
0 = \nabla_\theta g_{r\theta} = -\Gamma^\theta{}_{\theta r}g_{\theta\theta} - \Gamma^r{}_{\theta\theta}g_{rr}
$$

implies $c_\theta=c_r$. Hence all four constants coincide:

$$
c_t=c_r=c_\theta=c_\phi=c.
$$

The reconstructed metric is therefore

$$
ds^2=c\left[
-\left(1-\frac{2M}{r}\right)dt^2
+\left(1-\frac{2M}{r}\right)^{-1}dr^2
+r^2d\theta^2+r^2\sin^2\theta\,d\phi^2
\right].
$$

For $c>0$ this has the usual $(-,+,+,+)$ signature. Thus the Schwarzschild
connection reconstructs the Schwarzschild metric, with exactly the expected
undetermined overall constant. The mass parameter $M$ is already encoded in
the connection and is recovered in the radial function $f(r)$.

The $M=0$ case deserves one qualification: the connection is then flat.
Without imposing the static, diagonal, spherically symmetric ansatz, a flat
connection preserves a larger family of constant bilinear forms in affine
Cartesian coordinates. This is an example in which the same connection can
come from more than constant rescalings of one metric.

## Test: the Taub-NUT connection

The Lorentzian Taub-NUT metric has an off-diagonal $t$--$\phi$ component, so
it provides a more substantial test. We use the convention

$$
\Sigma(r)=r^2+\ell^2,
\qquad
\Delta(r)=r^2-2Mr-\ell^2,
\qquad
F(r)=\frac{\Delta}{\Sigma},
$$

and define

$$
q(\theta)=2\ell\cos\theta,
\qquad
\eta=dt+q(\theta)d\phi.
$$

The usual metric in this convention is

$$
ds^2=-F\eta^2+\frac{dr^2}{F}
+\Sigma\left(d\theta^2+\sin^2\theta\,d\phi^2\right).
$$

Changing the convention from $dt+2\ell\cos\theta\,d\phi$ to
$dt-2\ell\cos\theta\,d\phi$ is equivalent to changing the sign of $\ell$
in the formulas below.

### Reading the structure from the connection

Some connection coefficients that are sufficient for the reconstruction
are

$$
\begin{aligned}
\Gamma^t{}_{rt}&=\frac{F'}{2F},
&\Gamma^\phi{}_{rt}&=0,
&\Gamma^r{}_{tt}&=\frac{FF'}{2},\\
\Gamma^r{}_{rr}&=-\frac{F'}{2F},
&\Gamma^\theta{}_{r\theta}
 &=\Gamma^\phi{}_{r\phi}=\frac{r}{\Sigma},
&\Gamma^r{}_{\theta\theta}&=-rF,\\
\Gamma^t{}_{r\phi}
 &=\frac{q}{2}\left(\frac{F'}{F}-\frac{2r}{\Sigma}\right),
&\Gamma^r{}_{t\phi}&=\frac{qFF'}{2}.
\end{aligned}
$$

As usual, coefficients related by symmetry of the two lower indices are
understood. The characteristic Taub-NUT twist can be read directly from
the connection:

$$
\frac{\Gamma^r{}_{t\phi}}{\Gamma^r{}_{tt}} = q(\theta) = 2\ell\cos\theta,
$$

where the denominator is nonzero. Similarly,

$$
F=-\frac{1}{r}\Gamma^r{}_{\theta\theta},
\qquad
\Sigma=\frac{r}{\Gamma^\theta{}_{r\theta}}.
$$

Thus the radial functions and the twisted one-form are encoded in the
connection rather than being additional metric data.

### Solving the compatibility equations

Guided by these symmetries, take the ansatz

$$
ds^2=-A(r)\eta^2+B(r)dr^2
+C(r)\left(d\theta^2+\sin^2\theta\,d\phi^2\right).
$$

In the coordinate basis its nonzero components are

$$
\begin{aligned}
g_{tt}&=-A,
&g_{t\phi}&=-Aq,
&g_{rr}&=B,\\
g_{\theta\theta}&=C,
&g_{\phi\phi}&=C\sin^2\theta-Aq^2.
\end{aligned}
$$

The $(r,t,t)$, $(r,r,r)$, and $(r,\theta,\theta)$ components of
$\nabla g=0$ give

$$
\frac{A'}{A}=2\Gamma^t{}_{rt}=\frac{F'}{F},
\qquad
\frac{B'}{B}=2\Gamma^r{}_{rr}=-\frac{F'}{F},
$$

and

$$
\frac{C'}{C} = 2\Gamma^\theta{}_{r\theta} = \frac{2r}{\Sigma}.
$$

After integration,

$$
A=aF,
\qquad
B=\frac{b}{F},
\qquad
C=c\Sigma,
$$

where $a,b,c$ are initially independent constants. As in the Schwarzschild
example, equations for components that vanish in the ansatz relate these
constants. First,

$$
\begin{aligned}
0=\nabla_t g_{tr}
&=-\Gamma^r{}_{tt}g_{rr}
  -\Gamma^t{}_{tr}g_{tt}
  -\Gamma^\phi{}_{tr}g_{t\phi}\\
&=\frac{F'}{2}(a-b),
\end{aligned}
$$

so $a=b$. Next,

$$
\begin{aligned}
0=\nabla_\theta g_{r\theta}
&=-\Gamma^\theta{}_{\theta r}g_{\theta\theta}
  -\Gamma^r{}_{\theta\theta}g_{rr}\\
&=r(b-c),
\end{aligned}
$$

so $b=c$. Hence

$$
a=b=c=k.
$$

The compatibility equations for $g_{t\phi}$ and $g_{\phi\phi}$ are then
automatically satisfied. For instance, the $(r,t,\phi)$ equation uses both
$\Gamma^t{}_{r\phi}$ and $\Gamma^\phi{}_{r\phi}$ and returns
$\partial_r g_{t\phi}=-qA'$, as required.

The reconstructed metric is therefore

$$
\begin{aligned}
ds^2=k\Bigg[&
-\frac{r^2-2Mr-\ell^2}{r^2+\ell^2}
 \left(dt+2\ell\cos\theta\,d\phi\right)^2 \\
&+\frac{r^2+\ell^2}{r^2-2Mr-\ell^2}\,dr^2
+(r^2+\ell^2)
 \left(d\theta^2+\sin^2\theta\,d\phi^2\right)
\Bigg].
\end{aligned}
$$

For $k>0$, this is Lorentzian wherever $F\neq0$; the coordinate vector
$\partial_t$ is timelike in a region where $F>0$. Therefore, on a generic
non-flat region, the Taub-NUT connection recovers
the starting Taub-NUT metric up to the same unavoidable overall scale as in
the Schwarzschild case. Both $M$ and the NUT parameter $\ell$ occur in the
connection.

The limit $\ell\to0$ gives

$$
\eta\to dt,
\qquad
\Sigma\to r^2,
\qquad
F\to1-\frac{2M}{r},
$$

so the reconstruction reduces continuously to the Schwarzschild result.
This also checks that the off-diagonal terms have the correct normalization
and sign.

This calculation is local. Globally, the one-form $\eta$ requires the usual
Taub-NUT patching around the polar axes, and questions involving the Misner
string or a periodic time coordinate require global information that cannot
be inferred from connection coefficients in a single coordinate chart.

## Conclusion

A connection determines a metric exactly when it is torsion-free and its
holonomy preserves a non-degenerate symmetric bilinear form of the required
signature. Reconstruction means solving $\nabla g=0$. For the generic
Schwarzschild and Taub-NUT connections, this procedure returns the original
metric up to a constant overall scale, which no Levi-Civita connection can
determine. The Taub-NUT example additionally shows that off-diagonal metric
components can be reconstructed: their twisting function is already
encoded in the mixed connection coefficients.
