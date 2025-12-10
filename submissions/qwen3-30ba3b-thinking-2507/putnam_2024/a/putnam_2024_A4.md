# putnam_2024_A4

## Problem

Find all primes $p > 5$ for which there exists an integer $a$ and an integer $r$ satisfying $1 \le r \le p-1$ with the following property: the sequence $1, a, a^2, \ldots, a^{p-5}$ can be rearranged to form a sequence $b_0, b_1, b_2, \ldots, b_{p-5}$ such that $b_n - b_{n-1} - r$ is divisible by $p$ for $1 \le n \le p-5$.

## Submission

To solve the problem, we are given a prime $ p > 5 $ and asked to find all such primes for which there exists an integer $ a $ and an integer $ r $ with $ 1 \leq r \leq p-1 $, such that the sequence $ 1, a, a^2, \ldots, a^{p-5} $ can be rearranged into a sequence $ b_0, b_1, \ldots, b_{p-5} $ satisfying:

$$
b_n - b_{n-1} - r \equiv 0 \pmod{p}, \quad \text{for } 1 \leq n \leq p-5.
$$

---

### Key Observations

1. **Sequence Length**:  
   The original sequence has $ (p - 5) - 0 + 1 = p - 4 $ terms. So the set $ S = \{a^k \mid k = 0, 1, \dots, p-5\} $ must have $ p - 4 $ distinct elements modulo $ p $.

2. **Arithmetic Progression Condition**:  
   The condition implies that the set $ S $ must be equal (as a set) to an arithmetic progression modulo $ p $ of length $ p - 4 $. That is, $ S = \{c, c + r, c + 2r, \dots, c + (p-5)r\} \mod p $, for some $ c $ and $ r \neq 0 $.

3. **Difference Set Argument**:  
   A key insight from additive combinatorics is that for any arithmetic progression $ A $ of length $ N $ in $ \mathbb{Z}/p\mathbb{Z} $, the difference set $ A - A $ has size exactly $ 2N - 1 $. Since $ A \subseteq \mathbb{Z}/p\mathbb{Z} $, it follows that:

   $$
   |A - A| = 2N - 1 \leq p.
   $$

   Substituting $ N = p - 4 $, we get:

   $$
   2(p - 4) - 1 \leq p \Rightarrow 2p - 9 \leq p \Rightarrow p \leq 9.
   $$

   Therefore, the only possible prime $ p > 5 $ satisfying this inequality is $ p = 7 $.

---

### Verification for $ p = 7 $

Let’s verify that $ p = 7 $ satisfies the condition.

- $ N = p - 4 = 3 $: The sequence is $ 1, a, a^2 $.
- Let $ a = 3 $, a primitive root modulo 7 (since $ 3^6 \equiv 1 \mod 7 $).
- Compute powers modulo 7:
  - $ a^0 = 1 $
  - $ a^1 = 3 $
  - $ a^2 = 9 \equiv 2 \mod 7 $
- So the sequence is $ [1, 3, 2] $, which can be rearranged as $ [1, 2, 3] $.
- This is an arithmetic progression with common difference $ r = 1 $, and all conditions are satisfied:
  - $ 2 - 1 = 1 $
  - $ 3 - 2 = 1 $

Thus, $ p = 7 $ works.

---

### Why No Other Primes Work

For any $ p > 7 $, we have $ N = p - 4 $, so the required inequality becomes:

$$
2(p - 4) - 1 = 2p - 9 > p \quad \text{when } p > 9.
$$

This violates the necessary constraint $ |A - A| \leq p $, meaning no such arithmetic progression of length $ p - 4 $ can exist in $ \mathbb{Z}/p\mathbb{Z} $, hence no such prime $ p > 7 $ can satisfy the condition.

---

### Final Answer

$$
\boxed{7}
$$
