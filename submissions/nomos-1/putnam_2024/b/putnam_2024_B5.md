# putnam_2024_B5

## Problem

Let $k$ and $m$ be positive integers. For a positive integer $n$, let $f(n)$ be the number of integer sequences $x_1, \ldots, x_k, y_1, \ldots, y_m, z$ satisfying $1 \le x_1 \le \cdots \le x_k \le z \le n$ and $1 \le y_1 \le \cdots \le y_m \le z \le n$. Show that $f(n)$ can be expressed as a polynomial in $n$ with nonnegative coefficients.

## Submission

For a fixed integer \(z\) with \(1\le z\le n\), the number of sequences \(1\le x_1\le\cdots\le x_k\le z\) is the number of multisets of size \(k\) from \(\{1,\dots ,z\}\); this is \(\binom{z+k-1}{k}\). The same holds for the \(y\)’s. Hence  

\[
f(n)=\sum_{z=1}^{n}\binom{z+k-1}{k}\binom{z+m-1}{m}. \tag{1}
\]

---

### 1.  Vandermonde expansion  

The Vandermonde identity gives \(\displaystyle\binom{a+b}{a}=\sum_{i=0}^{a}\binom{a}{i}\binom{b}{a-i}\).  
With \(a=z,\;b=k-1\) we obtain  

\[
\binom{z+k-1}{k}=\sum_{i=0}^{k}\binom{z}{i}\binom{k-1}{k-i}.
\]

Because \(k\ge 1\), the term \(i=0\) contributes \(\binom{k-1}{k}=0\); therefore we may restrict the sum to \(i=1,\dots ,k\):

\[
\binom{z+k-1}{k}=\sum_{i=1}^{k}\binom{z}{i}\binom{k-1}{k-i}. \tag{2}
\]

Similarly  

\[
\binom{z+m-1}{m}=\sum_{j=1}^{m}\binom{z}{j}\binom{m-1}{m-j}. \tag{3}
\]

Substituting (2) and (3) into (1) yields  

\[
f(n)=\sum_{z=1}^{n}\sum_{i=1}^{k}\sum_{j=1}^{m}\binom{z}{i}\binom{k-1}{k-i}\binom{z}{j}\binom{m-1}{m-j}
      =\sum_{i=1}^{k}\sum_{j=1}^{m}\binom{k-1}{k-i}\binom{m-1}{m-j}\sum_{z=1}^{n}\binom{z}{i}\binom{z}{j}. \tag{4}
\]

---

### 2.  Falling factorials  

For a non‑negative integer \(a\) we write the falling factorial \((z)_a=z(z-1)\cdots(z-a+1)\) (with \((z)_0=1\)).  
Then \(\displaystyle\binom{z}{a}=\frac{(z)_a}{a!}\). Consequently  

\[
\sum_{z=1}^{n}\binom{z}{i}\binom{z}{j}
   =\frac{1}{i!\,j!}\sum_{z=1}^{n}(z)_i(z)_j. \tag{5}
\]

---

### 3.  Product of falling factorials  

**Lemma 1.**  For any non‑negative integers \(i,j\) and variable \(t\),

\[
(t)_i(t)_j=\sum_{r=0}^{\min(i,j)}\binom{i}{r}\binom{j}{r}\,r!\,(t)_{i+j-r}. \tag{6}
\]

*Proof.*  Both sides are polynomials in \(t\); it suffices to verify the equality for all integers \(t\ge 0\).  
Count ordered pairs \((f,g)\) where \(f:[i]\to[t]\) and \(g:[j]\to[t]\) are injective.  
The left‑hand side is exactly the number of such pairs.

Fix \(r=|f([i])\cap g([j])|\).  To construct a pair with this intersection size:

* choose the union \(U=f([i])\cup g([j])\) of size \(i+j-r\): \(\binom{t}{i+j-r}\) ways;
* choose the intersection \(I\subseteq U\) of size \(r\): \(\binom{i+j-r}{r}\) ways;
* from the remaining \(i+j-2r\) elements pick the set \(A=f([i])\setminus g([j])\) of size \(i-r\): \(\binom{i+j-2r}{i-r}\) ways;
* assign \(f\): the \(i\) elements of \(f([i])=I\cup A\) must be matched with the \(i\) elements of \([i]\); there are \(i!\) bijections;
* assign \(g\): similarly \(j!\) bijections.

Hence the number of pairs with intersection size \(r\) is  

\[
\binom{t}{i+j-r}\,\binom{i+j-r}{r}\,\binom{i+j-2r}{i-r}\,i!\,j!
   =\binom{t}{i+j-r}\,\frac{(i+j-r)!}{r!\,(i-r)!\,(j-r)!}\,i!\,j!.
\]

Because \(\displaystyle\binom{t}{i+j-r}=\frac{(t)_{i+j-r}}{(i+j-r)!}\), this simplifies to  

\[
\frac{(t)_{i+j-r}\,i!\,j!}{r!\,(i-r)!\,(j-r)!}
   =\binom{i}{r}\binom{j}{r}\,r!\,(t)_{i+j-r}.
\]

Summing over \(r\) gives (6). ∎

---

### 4.  Summation of falling factorials  

**Lemma 2.**  For any non‑negative integer \(s\),

\[
\sum_{z=0}^{n}(z)_s = s!\,\binom{n+1}{s+1}. \tag{7}
\]

*Proof.*  Observe that  

\[
(z+1)_{s+1}-(z)_{s+1}=(z)_{s}\big((z+1)-(z-s)\big)=(s+1)(z)_s,
\]

so \((z)_s=\frac{(z+1)_{s+1}-(z)_{s+1}}{s+1}\).  Summing from \(z=0\) to \(n\) telescopes:

\[
\sum_{z=0}^{n}(z)_s=\frac{(n+1)_{s+1}-0_{s+1}}{s+1}
   =\frac{(s+1)!\,\binom{n+1}{s+1}}{s+1}=s!\,\binom{n+1}{s+1}. \quad\square
\]

---

### 5.  Putting everything together  

Apply Lemma 1 to \((z)_i(z)_j\).  Since \((0)_i=0\) for \(i>0\), we may start the sum at \(z=0\):

\[
\sum_{z=1}^{n}(z)_i(z)_j
   =\sum_{z=0}^{n}(z)_i(z)_j
   =\sum_{r=0}^{\min(i,j)}\binom{i}{r}\binom{j}{r}\,r!\sum_{z=0}^{n}(z)_{i+j-r}.
\]

By Lemma 2, \(\displaystyle\sum_{z=0}^{n}(z)_{i+j-r}=(i+j-r)!\,\binom{n+1}{i+j-r+1}\).  Hence  

\[
\sum_{z=1}^{n}(z)_i(z)_j
   =\sum_{r=0}^{\min(i,j)}\binom{i}{r}\binom{j}{r}\,r!\,(i+j-r)!\,\binom{n+1}{i+j-r+1}. \tag{8}
\]

Insert (8) into (5) and then into (4):

\[
f(n)=\sum_{i=1}^{k}\sum_{j=1}^{m}\binom{k-1}{k-i}\binom{m-1}{m-j}\,
        \frac{1}{i!\,j!}\sum_{r=0}^{\min(i,j)}\binom{i}{r}\binom{j}{r}\,r!\,(i+j-r)!\,\binom{n+1}{i+j-r+1}.
\]

Simplify the coefficient:

\[
\frac{1}{i!\,j!}\,\binom{i}{r}\binom{j}{r}\,r!\,(i+j-r)!
   =\frac{(i+j-r)!}{(i-r)!\,(j-r)!\,r!}\;\binom{k-1}{k-i}\binom{m-1}{m-j}.
\]

Thus  

\[
f(n)=\sum_{i=1}^{k}\sum_{j=1}^{m}\sum_{r=0}^{\min(i,j)}
        \underbrace{\binom{k-1}{k-i}\binom{m-1}{m-j}\,\frac{(i+j-r)!}{(i-r)!\,(j-r)!\,r!}}_{=:c_{i,j,r}\;
        \binom{n+1}{i+j-r+1}. \tag{9}
\]

---

### 6.  Non‑negativity  

For each triple \((i,j,r)\) the factor \(c_{i,j,r}\) is a product of binomial coefficients and a multinomial coefficient, therefore a non‑negative integer.  
The binomial coefficient \(\displaystyle\binom{n+1}{s}\) expands as  

\[
\binom{n+1}{s}=\frac{(n+1)(n+2)\cdots(n+s)}{s!},
\]

a polynomial in \(n\) with **positive** coefficients.  Consequently \(f(n)\) is a finite sum of polynomials with non‑negative coefficients, and hence itself a polynomial with non‑negative coefficients. ∎
