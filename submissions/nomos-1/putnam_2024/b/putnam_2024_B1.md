# putnam_2024_B1

## Problem

Let $n$ and $k$ be positive integers. The square in the $i$th row and $j$th column of an $n$-by-$n$ grid contains the number $i + j - k$. For which $n$ and $k$ is it possible to select $n$ squares from the grid, no two in the same row or column, such that the numbers contained in the selected squares are exactly $1, 2, \ldots, n$?

## Submission

**Answer:** The selection is possible if and only if \(n\) is odd and \(k = \frac{n+1}{2}\).

**Proof.**  
Let the selected squares be \((i, \sigma(i))\) for \(i=1,\ldots,n\), where \(\sigma\) is a permutation of \(\{1,\ldots,n\}\). The numbers are \(i+\sigma(i)-k\). Their sum is
\[
\sum_{i=1}^n (i+\sigma(i)-k) = \sum_{i=1}^n i + \sum_{i=1}^n \sigma(i) - nk = n(n+1) - nk.
\]
Since the numbers must be exactly \(1,2,\ldots,n\), their sum is \(\frac{n(n+1)}{2}\). Hence
\[
n(n+1) - nk = \frac{n(n+1)}{2} \quad\Longrightarrow\quad n+1 - k = \frac{n+1}{2} \quad\Longrightarrow\quad k = \frac{n+1}{2}.
\]
Thus \(n+1\) must be even, i.e., \(n\) odd, and \(k\) is forced to be \((n+1)/2\).

Conversely, suppose \(n\) is odd and write \(n=2m-1\) (so \(m = \frac{n+1}{2}\)). Define \(\sigma\) by
\[
\sigma(i) = \begin{cases}
i+m & \text{if } 1 \le i \le m-1,\\
i-m+1 & \text{if } m \le i \le 2m-1.
\end{cases}
\]
One checks that \(\sigma\) is a permutation of \(\{1,\ldots,n\}\). Then
\[
i+\sigma(i)-k = 
\begin{cases}
i+(i+m)-m = 2i & \text{for } 1\le i\le m-1,\\
i+(i-m+1)-m = 2i-2m+1 & \text{for } m\le i\le 2m-1.
\end{cases}
\]
As \(i\) runs from \(1\) to \(m-1\), \(2i\) runs over the even numbers \(2,4,\ldots,2m-2\); as \(i\) runs from \(m\) to \(2m-1\), \(2i-2m+1\) runs over the odd numbers \(1,3,\ldots,2m-1\). Hence the selected numbers are precisely \(1,2,\ldots,n\). ∎
