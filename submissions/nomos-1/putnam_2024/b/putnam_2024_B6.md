# putnam_2024_B6

## Problem

For a real number $a$, let $F_a(x) = \sum_{n \ge 1} n^a e^{2n} x^{n^2}$ for $0 \le x < 1$. Find a real number $c$ such that
$$\lim_{x \to 1^-} F_a(x) e^{-1/(1-x)} = 0 \text{ for all } a < c, \text{ and}$$
$$\lim_{x \to 1^-} F_a(x) e^{-1/(1-x)} = \infty \text{ for all } a > c.$$

## Submission

The answer is $\boxed{-\dfrac12}$.

**Proof.**  
Let $t = 1-x$ with $0<t<1$ and $s = -\ln x = -\ln(1-t)$. As $t\to 0^+$ we have $t \le s \le \frac{t}{1-t}$, so $s\sim t$. Moreover
\[
\frac1t = \frac1s + \frac12 + O(s),\qquad\text{hence}\qquad e^{-1/t} = e^{-1/s}e^{-1/2}e^{O(s)}.
\]
Thus it is enough to study $F_a(x)e^{-1/s}$.

Now
\[
F_a(x) = \sum_{n\ge 1} n^a e^{2n}x^{n^2} = \sum_{n\ge 1} n^a e^{2n - s n^2} = e^{1/s}\sum_{n\ge 1} n^a e^{-s(n-1/s)^2,
\]
because $-sn^2+2n = -s(n-1/s)^2 + 1/s$. Hence
\[
F_a(x)e^{-1/s} =: S(s) = \sum_{n\ge 1} n^a e^{-s(n-1/s)^2.
\]

Set $u_n = \sqrt{s}\,(n-1/s)$. Then $n = \frac{1+u_n\sqrt{s}}{s}$ and $e^{-s(n-1/s)^2}=e^{-u_n^2}$, so
\[
S(s) = s^{-a}\sum_{n=1}^{\infty} (1+u_n\sqrt{s})^a e^{-u_n^2}.
\]
The points $u_n$ are equally spaced with step $\sqrt{s}$ and run from $u_1 = \sqrt{s}-1/\sqrt{s}$ to $+\infty$.  Write
\[
S(s) = s^{-a}\sum_{n=1}^{\infty} f_s(u_n),\qquad f_s(u) = (1+\sqrt{s}\,u)^a e^{-u^2}.
\]
Equivalently,
\[
s^{a+1/2}S(s) = \sum_{n=1}^{\infty} f_s(u_n)\sqrt{s} = \sum_{n=1}^{\infty} f_s(u_n)\Delta u,\quad \Delta u = \sqrt{s}.
\]

As $s\to0$, $\Delta u\to0$ and $\{u_n\}$ becomes dense in $\mathbb{R}$.  For any $\varepsilon>0$ we can find $M>0$ such that $\int_{|u|>M} e^{-u^2}\,du < \varepsilon$.  On $|u|\le M$ we have $f_s(u) = e^{-u^2}+O(\sqrt{s})$ uniformly.  The Riemann sum over $|u|\le M$ approximates $\int_{-M}^{M} e^{-u^2}\,du$ with error $O(\sqrt{s})$.  The tails $|u|>M$ contribute at most $O(\varepsilon)$ to both the sum and the integral.  Therefore
\[
\lim_{s\to0}\sum_{n=1}^{\infty} f_s(u_n)\Delta u = \int_{-\infty}^{\infty} e^{-u^2}\,du = \sqrt{\pi}.
\]
Consequently
\[
\lim_{s\to0} s^{a+1/2}S(s) = \sqrt{\pi}.
\]

Returning to $F_a(x)$,
\[
F_a(x)e^{-1/t} = e^{1/s-1/t}S(s) \sim e^{-1/2}\sqrt{\pi}\,s^{-a-1/2} \sim \sqrt{\pi}\,(1-x)^{-a-1/2}.
\]
Thus
\[
\lim_{x\to1^-} F_a(x)e^{-1/(1-x)} = 
\begin{cases}
0, & a < -\dfrac12,\\[8pt]
\infty, & a > -\dfrac12,
\end{cases}
\]
and the required constant is $-\dfrac12$. ∎
