# putnam_2024_B2

## Problem

Two convex quadrilaterals are called *partners* if they have three vertices in common and they can be labeled $ABCD$ and $ABCE$ so that $E$ is the reflection of $D$ across the perpendicular bisector of the diagonal $AC$. Is there an infinite sequence of convex quadrilaterals such that each quadrilateral is a partner of its successor and no two elements of the sequence are congruent?

## Submission

**Answer:** No, such an infinite sequence does not exist.

**Proof.**  
Assume, for contradiction, that there exists an infinite sequence \(Q_1, Q_2, Q_3, \dots\) of convex quadrilaterals with the property that each \(Q_i\) and \(Q_{i+1}\) are partners. We first prove two invariants that hold for any pair of partners.

---

### Invariant 1 – Side lengths
Let \(Q\) and \(Q'\) be partners. Then there exist labelings \(Q = ABCD\) and \(Q' = ABCE\) where \(E\) is the reflection of \(D\) across the perpendicular bisector of \(AC\).  
The sides of \(Q\) are \(AB, BC, CD, DA\); the sides of \(Q'\) are \(AB, BC, CE, EA\). Because reflection across the perpendicular bisector of \(AC\) swaps \(A\) and \(C\), we have \(CE = DA\) and \(EA = CD\). Hence the multisets  
\[
\{AB, BC, CD, DA\}\quad\text{and}\quad \{AB, BC, DA, CD\}
\]  
are identical. Thus the multiset of side lengths is unchanged by each move.

### Invariant 2 – Area
Again using the same labeling,  
\[
\operatorname{area}(Q) = \operatorname{area}(\triangle ABC) + \operatorname{area}(\triangle ADC),\qquad
\operatorname{area}(Q') = \operatorname{area}(\triangle ABC) + \operatorname{area}(\triangle AEC).
\]  
Place \(AC\) on the \(x\)-axis and its perpendicular bisector on the \(y\)-axis. Reflection across the \(y\)-axis changes the \(x\)-coordinate but leaves the \(y\)-coordinate unchanged, so the distances from \(D\) and \(E\) to the line \(AC\) are equal. Therefore \(\operatorname{area}(\triangle ADC) = \operatorname{area}(\triangle AEC)\). Consequently  
\[
\operatorname{area}(Q') = \operatorname{area}(Q).
\]  
Thus the area is also preserved throughout the sequence.

---

All quadrilaterals in the sequence therefore have the same multiset of side lengths and the same area \(K>0\).

---

### Finiteness for fixed side lengths and area
Let the common multiset be \(\{a,b,c,d\}\). Consider any convex quadrilateral with these side lengths. Up to congruence we may assume the sides appear in the cyclic order \((x,y,z,w)\), a permutation of \(a,b,c,d\). The quadrilateral is determined up to congruence by the length \(e = AC\) (or \(BD\)). The triangle inequalities give  
\[
|x-y| < e < x+y \quad\text{and}\quad |z-w| < e < z+w.
\]  
The area is  
\[
K = \Delta(x,y,e) + \Delta(z,w,e),\qquad 
\Delta(p,q,e) = \frac14\sqrt{(p+q+e)(-p+q+e)(p-q+e)(p+q-e)}.
\]  
Squaring twice to eliminate the radicals yields a polynomial equation in \(e^2\) of degree at most \(4\); hence for the given order there are at most \(4\) possible values of \(e\). Each admissible \(e\) determines the two triangles uniquely (up to congruence), and placing them on opposite sides of \(AC\) produces a quadrilateral (its mirror image is congruent). So at most \(4\) distinct quadrilaterals (up to congruence) exist for this order.

The number of distinct cyclic orders of four sides (mod rotation and reversal) is at most \(3\). Consequently the total number of convex quadrilaterals with side lengths \(\{a,b,c,d\}\) and area \(K\) is finite (at most \(12\)).

---

All members of the infinite sequence belong to this finite set, so by the pigeonhole principle two of them must be congruent – a contradiction. Hence no infinite sequence with the required properties exists. \(\square\)
