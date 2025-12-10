# putnam_2024_A2

## Problem

For which real polynomials $p$ is there a real polynomial $q$ such that
$$p(p(x)) - x = (p(x) - x)^2 q(x)$$
for all real $x$?

## Submission

Let \(f(x)=p(x)-x\). Then  
\[
p(p(x)) = p(x+f(x)) = x+f(x) + f(x+f(x)),
\]  
so the given equation becomes  
\[
f(x) + f(x+f(x)) = f(x)^2 q(x). \tag{1}
\]

If \(f\equiv 0\) then \(p(x)=x\) and (1) holds for any \(q\); thus \(p(x)=x\) is a solution.

Assume \(f\not\equiv 0\). Expand \(f(x+f(x))\) using the Taylor formula (or the polynomial expansion)  
\[
f(x+f(x)) = f(x) + f'(x)f(x) + f(x)^2 R(x)
\]  
for some polynomial \(R(x)\). Substituting into (1) yields  
\[
f(x) + \bigl(f(x) + f'(x)f(x) + f(x)^2 R(x)\bigr) = f(x)^2 q(x)
\;\Longrightarrow\; 2f(x) + f'(x)f(x) + f(x)^2 R(x) = f(x)^2 q(x).
\]  
Factoring \(f(x)\) and cancelling it (the ring \(\mathbb R[x]\) has no zero divisors) gives  
\[
2 + f'(x) + f(x)R(x) = f(x) q(x)
\;\Longrightarrow\; f(x)\bigl(q(x)-R(x)\bigr) = 2 + f'(x).
\]  
Hence \(f(x)\) divides \(2+f'(x)\).

Now let \(d = \deg f\).

* \(d = 0\): \(f(x)=c\neq 0\) constant. Then \(f'(x)=0\) and \(2+f'(x)=2\). A non‑zero constant divides every polynomial (write \(2 = c\cdot\frac{2}{c}\)), so the condition holds. Hence \(p(x)=x+c\).

* \(d = 1\): write \(f(x)=ax+b\) with \(a\neq 0\). Then \(f'(x)=a\) and \(2+f'(x)=a+2\) is constant. A non‑constant polynomial can divide a constant only if that constant is zero, so \(a+2=0\), i.e. \(a=-2\). Then \(f(x)=-2x+b\) and \(2+f'(x)=0\) is trivially divisible by \(f\). Thus \(p(x)=x+(-2x+b)=-x+b\).

* \(d\ge 2\): \(\deg(2+f') = d-1\) (because \(f'\) has degree \(d-1\)). A polynomial of degree \(d\) cannot divide a non‑zero polynomial of lower degree, so we must have \(2+f'(x)\equiv 0\), which would force \(f'\) constant and \(f\) linear – impossible. Hence no solutions with \(\deg f\ge 2\).

Therefore the only possibilities are \(f\) constant or \(f(x)=-2x+b\). In terms of \(p\) we obtain  
\[
p(x)=x+a \quad\text{or}\quad p(x)=-x+a \qquad (a\in\mathbb R).
\]

Both families satisfy the original equation:  
- For \(p(x)=x+a\), \(p(p(x))-x=2a\) and \((p(x)-x)^2 = a^2\); taking \(q(x)=\frac{2}{a}\) (or any \(q\) when \(a=0\)) works.  
- For \(p(x)=-x+a\), \(p(p(x))-x=0\) and \((p(x)-x)^2 = (-2x+a)^2\); taking \(q(x)=0\) works.

Thus the required polynomials are exactly  

\[
\boxed{p(x)=x+a\ \text{ for some }a\in\mathbb R\quad\text{or}\quad p(x)=-x+a\ \text{ for some }a\in\mathbb R.}
\]
