# putnam_2024_A2

## Problem

For which real polynomials $p$ is there a real polynomial $q$ such that
$$p(p(x)) - x = (p(x) - x)^2 q(x)$$
for all real $x$?

## Submission

To determine all real polynomials $ p $ such that there exists a real polynomial $ q $ satisfying

$$
p(p(x)) - x = (p(x) - x)^2 q(x)
$$

for all real $ x $, we proceed by analyzing the structure of the equation and using properties of polynomials.

---

### **Step 1: Reformulating the Equation**

Let us define:

$$
d(x) = p(x) - x.
$$

Then $ p(x) = x + d(x) $, and we can express the left-hand side as:

$$
p(p(x)) - x = d(x) + d(x + d(x)).
$$

The given condition becomes:

$$
d(x) + d(x + d(x)) = d(x)^2 q(x).
$$

This implies that $ d(x)^2 \mid d(x) + d(x + d(x)) $ in the ring of real polynomials.

---

### **Step 2: Necessary Conditions from Polynomial Structure**

We analyze the degrees and use a Taylor expansion to derive a key condition. Consider the behavior of $ d(x + d(x)) $ around $ x $. Using a Taylor expansion of $ d $ at $ x $, we find:

$$
d(x + d(x)) \equiv d(x) + d'(x)d(x) \mod d(x)^2.
$$

Thus,

$$
d(x) + d(x + d(x)) \equiv 2d(x) + d'(x)d(x) \mod d(x)^2.
$$

Setting this equal to $ d(x)^2 q(x) $, which is divisible by $ d(x)^2 $, gives:

$$
2d(x) + d'(x)d(x) \equiv 0 \mod d(x)^2,
$$

or equivalently,

$$
d'(x) + 2 \equiv 0 \mod d(x).
$$

So we obtain the necessary condition:

$$
d'(x) + 2 = d(x) r(x),
$$

for some polynomial $ r(x) $.

---

### **Step 3: Degree Analysis**

Let $ n = \deg d(x) $. Then:

- $ \deg(d'(x)) = n - 1 $ if $ n \geq 1 $,
- $ \deg(d(x) r(x)) = n + \deg r(x) $.

For the equality $ d'(x) + 2 = d(x) r(x) $ to hold, the degree of the right-hand side must match the left-hand side. The only way this is possible is when $ n = 0 $ or $ n = 1 $, because for $ n \geq 2 $, $ \deg(d(x) r(x)) \geq n > n - 1 = \deg(d'(x)) $, leading to a contradiction unless $ r(x) $ has negative degree (which is not allowed).

---

### **Case 1: $ d(x) = 0 $**

This corresponds to $ p(x) = x $. Then:

- $ p(p(x)) = x $, so $ p(p(x)) - x = 0 $,
- $ (p(x) - x)^2 = 0 $, so the equation holds trivially with any $ q(x) $.

✅ **Valid solution.**

---

### **Case 2: $ \deg d(x) = 0 $, i.e., $ d(x) = c $, constant**

Then $ p(x) = x + c $, and:

- $ p(p(x)) = x + 2c $, so $ p(p(x)) - x = 2c $,
- $ (p(x) - x)^2 = c^2 $, so $ 2c = c^2 q(x) $.

This is solvable for $ q(x) $ if $ c \ne 0 $: set $ q(x) = \frac{2}{c} $, a constant polynomial.

If $ c = 0 $, then $ p(x) = x $, which is already covered in Case 1.

✅ **All polynomials of the form $ p(x) = x + c $, $ c \in \mathbb{R} $, are valid solutions.**

---

### **Case 3: $ \deg d(x) = 1 $, i.e., $ d(x) = mx + k $, $ m \ne 0 $**

Then $ p(x) = x + mx + k = (m+1)x + k $, and $ d'(x) = m $. From the earlier derived condition:

$$
d'(x) + 2 = d(x) r(x) \Rightarrow m + 2 = (mx + k) r(x).
$$

The right-hand side is a linear polynomial times $ r(x) $, so the only way the left-hand side (a constant) can equal the right-hand side is if $ r(x) = 0 $, giving $ m + 2 = 0 \Rightarrow m = -2 $.

Thus, $ d(x) = -2x + k $, and $ p(x) = x + (-2x + k) = -x + k $.

Now check the original equation:

- $ p(p(x)) = p(-x + k) = -(-x + k) + k = x $,
- So $ p(p(x)) - x = 0 $,
- And $ (p(x) - x)^2 = (-2x + k)^2 $, so the equation holds for any $ q(x) $, including $ q(x) = 0 $.

✅ **All polynomials of the form $ p(x) = -x + k $, $ k \in \mathbb{R} $, are valid solutions.**

---

### **Case 4: $ \deg d(x) \geq 2 $**

As shown earlier, this leads to a contradiction in degrees. Specifically, $ \deg(d'(x)) = n - 1 < n = \deg(d(x)) \leq \deg(d(x)r(x)) $, so no such polynomial can satisfy the required identity.

❌ **No solutions exist for $ \deg d(x) \geq 2 $.**

---

### **Final Answer**

Combining all cases, the only real polynomials $ p $ satisfying the given condition are:

- All constant shifts of the identity function:  
  $$
  p(x) = x + c, \quad c \in \mathbb{R}.
  $$

- All linear involutions:  
  $$
  p(x) = -x + k, \quad k \in \mathbb{R}.
  $$

These two families are disjoint (since $ x + c = -x + k $ would imply $ 2x = k - c $, impossible for all $ x $), and together they constitute all solutions.

---

### ✅ **Answer**

$$
\boxed{p(x) = x + c \text{ for some } c \in \mathbb{R}, \quad \text{or} \quad p(x) = -x + k \text{ for some } k \in \mathbb{R}}
$$
