# putnam_2024_A3

## Problem

Let $S$ be the set of bijections
$$T : \{1,2,3\} \times \{1,2,\ldots,2024\} \to \{1,2,\ldots,6072\}$$
such that $T(1,j) < T(2,j) < T(3,j)$ for all $j \in \{1,2,\ldots,2024\}$ and $T(i,j) < T(i,j+1)$ for all $i \in \{1,2,3\}$ and $j \in \{1,2,\ldots,2023\}$. Do there exist $a$ and $c$ in $\{1,2,3\}$ and $b$ and $d$ in $\{1,2,\ldots,2024\}$ such that the fraction of elements $T$ in $S$ for which $T(a,b) < T(c,d)$ is at least $1/3$ and at most $2/3$?

## Submission

Yes, for example $a=1$, $b=2024$, $c=3$, $d=1$.

*Proof.*  
Let $N=6072$. For any $T\in S$ define a new map $T'$ by  
\[
T'(i,j)=N+1-T(4-i,\,2025-j)\qquad\text{for all }(i,j)\in\{1,2,3\}\times\{1,\dots,2024\}.
\]  
The transformation $(i,j)\mapsto(4-i,2025-j)$ is a bijection on the set of cells, so $T'$ is a bijection from the cells to $\{1,\dots,N\}$.  

We check that $T'$ satisfies the required monotonicity conditions:  

- For any $i$ and $j<2024$, we have $2025-j>2025-(j+1)$. Since the row $4-i$ of $T$ is strictly increasing,  
  $T(4-i,2025-j)>T(4-i,2025-(j+1))$, hence  
  $T'(i,j)=N+1-T(4-i,2025-j)<N+1-T(4-i,2025-(j+1))=T'(i,j+1)$.  

- For any $j$ and $i<3$, we have $4-i>4-(i+1)$. The column $2025-j$ of $T$ is strictly increasing, so  
  $T(4-i,2025-j)>T(4-(i+1),2025-j)$, giving  
  $T'(i,j)=N+1-T(4-i,2025-j)<N+1-T(4-(i+1),2025-j)=T'(i+1,j)$.  

- The inequalities $T'(1,j)<T'(2,j)<T'(3,j)$ follow similarly from the column condition of $T$:  
  $T(3,2025-j)>T(2,2025-j)>T(1,2025-j)$ implies $T'(1,j)<T'(2,j)<T'(3,j)$.

Thus $T'\in S$. Clearly $(T')'=T$, so the map $T\mapsto T'$ is an involution and therefore a bijection of $S$ onto itself.

Now compute  
\[
T'(1,2024)=N+1-T(3,1),\qquad T'(3,1)=N+1-T(1,2024).
\]  
Consequently,  
\[
T(1,2024)<T(3,1)\;\Longleftrightarrow\;T'(1,2024)>T'(3,1).
\]  
The involution pairs each tableau with one for which the opposite strict inequality holds, and no tableau can satisfy both. Hence the two sets  
$\{T\in S:T(1,2024)<T(3,1)\}$ and $\{T\in S:T(1,2024)>T(3,1)\}$ have equal cardinalities. Because $T(1,2024)\neq T(3,1)$ for every $T$, they partition $S$, so each contains exactly $|S|/2$ elements.  

Therefore the fraction of $T\in S$ with $T(1,2024)<T(3,1)$ is $\frac12$, which lies between $\frac13$ and $\frac23$. ∎
