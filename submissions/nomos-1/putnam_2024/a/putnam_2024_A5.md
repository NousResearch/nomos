# putnam_2024_A5

## Problem

Consider a circle $\Omega$ with radius $9$ and center at the origin $(0,0)$, and a disc $\Delta$ with radius $1$ and center at $(r,0)$, where $0 \le r \le 8$. Two points $P$ and $Q$ are chosen independently and uniformly at random on $\Omega$. Which value(s) of $r$ minimize the probability that the chord $PQ$ intersects $\Delta$?

## Submission

We consider the circle $\Omega$ of radius $9$ centered at the origin.  Two points $P,Q$ are chosen independently uniformly on $\Omega$; write $P=(9\cos\alpha,\,9\sin\alpha$, $Q=(9\cos\beta,\,9\sin\beta$ with $\alpha,\beta\sim\mathrm{Uniform}[0,2\pi)$.  The chord $PQ$ is the line through these points.  Its distance from the fixed point $C=(r,0)$ (with $0\le r\le8$) is

\[
d = \bigl|9\cos\tfrac{\alpha-\beta}{2} - r\cos\tfrac{\alpha+\beta}{2}\bigr|.
\]

**Derivation:** The line through $P$ and $Q$ can be written as $x\cos\mu + y\sin\mu = 9\cos\frac{\alpha-\beta}{2}$ where $\mu=\frac{\alpha+\beta}{2}$; the signed distance from $C$ to this line is $r\cos\mu-9\cos\frac{\alpha-\beta}{2}$, and its absolute value is $d$.

Set $u=\frac{\alpha-\beta}{2$, $v=\frac{\alpha+\beta}{2}$.  The map $(\alpha,\beta)\mapsto(u,v)$ has Jacobian $2$, hence $(u,v)$ are independent with $u\sim\mathrm{Uniform}[0,\pi)$, $v\sim\mathrm{Uniform}[0,2\pi)$.  Therefore

\[
\Pr(\text{chord intersects }\Delta) = \frac1{2\pi^2}\int_0^\pi\int_0^{2\pi} \mathbf{1}_{\{d\le1\}\,dv\,du.
\]

Fix $v$ and put $b=r\cos v$.  The condition becomes $|9\cos u - b|\le1$, i.e. $\cos u\in\bigl[\frac{b-1}{9},\frac{b+1}{9}\bigr]$.  Because $|b|\le r\le8$, this interval lies inside $[-1,1]$.  For $u\in[0,\pi)$ the set where $\cos u$ lies in a given subinterval $[L,U]\subseteq[-1,1]$ has length $\arccos L-\arccos U$.  Hence

\[
\ell(v)=\int_0^\pi \mathbf{1}_{\{|9\cos u-b|\le1\}\,du = \arccos\frac{b-1}{9}-\arccos\frac{b+1}{9}.
\]

Using $\arccos x = \frac\pi2-\arcsin x$ we rewrite

\[
\ell(v)= \arcsin\frac{b+1}{9}-\arcsin\frac{b-1}{9}.
\]

Thus

\[
\Pr(r)=\frac1{2\pi^2}\int_0^{2\pi}\ell(v)\,dv.
\]

The integrand depends only on $\cos v$; by symmetry

\[
\int_0^{2\pi}f(\cos v)\,dv = 2\int_{-1}^{1}\frac{f(t)}{\sqrt{1-t^2}\,dt,
\]

so

\[
\Pr(r)=\frac1{\pi^2}\int_{-1}^{1}\Bigl(\arcsin\frac{rt+1}{9}-\arcsin\frac{rt-1}{9}\Bigr)\frac{dt}{\sqrt{1-t^2}.
\]

The integrand is even, therefore

\[
\Pr(r)=\frac2{\pi^2}\int_0^{1}\Bigl(\arcsin\frac{rt+1}{9}-\arcsin\frac{rt-1}{9}\Bigr)\frac{dt}{\sqrt{1-t^2}.
\]

Now substitute $t=\sin\theta$, $dt=\cos\theta\,d\theta$, $\frac{dt}{\sqrt{1-t^2}=d\theta$, $\theta\in[0,\frac\pi2$:

\[
\Pr(r)=\frac2{\pi^2}\int_0^{\pi/2}\Bigl(\arcsin\frac{r\sin\theta+1}{9}-\arcsin\frac{r\sin\theta-1}{9}\Bigr)d\theta. \tag{1}
\]

Differentiate (1) with respect to $r$ (the integrand is smooth for $0<r<8$ and the integral converges at the endpoints):

\[
\Pr'(r)=\frac2{\pi^2}\int_0^{\pi/2}\Bigl(
\frac{\sin\theta}{\sqrt{81-(r\sin\theta+1)^2}-\frac{\sin\theta}{\sqrt{81-(r\sin\theta-1)^2}\Bigr)d\theta.
\]

For $0<r\le8$ and $\theta>0$ we have $(r\sin\theta+1)^2>(r\sin\theta-1)^2$, hence $81-(r\sin\theta+1)^2<81-(r\sin\theta-1)^2$ and consequently

\[
\frac1{\sqrt{81-(r\sin\theta+1)^2}>\frac1{\sqrt{81-(r\sin\theta-1)^2}.
\]

Since $\sin\theta\ge0$, the integrand is positive for every $\theta>0$; thus $\Pr'(r)>0$ for $r>0$.  At $r=0$ the two terms are equal, so $\Pr'(0)=0$.  Hence $\Pr(r)$ is strictly increasing on $(0,8]$ and continuous at $0$.  Consequently the minimum occurs at the left endpoint $r=0$.

\[
\boxed{0}
\]
