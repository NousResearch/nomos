# putnam_2024_B4

## Problem

Let $n$ be a positive integer. Set $a_{n,0} = 1$. For $k \ge 0$, choose an integer $m_{n,k}$ uniformly at random from the set $\{1,\ldots,n\}$, and let
$$a_{n,k+1} = \begin{cases}
a_{n,k} + 1, & \text{if } m_{n,k} > a_{n,k}; \\
a_{n,k}, & \text{if } m_{n,k} = a_{n,k}; \\
a_{n,k} - 1, & \text{if } m_{n,k} < a_{n,k}.
\end{cases}$$
Let $E(n)$ be the expected value of $a_{n,n}$. Determine $\lim_{n \to \infty} E(n)/n$.

## Submission

The limit is \(\displaystyle \frac{1-e^{-2}}{2}\).

**Proof.**  
Let \(E_k = \mathbb{E}[a_{n,k}]\).  Given \(a_{n,k}\), the next value satisfies  
\[
\mathbb{E}[a_{n,k+1} \mid a_{n,k}] = a_{n,k} + \frac{n-2a_{n,k}+1}{n} = \left(1-\frac{2}{n}\right)a_{n,k} + \frac{n+1}{n}.
\]  
Taking expectations gives the linear recurrence  
\[
E_{k+1} = \left(1-\frac{2}{n}\right)E_k + \frac{n+1}{n},\qquad E_0 = 1.
\]  
Solving yields  
\[
E_k = \left(1-\frac{2}{n}\right)^{\!k} + \frac{n+1}{n}\cdot\frac{1-\left(1-\frac{2}{n}\right)^{\!k}}{2/n}
      = \frac{n+1}{2} - \frac{n-1}{2}\left(1-\frac{2}{n}\right)^{\!k}.
\]  
In particular, for \(k=n\),  
\[
E(n) = \frac{n+1}{2} - \frac{n-1}{2}\left(1-\frac{2}{n}\right)^{\!n}.
\]  
Dividing by \(n\) and letting \(n\to\infty\),  
\[
\frac{E(n)}{n} = \frac{n+1}{2n} - \frac{n-1}{2n}\left(1-\frac{2}{n}\right)^{\!n}
          \;\longrightarrow\; \frac12 - \frac12 e^{-2} = \frac{1-e^{-2}}{2},
\]  
since \(\displaystyle \lim_{n\to\infty}\left(1-\frac{2}{n}\right)^{\!n}=e^{-2}\). ∎
