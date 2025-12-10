# putnam_2024_B2

## Problem

Two convex quadrilaterals are called *partners* if they have three vertices in common and they can be labeled $ABCD$ and $ABCE$ so that $E$ is the reflection of $D$ across the perpendicular bisector of the diagonal $AC$. Is there an infinite sequence of convex quadrilaterals such that each quadrilateral is a partner of its successor and no two elements of the sequence are congruent?

## Submission

To determine whether there exists an infinite sequence of **convex quadrilaterals** such that:

1. Each quadrilateral is a *partner* of its successor (i.e., they share three vertices and the fourth vertex of one is the reflection of the other across the perpendicular bisector of the diagonal connecting the shared common pair), and  
2. No two elements in the sequence are congruent,

we must carefully analyze the geometric implications of the "partner" definition.

---

### Understanding the Partner Relation

Two convex quadrilaterals are **partners** if:
- They share **three vertices**, say $ A, B, C $,
- The fourth vertex of the first quadrilateral is $ D $, and the fourth vertex of the second is $ E $,
- $ E $ is the **reflection of $ D $** across the **perpendicular bisector of diagonal $ AC $**.

This implies that the **diagonal $ AC $** is fixed for both quadrilaterals, and the **third common vertex $ B $** lies on the perpendicular bisector of $ AC $. This ensures that the reflection over this line maps the set $ \{A, B, C, D\} $ to $ \{A, B, C, E\} $, preserving the three shared vertices.

Since the reflection is an **isometry**, it preserves all distances and angles. Therefore, the two quadrilaterals are **congruent** under this transformation.

---

### Key Implication

Because the transformation used to define a partner is an **isometry**, **every pair of partners is congruent**. That is, for any quadrilateral $ Q_n $, the quadrilateral $ Q_{n+1} $ formed by reflecting the fourth vertex across the perpendicular bisector of a chosen diagonal (with the third vertex on that bisector) will be **congruent** to $ Q_n $.

Thus, **any sequence of such quadrilaterals must consist of congruent quadrilaterals**. If we attempt to construct an infinite sequence where each quadrilateral is a partner of the next, then **all quadrilaterals in the sequence must be congruent**.

Hence, it is **impossible** to have an infinite sequence of convex quadrilaterals where **no two are congruent**, because every step in the sequence produces a quadrilateral **congruent** to the previous one.

---

### Conclusion

The requirement that no two elements in the sequence are congruent is **incompatible** with the definition of "partners", which inherently leads to congruence through isometric transformations.

Therefore, the answer is:

$$
\boxed{\text{No}}
$$
