# putnam_2024_A6

## Problem

Let $c_0, c_1, c_2, \ldots$ be the sequence defined so that
$$\frac{1 - 3x - \sqrt{1 - 14x + 9x^2}}{4} = \sum_{k=0}^{\infty} c_k x^k$$
for sufficiently small $x$. For a positive integer $n$, let $A$ be the $n$-by-$n$ matrix with $i,j$-entry $c_{i+j-1}$ for $i$ and $j$ in $\{1,\ldots,n\}$. Find the determinant of $A$.

## Submission

Let \(c_0,c_1,c_2,\dots\) be defined by

\[
\frac{1-3x-\sqrt{1-14x+9x^2}{4}=\sum_{k=0}^{\infty}c_kx^k\qquad\text{for small }x.
\]

In particular \(c_0=0,\;c_1=1,\;c_2=5,\;c_3=35,\;c_4=295,\;c_5=2765,\dots\).  For a positive integer \(n\) define the \(n\times n\) matrix \(A\) by \(A_{ij}=c_{i+j-1}\;(1\le i,j\le n)\).  We shall prove that

\[
\det A = 10^{\frac{n(n-1)}{2}.
\]

---

### 1. Shifting the sequence

Set \(a_k=c_{k+1}\;(k\ge 0)\).  Then \(a_0=1,\;a_1=5,\;a_2=35,\;a_3=295,\;a_4=2765,\dots\) and

\[
A = \bigl(a_{i+j}\bigr)_{0\le i,j\le n-1}.
\]

The generating function of \((a_k)\) is

\[
a(x):=\sum_{k=0}^{\infty}a_kx^k=\frac{1-3x-\sqrt{1-14x+9x^2}{4x}.
\]

Squaring the identity \(4x\,a(x)=1-3x-\sqrt{1-14x+9x^2\) gives after simplification

\[
2x\,a(x)^2+(3x-1)a(x)+1=0. \tag{1}
\]

---

### 2. Stieltjes transform

Define the Stieltjes transform

\[
F(z)=\sum_{k=0}^{\infty}\frac{a_k}{z^{k+1}= \frac{a(1/z)}{z}= \frac{z-3-\sqrt{z^2-14z+9}{4z}\qquad (|z|\text{ large}). \tag{2}
\]

---

### 3. Continued fraction expansion

Consider the infinite continued fraction

\[
F(z)=\cfrac{1}{z-5-\cfrac{10}{z-7-\cfrac{10}{z-7-\cfrac{10}{z-7-\cdots}}.
\]

Let \(G(z)\) denote the tail after the first step, i.e.

\[
G(z)=\cfrac{1}{z-7-\cfrac{10}{z-7-\cfrac{10}{z-7-\cdots}}.
\]

Then \(G(z)\) satisfies \(G(z)=\dfrac{1}{z-7-10\,G(z)}\), i.e.

\[
10\,G(z)^2+(7-z)G(z)+1=0\quad\Longrightarrow\quad G(z)=\frac{z-7-\sqrt{z^2-14z+9}{20}
\]

(the branch that tends to \(0\) as \(z\to\infty\)).  Substituting,

\[
\frac{1}{z-5-10\,G(z)}=\frac{1}{z-5-\frac{z-7-\sqrt{z^2-14z+9}{2}}
=\frac{2}{2z-10-(z-7-\sqrt{z^2-14z+9)}=\frac{z-3-\sqrt{z^2-14z+9}{4z}=F(z).
\]

Hence the continued fraction with \(a_0=5,\;a_n=7\;(n\ge 1),\;b_1=10,\;b_n=10\;(n\ge 2)\) indeed equals \(F(z)\).  By the uniqueness of the expansion (Jacobi’s algorithm) this is the continued fraction that corresponds to the moment sequence \((a_k)\).

---

### 4. Orthogonal polynomials

The continued fraction above yields the three‑term recurrence for the *monic* orthogonal polynomials \(P_n(x)\) (with respect to the measure having moments \(a_k\)):

\[
P_0(x)=1,\qquad P_1(x)=x-5,\qquad 
P_{n+1}(x)=(x-7)P_n(x)-10\,P_{n-1}(x)\quad(n\ge 1). \tag{3}
\]

---

### 5. Norms of the orthogonal polynomials

Let \(h_n=\int P_n(x)^2\,d\mu\) (the measure \(\mu\) is the one with moments \(a_k\)).  From (3) one obtains

\[
h_0=a_0=1,\qquad h_1=\int (x-5)^2\,d\mu = a_2-2\cdot5\,a_1+25=35-50+25=10.
\]

For \(n\ge 1\) the coefficient \(10\) in (3) is exactly \(h_n/h_{n-1}\); therefore

\[
h_n=10\,h_{n-1}\qquad (n\ge 1).
\]

Consequently \(h_n=10^n\) for all \(n\ge0\).

(One can also verify \(h_2=100\) directly: \(P_2(x)=x^2-12x+25\) and
\(h_2=a_4-24a_3+194a_2-600a_1+625=100\), and the pattern continues.)

---

### 6. Hankel determinant

For a positive definite moment sequence the Hankel determinant

\[
H_n=\det\bigl(a_{i+j}\bigr)_{0\le i,j\le n-1}
\]

factorises as

\[
H_n=\prod_{k=0}^{n-1}h_k .
\]

Thus

\[
H_n=\prod_{k=0}^{n-1}10^{\,k}=10^{0+1+\cdots+(n-1}=10^{\frac{n(n-1)}{2}.
\]

Because \(A\) is exactly this matrix, \(\det A=H_n\).

---

\[
\boxed{10^{\frac{n(n-1)}{2}}
\]
