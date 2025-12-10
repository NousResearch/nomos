# putnam_2024_A3

## Problem

Let $S$ be the set of bijections
$$T : \{1,2,3\} \times \{1,2,\ldots,2024\} \to \{1,2,\ldots,6072\}$$
such that $T(1,j) < T(2,j) < T(3,j)$ for all $j \in \{1,2,\ldots,2024\}$ and $T(i,j) < T(i,j+1)$ for all $i \in \{1,2,3\}$ and $j \in \{1,2,\ldots,2023\}$. Do there exist $a$ and $c$ in $\{1,2,3\}$ and $b$ and $d$ in $\{1,2,\ldots,2024\}$ such that the fraction of elements $T$ in $S$ for which $T(a,b) < T(c,d)$ is at least $1/3$ and at most $2/3$?

## Submission

To solve the problem, we analyze the set $ S $ of bijections $ T : \{1,2,3\} \times \{1,2,\ldots,2024\} \to \{1,2,\ldots,6072\} $ satisfying:

- **Column condition**: $ T(1,j) < T(2,j) < T(3,j) $ for all $ j $,
- **Row condition**: $ T(i,j) < T(i,j+1) $ for all $ i $ and $ j $.

This is precisely the definition of a *standard Young tableau* (SYT) of shape $ 3 \times 2024 $. The total number of such SYTs is given by the hook-length formula, but we don't need its exact value.

---

### Key Observation

For any two *incomparable* cells in the grid (i.e., neither is above-left nor below-right of the other), the relative order of their values in a random SYT is not fixed—it can be either way. Let’s denote an ordered pair of incomparable cells as $ (X, Y) $, where $ X = (a,b) $, $ Y = (c,d) $, and $ X $ and $ Y $ are incomparable.

Let $ p(X,Y) = \frac{|\{T \in S : T(X) < T(Y)\}|}{|S|} $ be the fraction of SYTs where $ T(X) < T(Y) $. Then $ p(X,Y) \in (0,1) $, since the order is not forced.

Now consider the set $ P $ of **all** ordered pairs $ (X,Y) $ with $ X $ and $ Y $ incomparable. For each unordered pair $ \{X,Y\} $, there are exactly two such ordered pairs: $ (X,Y) $ and $ (Y,X) $, and we have:
$$
p(X,Y) + p(Y,X) = 1.
$$

Therefore, the average value of $ p $ over all such ordered pairs is:
$$
\text{Average } p = \frac{1}{|P|} \sum_{(X,Y) \in P} p(X,Y) = \frac{1}{|P|} \cdot \frac{|P|}{2} = \frac{1}{2}.
$$

This is a **key insight**: the average of all these probabilities is exactly $ \frac{1}{2} $, which lies within the interval $ [\frac{1}{3}, \frac{2}{3}] $.

---

### Conclusion via Averaging Argument

Since the average of all $ p(X,Y) $ values is $ \frac{1}{2} $, it is **impossible** for all $ p(X,Y) $ to lie strictly outside $ [\frac{1}{3}, \frac{2}{3}] $. Therefore, **there must exist at least one** pair $ (X,Y) $ such that:
$$
\frac{1}{3} \leq p(X,Y) \leq \frac{2}{3}.
$$

In particular, this means that there exist indices $ a,c \in \{1,2,3\} $ and $ b,d \in \{1,2,\ldots,2024\} $ such that the fraction of elements $ T \in S $ with $ T(a,b) < T(c,d) $ is between $ \frac{1}{3} $ and $ \frac{2}{3} $, inclusive.

---

### Final Answer

$$
\boxed{\text{Yes}}
$$
