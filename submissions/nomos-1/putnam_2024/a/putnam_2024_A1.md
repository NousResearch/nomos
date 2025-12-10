# putnam_2024_A1

## Problem

Determine all positive integers $n$ for which there exist positive integers $a$, $b$, and $c$ satisfying
$$2a^n + 3b^n = 4c^n.$$

## Submission

The only positive integer \(n\) for which the equation has positive integer solutions is \(n=1\).

**Proof.**  
For \(n=1\) the triple \((a,b,c)=(1,2,2)\) gives \(2\cdot1+3\cdot2=8=4\cdot2\), so \(n=1\) works.

Now suppose \(n\ge2\) and that positive integers \(a,b,c\) satisfy \(2a^n+3b^n=4c^n\).

**Case \(n=2\).**  
Then \(2a^2+3b^2=4c^2\). Modulo \(4\) we have \(a^2\equiv0\) or \(1\), hence \(2a^2\equiv0\) or \(2\); similarly \(3b^2\equiv0\) or \(3\). The right‑hand side is \(0\pmod4\), so we must have \(2a^2\equiv0\) and \(3b^2\equiv0\), i.e. \(a\) and \(b\) even. Write \(a=2x,\;b=2y\). Substituting yields  
\[
8x^2+12y^2=4c^2\quad\Longrightarrow\quad 2x^2+3y^2=c^2.\tag{1}
\]  
Modulo \(3\), (1) gives \(2x^2\equiv c^2\pmod3\). Since squares modulo \(3\) are \(0\) or \(1\), this forces \(x\equiv0\pmod3\) and \(c\equiv0\pmod3\). Write \(x=3x_1\), \(c=3c_1\). Then  
\[
18x_1^2+3y^2=9c_1^2\quad\Longrightarrow\quad 6x_1^2+y^2=3c_1^2\quad\Longrightarrow\quad y^2=3(c_1^2-2x_1^2),
\]  
so \(3\mid y\); write \(y=3y_1\). Substituting back gives \(9y_1^2=3(c_1^2-2x_1^2)\), i.e. \(c_1^2=2x_1^2+3y_1^2\). Thus \((x_1,y_1,c_1)\) is another positive solution of (1) with \(x_1<x,\;y_1<y,\;c_1<c\). By infinite descent, (1) has no positive integer solutions, contradiction. Hence \(n=2\) is impossible.

**Case \(n\ge3\).**  
Again modulo \(4\) forces \(a\) and \(b\) even (the same reasoning as above). Put \(a=2x,\;b=2y\). Then  
\[
2\cdot(2x)^n+3\cdot(2y)^n=2^n(2x^n+3y^n)=4c^n.
\]  
Because \(n\ge3\), we may divide by \(4\) to obtain  
\[
2^{n-2}(2x^n+3y^n)=c^n.
\]  
Hence \(c^n\) is even, so \(c\) is even; write \(c=2z\). Substituting gives  
\[
2^{n-2}(2x^n+3y^n)=2^n z^n\quad\Longrightarrow\quad 2x^n+3y^n=4z^n.
\]  
Thus \((x,y,z)\) is a positive integer solution of the original equation with \(x<a,\;y<b,\;z<c\). Repeating this argument produces an infinite strictly decreasing sequence of positive integers, which is impossible. Therefore no solution exists for \(n\ge3\).

The two cases cover all \(n\ge2\); consequently the only admissible value is \(n=1\).

\[
\boxed{n=1}
\]
