# putnam_2024_A4

## Problem

Find all primes $p > 5$ for which there exists an integer $a$ and an integer $r$ satisfying $1 \le r \le p-1$ with the following property: the sequence $1, a, a^2, \ldots, a^{p-5}$ can be rearranged to form a sequence $b_0, b_1, b_2, \ldots, b_{p-5}$ such that $b_n - b_{n-1} - r$ is divisible by $p$ for $1 \le n \le p-5$.

## Submission

Let $p>5$ be a prime and suppose there exist integers $a$ and $r$ with $1\le r\le p-1$ such that the multiset $\{1,a,a^2,\dots,a^{p-5\}$ can be rearranged to $b_0,b_1,\dots,b_{p-5}$ satisfying $b_n\equiv b_{n-1}+r\pmod p$ for $n=1,\dots,p-5$. Then $b_n\equiv b_0+nr\pmod p$, so the set $S=\{a^k\pmod p\mid 0\le k\le p-5\}$ is exactly $\{b_0+nr\mid n=0,\dots,p-5\}$, a set of $p-4$ distinct residues (since $r\not\equiv0\pmod p$). In particular $a\not\equiv0\pmod p$ and the $p-4$ powers are distinct; let $d$ be the order of $a$ modulo $p$. Then $d\ge p-4$ and $d\mid p-1$. For $p\ge11$, we have $p-4>\frac{p-1}{2}$, so the only divisor of $p-1$ at least $p-4$ is $p-1$, hence $d=p-1$ and $a$ is a primitive root. For $p=7$ we treat separately.

Because $r$ is invertible modulo $p$, the set $r^{-1}S$ is an arithmetic progression with difference $1$, i.e. $r^{-1}S=\{t,t+1,\dots,t+p-5\}$ for some $t\in\mathbb Z$. Hence $S$ itself is an interval of length $p-4$ in the cyclic group $\mathbb Z/p\mathbb Z$. Its complement consists of $4$ residues, and since $0\notin S$ (all elements of $S$ are nonzero), $0$ belongs to the complement. The complement is therefore an interval of length $4$ containing $0$; the only such intervals are
\[
\{0,1,2,3\},\quad \{p-1,0,1,2\},\quad \{p-2,p-1,0,1\},\quad \{p-3,p-2,p-1,0\}.
\]

Now $S$ is exactly $\{a^k\mid 0\le k\le p-5\}$, so the complement is $\{0,a^{p-4},a^{p-3},a^{p-2}\}$. We claim that $a^{p-4},a^{p-3},a^{p-2}\not\equiv1\pmod p$. Indeed, if $a^{p-4}\equiv1$ then $d\mid p-4$. For $p\ge7$, $d\ge p-4$ and $d\mid p-1$; the only possibility would be $d=p-1$ and $p-1\mid p-4$, impossible. For $p=7$ we check later. Thus the first three intervals, which contain $1$, cannot be the complement. Consequently we must have
\[
\{a^{p-4},a^{p-3},a^{p-2}\} = \{p-3,p-2,p-1\}\pmod p. \tag{1}
\]

Using $a^{p-2}\equiv a^{-1},\;a^{p-3}\equiv a^{-2},\;a^{p-4}\equiv a^{-3}$ (since $a^{p-1}\equiv1$), set $b\equiv a^{-1}\pmod p$. Then $b$ is also a primitive root (for $p\ge11$; for $p=7$ we will see it is). Equation (1) becomes
\[
\{b,b^2,b^3\} = \{-1,-2,-3\}\pmod p. \tag{2}
\]

Now $b$ belongs to this set, so we examine the three possibilities.

- $b\equiv -1$: then $b^2\equiv1$, $b^3\equiv-1$, giving $\{ -1,1,-1\}$, not three distinct numbers.
- $b\equiv -2$: then $b^2\equiv4$, $b^3\equiv-8$. We need $\{4,-8\}=\{-1,-3\}$. This forces $4\equiv-1$ or $4\equiv-3$. The first gives $p\mid5$, the second $p\mid7$. $p=5$ is excluded, $p=7$ works. Indeed for $p=7$, $b\equiv5$ is primitive and $5,5^2=4,5^3=6$ are $-2,-3,-1$.
- $b\equiv -3$: then $b^2\equiv9$, $b^3\equiv-27$. We need $\{9,-27\}=\{-1,-2\}$. The equations $9\equiv-1$ or $9\equiv-2$ give $p=5$ or $p=11$; for $p=11$, $-27\equiv6\not\equiv-1$, so only $p=5$ appears.

Thus the only prime $>5$ that satisfies (2) is $p=7$.

For $p=7$, take $a=3$ (a primitive root) and $r=1$. Then $1,3,3^2\equiv2$ can be ordered as $1,2,3$, and $2-1=1$, $3-2=1$, both $\equiv1\pmod7$. Hence $p=7$ works.

Therefore the only prime $p>5$ with the required property is $\boxed{p=7}$.
