# putnam_2024_B5

## Problem

Let $k$ and $m$ be positive integers. For a positive integer $n$, let $f(n)$ be the number of integer sequences $x_1, \ldots, x_k, y_1, \ldots, y_m, z$ satisfying $1 \le x_1 \le \cdots \le x_k \le z \le n$ and $1 \le y_1 \le \cdots \le y_m \le z \le n$. Show that $f(n)$ can be expressed as a polynomial in $n$ with nonnegative coefficients.

## Submission

To show that the function $ f(n) $, defined as the number of integer sequences satisfying the conditions:

$$
1 \le x_1 \le \cdots \le x_k \le z \le n \quad \text{and} \quad 1 \le y_1 \le \cdots \le y_m \le z \le n,
$$

can be expressed as a **polynomial in $ n $ with nonnegative coefficients**, we proceed by analyzing its structure.

---

### Step 1: Counting for Fixed $ z $

For a fixed value of $ z $ (with $ 1 \le z \le n $), the number of non-decreasing sequences $ x_1 \le \cdots \le x_k \le z $ is given by the binomial coefficient:

$$
\binom{z + k - 1}{k},
$$

which counts the number of multisets of size $ k $ from a set of size $ z $. Similarly, the number of such $ y $-sequences is:

$$
\binom{z + m - 1}{m}.
$$

Thus, for each fixed $ z $, the number of valid combinations of $ x $- and $ y $-sequences is:

$$
\binom{z + k - 1}{k} \cdot \binom{z + m - 1}{m}.
$$

Summing over all possible values of $ z $ from 1 to $ n $, we obtain:

$$
f(n) = \sum_{z=1}^{n} \binom{z + k - 1}{k} \cdot \binom{z + m - 1}{m}.
$$

---

### Step 2: Polynomial Structure of the Sum

Each term $ \binom{z + k - 1}{k} $ is a polynomial in $ z $ of degree $ k $ with **positive rational coefficients**. For example:

$$
\binom{z + k - 1}{k} = \frac{(z + k - 1)(z + k - 2)\cdots z}{k!},
$$

which expands to a polynomial in $ z $ with all positive coefficients.

Similarly, $ \binom{z + m - 1}{m} $ is a polynomial in $ z $ of degree $ m $ with positive rational coefficients.

The product of two such polynomials is also a polynomial in $ z $ of degree $ k + m $, and since both polynomials have **only positive coefficients**, their product will also have **only positive coefficients**.

Now, consider the sum:

$$
f(n) = \sum_{z=1}^{n} P(z),
$$

where $ P(z) $ is a polynomial in $ z $ with **positive coefficients**. A well-known result in combinatorics and polynomial theory is that the sum of a polynomial with positive coefficients from $ z = 1 $ to $ n $ results in a polynomial in $ n $ with **all positive coefficients**.

This follows because:

- The sum $ \sum_{z=1}^n z^d $ is a polynomial in $ n $ of degree $ d+1 $ with all positive coefficients.
- Since $ P(z) $ is a linear combination of powers of $ z $ with positive coefficients, the sum $ \sum_{z=1}^n P(z) $ is a linear combination of these sums with positive coefficients — hence, it has **all positive coefficients**.

---

### Step 3: Conclusion

Therefore, $ f(n) $ is a polynomial in $ n $ whose coefficients are all **positive**, and thus **nonnegative**. This satisfies the requirement of the problem.

---

### Final Answer

$$
\boxed{f(n) \text{ can be expressed as a polynomial in } n \text{ with nonnegative coefficients.}}
$$
