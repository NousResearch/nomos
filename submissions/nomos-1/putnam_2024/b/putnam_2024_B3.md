# putnam_2024_B3

## Problem

Let $r_n$ be the $n$th smallest positive solution to $\tan x = x$, where the argument of tangent is in radians. Prove that
$$0 < r_{n+1} - r_n - \pi < \frac{1}{(n^2 + n)\pi}$$
for $n \ge 1$.

## Submission

We prove the inequality by analyzing the location of the solutions and using a tangent subtraction formula.

**Proof.**  
For each integer \(k\ge 1\) consider \(f(x)=\tan x - x\) on the interval \((k\pi, k\pi+\pi/2)\).  On this interval \(\tan x\) is continuous and strictly increasing, \(f(k\pi)=-k\pi<0\) and \(\lim_{x\to (k\pi+\pi/2)^-}f(x)=+\infty\); therefore there exists a unique \(r_k\in(k\pi,k\pi+\pi/2)\) with \(f(r_k)=0\).  No positive solution lies elsewhere because \(\tan x<0\) on \((k\pi+\pi/2,(k+1)\pi)\).  Hence the positive solutions are \(r_1<r_2<\cdots\) with \(r_n\in(n\pi,n\pi+\pi/2)\) for all \(n\ge 1\).

Because \(\tan r_n=r_n\) and \(r_n-n\pi\in(0,\pi/2)\), we have  
\[
r_n-n\pi = \arctan r_n.
\]  
Set \(\delta_n=r_n-n\pi\); then \(\delta_n=\arctan r_n\).  Similarly \(\delta_{n+1}=r_{n+1}-(n+1)\pi=\arctan r_{n+1}\).

Now
\[
r_{n+1}-r_n = \bigl((n+1)\pi+\delta_{n+1}\bigr)-\bigl(n\pi+\delta_n\bigr)=\pi+(\delta_{n+1}-\delta_n).
\]  
Using the identity \(\arctan b-\arctan a = \arctan\frac{b-a}{1+ab}\) for \(a,b>0\) (the difference lies in \((0,\pi/2)\)), we obtain
\[
\delta_{n+1}-\delta_n = \arctan r_{n+1}-\arctan r_n = \arctan\frac{r_{n+1}-r_n}{1+r_nr_{n+1}}.
\]  
Let \(d=r_{n+1}-r_n>0\).  Then
\[
d = \pi + \arctan\frac{d}{1+r_nr_{n+1}}. \tag{1}
\]  
Since \(\arctan t < t\) for every \(t>0\), (1) gives
\[
d < \pi + \frac{d}{1+r_nr_{n+1}}. \tag{2}
\]  
Rearranging (2) yields
\[
d\left(1-\frac{1}{1+r_nr_{n+1}\right) < \pi \;\Longrightarrow\; d\cdot\frac{r_nr_{n+1}}{1+r_nr_{n+1}} < \pi \;\Longrightarrow\; d < \pi\,\frac{1+r_nr_{n+1}}{r_nr_{n+1}} = \pi + \frac{\pi}{r_nr_{n+1}}. \tag{3}
\]  
Thus
\[
d-\pi < \frac{\pi}{r_nr_{n+1}}. \tag{4}
\]  
From \(r_n>n\pi\) and \(r_{n+1}>(n+1)\pi\) we have \(r_nr_{n+1}>n(n+1)\pi^2\), so
\[
\frac{\pi}{r_nr_{n+1}} < \frac{1}{n(n+1)\pi}. \tag{5}
\]  
Combining (4) and (5) gives
\[
0 < r_{n+1}-r_n-\pi < \frac{1}{(n^2+n)\pi},
\]  
which completes the proof. ∎
