# putnam_2024_A5

## Problem

Consider a circle $\Omega$ with radius $9$ and center at the origin $(0,0)$, and a disc $\Delta$ with radius $1$ and center at $(r,0)$, where $0 \le r \le 8$. Two points $P$ and $Q$ are chosen independently and uniformly at random on $\Omega$. Which value(s) of $r$ minimize the probability that the chord $PQ$ intersects $\Delta$?

## Submission

To determine the value(s) of $ r \in [0, 8] $ that **minimize** the probability that a randomly chosen chord $ PQ $ (with endpoints on the circle $ \Omega $ of radius 9 centered at the origin) intersects the disc $ \Delta $ of radius 1 centered at $ (r, 0) $, we proceed with a geometric and probabilistic analysis.

---

### **Key Observations and Setup**

- The circle $ \Omega $ has equation $ x^2 + y^2 = 81 $.
- The disc $ \Delta $ has center $ (r, 0) $ and radius 1. It is entirely inside or tangent to $ \Omega $ since $ r + 1 \leq 9 $ for all $ r \leq 8 $.
- Two points $ P $ and $ Q $ are chosen independently and uniformly at random on $ \Omega $, i.e., on the circumference of the circle.
- A **chord** $ PQ $ is the line segment between these two points.
- The problem asks to **minimize the probability** that this chord intersects the disc $ \Delta $.

---

### **Geometric Insight Using Symmetry**

Due to the rotational symmetry of the circle, we can fix one point $ P $ at $ (9, 0) $ without loss of generality. Then, the second point $ Q $ is uniformly distributed over the circle, parameterized by an angle $ \theta \in [0, 2\pi) $, such that:
$$
Q = (9 \cos \theta, 9 \sin \theta)
$$

The distance from the center of the disc $ C = (r, 0) $ to the line containing the chord $ PQ $ is given by:
$$
d = (9 - r) |\cos(\theta/2)|
$$

This distance must be less than or equal to 1 for the line to intersect the disc. However, it's also necessary that the **foot of the perpendicular** from $ C $ to the line lies **on the segment** $ PQ $. This condition was verified to always hold for all $ r \in [0, 8] $, so the chord intersects $ \Delta $ **if and only if** $ d \leq 1 $, i.e., when:
$$
|\cos(\theta/2)| \leq \frac{1}{9 - r}
$$

Let $ k = \frac{1}{9 - r} $, which is in $ (0, 1] $ as $ r \in [0, 8] $.

Then, the values of $ \theta $ satisfying the inequality correspond to:
$$
\theta \in [2 \arccos(k), 2\pi - 2 \arccos(k)]
$$
The total measure of such $ \theta $ is:
$$
2\pi - 4 \arccos(k)
$$
Thus, the probability that a random chord intersects $ \Delta $ is:
$$
P(r) = \frac{1}{2\pi} (2\pi - 4 \arccos(k)) = 1 - \frac{2}{\pi} \arccos\left(\frac{1}{9 - r}\right)
$$

---

### **Optimization**

We now analyze how $ P(r) $ behaves as $ r $ increases from 0 to 8.

- As $ r $ increases, $ 9 - r $ decreases from 9 to 1.
- Therefore, $ \frac{1}{9 - r} $ increases from $ \frac{1}{9} $ to 1.
- Since $ \arccos(x) $ is a **decreasing function**, $ \arccos\left(\frac{1}{9 - r}\right) $ **decreases** as $ r $ increases.
- Consequently, $ P(r) = 1 - \frac{2}{\pi} \arccos\left(\frac{1}{9 - r}\right) $ **increases** as $ r $ increases.

Hence, $ P(r) $ is **strictly increasing** on $ [0, 8] $, and its **minimum occurs at $ r = 0 $**.

---

### **Verification via Derivative**

Define:
$$
P(r) = 1 - \frac{2}{\pi} \arccos\left(\frac{1}{9 - r}\right)
$$
Differentiating:
$$
P'(r) = \frac{2}{\pi} \cdot \frac{1}{(9 - r)^2 \sqrt{1 - \left(\frac{1}{9 - r}\right)^2}} > 0 \quad \text{for } r \in [0, 8)
$$
So $ P(r) $ is strictly increasing on $ [0, 8] $, confirming the minimum occurs at $ r = 0 $.

---

### **Conclusion**

The probability that a random chord $ PQ $ intersects the disc $ \Delta $ is minimized when the disc is centered at the origin, i.e., when $ r = 0 $.

$$
\boxed{0}
$$
