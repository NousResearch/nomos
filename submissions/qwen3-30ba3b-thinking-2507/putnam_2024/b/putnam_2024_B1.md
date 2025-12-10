# putnam_2024_B1

## Problem

Let $n$ and $k$ be positive integers. The square in the $i$th row and $j$th column of an $n$-by-$n$ grid contains the number $i + j - k$. For which $n$ and $k$ is it possible to select $n$ squares from the grid, no two in the same row or column, such that the numbers contained in the selected squares are exactly $1, 2, \ldots, n$?

## Submission

To solve the problem, we analyze an $ n \times n $ grid where the entry in row $ i $ and column $ j $ is given by:

$$
a_{ij} = i + j - k
$$

We are to determine for which positive integers $ n $ and $ k $ it is possible to select $ n $ squares such that:
- No two selected squares share a row or column (i.e., they form a permutation matrix),
- The numbers on the selected squares are exactly $ 1, 2, \ldots, n $, in some order.

---

### **Step 1: Sum Condition**

Let $ \sigma $ be a permutation of $ \{1, 2, \ldots, n\} $, representing the column chosen in each row. Then the selected entries are:

$$
a_{i,\sigma(i)} = i + \sigma(i) - k
$$

Summing over all rows:

$$
\sum_{i=1}^n a_{i,\sigma(i)} = \sum_{i=1}^n (i + \sigma(i) - k) = \sum_{i=1}^n i + \sum_{i=1}^n \sigma(i) - nk
$$

Since $ \sigma $ is a permutation, both sums $ \sum i $ and $ \sum \sigma(i) $ equal $ \frac{n(n+1)}{2} $. Thus,

$$
\text{Total sum} = n(n+1) - nk
$$

This must equal the sum of the first $ n $ natural numbers:

$$
\frac{n(n+1)}{2}
$$

Equating both expressions:

$$
n(n+1) - nk = \frac{n(n+1)}{2}
$$

Dividing both sides by $ n $ (since $ n > 0 $):

$$
(n+1) - k = \frac{n+1}{2} \quad \Rightarrow \quad k = \frac{n+1}{2}
$$

Thus, **$ k $ must be an integer**, so $ n+1 $ must be even ⇒ $ n $ is **odd**.

---

### **Step 2: Constructive Sufficiency for Odd $ n $**

Let $ n = 2m - 1 $, so $ k = m $. We now show that for any odd $ n $, choosing $ k = \frac{n+1}{2} $ allows us to construct a valid selection of $ n $ squares satisfying the condition.

Define a permutation $ \sigma $ as follows:

- For $ i = 1 $ to $ m $:  
  $$
  \sigma(i) = i + m - 1
  $$
- For $ i = m+1 $ to $ n $:  
  $$
  \sigma(i) = i - m
  $$

This defines a valid permutation since:
- The values $ \sigma(i) $ for $ i = 1 $ to $ m $ range from $ m $ to $ n $,
- The values $ \sigma(i) $ for $ i = m+1 $ to $ n $ range from $ 1 $ to $ m-1 $,
- So all columns from $ 1 $ to $ n $ are used exactly once.

Now compute the corresponding values $ a_{i,\sigma(i)} $:

- For $ i = 1 $ to $ m $:
  $$
  a_{i,\sigma(i)} = i + (i + m - 1) - m = 2i - 1
  $$
  These yield the odd numbers $ 1, 3, 5, \ldots, 2m - 1 $.

- For $ i = m+1 $ to $ n $:
  Let $ i = m + t $, so $ t = 1 $ to $ m - 1 $, then:
  $$
  a_{i,\sigma(i)} = (m + t) + t - m = 2t
  $$
  These yield the even numbers $ 2, 4, 6, \ldots, 2(m - 1) $.

Together, these give all integers from $ 1 $ to $ n $, with no duplicates. Hence, the set of selected numbers is exactly $ \{1, 2, \ldots, n\} $.

---

### **Conclusion**

The only cases where such a selection is possible are when $ n $ is **odd**, and $ k = \frac{n+1}{2} $. For even $ n $, the required value of $ k $ would not be an integer, making it impossible to satisfy the sum condition.

---

### ✅ Final Answer:

$$
\boxed{n \text{ is odd and } k = \frac{n+1}{2}}
$$
