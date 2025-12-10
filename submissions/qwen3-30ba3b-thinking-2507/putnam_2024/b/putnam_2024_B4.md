# putnam_2024_B4

## Problem

Let $n$ be a positive integer. Set $a_{n,0} = 1$. For $k \ge 0$, choose an integer $m_{n,k}$ uniformly at random from the set $\{1,\ldots,n\}$, and let
$$a_{n,k+1} = \begin{cases}
a_{n,k} + 1, & \text{if } m_{n,k} > a_{n,k}; \\
a_{n,k}, & \text{if } m_{n,k} = a_{n,k}; \\
a_{n,k} - 1, & \text{if } m_{n,k} < a_{n,k}.
\end{cases}$$
Let $E(n)$ be the expected value of $a_{n,n}$. Determine $\lim_{n \to \infty} E(n)/n$.

## Submission

To determine the limit  
$$
\lim_{n \to \infty} \frac{E(n)}{n},
$$
we analyze the process defined by the recurrence:

- Start with $ a_{n,0} = 1 $,
- For each $ k \geq 0 $, choose $ m_{n,k} \in \{1, 2, \ldots, n\} $ uniformly at random,
- Define:
  $$
  a_{n,k+1} =
  \begin{cases}
  a_{n,k} + 1 & \text{if } m_{n,k} > a_{n,k}, \\
  a_{n,k} & \text{if } m_{n,k} = a_{n,k}, \\
  a_{n,k} - 1 & \text{if } m_{n,k} < a_{n,k}.
  \end{cases}
  $$

Let $ E(n) = \mathbb{E}[a_{n,n}] $, the expected value of $ a_{n,n} $ after $ n $ steps.

---

### Step 1: Derive the Expectation Recurrence

Let $ X_k = a_{n,k} $. Then,

$$
\mathbb{E}[X_{k+1} \mid X_k = x] = 
\frac{(x+1)(n - x) + x + (x-1)^2}{n} = \frac{(n - 2)x + (n + 1)}{n}.
$$

This is linear in $ x $, so the expectation satisfies the recurrence:

$$
E_{k+1} = \left( \frac{n - 2}{n} \right) E_k + \frac{n + 1}{n}, \quad \text{with } E_0 = 1.
$$

This is a linear nonhomogeneous recurrence. Solving it gives:

$$
E_k = \frac{n + 1}{2} + \frac{1 - n}{2} \left( \frac{n - 2}{n} \right)^k.
$$

Setting $ k = n $, we get:

$$
E(n) = \frac{n + 1}{2} + \frac{1 - n}{2} \left( \frac{n - 2}{n} \right)^n.
$$

---

### Step 2: Compute the Limit

We are interested in:

$$
\lim_{n \to \infty} \frac{E(n)}{n} = \lim_{n \to \infty} \left[ \frac{n + 1}{2n} + \frac{1 - n}{2n} \left( \frac{n - 2}{n} \right)^n \right].
$$

Break this into two parts:

1. $ \frac{n + 1}{2n} = \frac{1}{2} + \frac{1}{2n} \to \frac{1}{2} $ as $ n \to \infty $,
2. $ \frac{1 - n}{2n} = -\frac{1}{2} + \frac{1}{2n} \to -\frac{1}{2} $,
3. $ \left( \frac{n - 2}{n} \right)^n = (1 - \tfrac{2}{n})^n \to e^{-2} $.

Therefore,

$$
\lim_{n \to \infty} \frac{E(n)}{n} = \frac{1}{2} - \frac{1}{2} e^{-2} = \frac{1 - e^{-2}}{2}.
$$

---

### Step 3: Confirmation via Continuous Approximation

For large $ n $, define $ t = \frac{k}{n} \in [0,1] $, and let $ x(t) = \frac{E_k}{n} $. The recurrence becomes approximately:

$$
\frac{dx}{dt} = -2x + 1, \quad x(0) = 0.
$$

Solving this ODE yields:

$$
x(t) = \frac{1 - e^{-2t}}{2}.
$$

At $ t = 1 $, we have:

$$
x(1) = \frac{1 - e^{-2}}{2},
$$

which matches our earlier result.

---

### Final Answer

$$
\boxed{\dfrac{1 - e^{-2}}{2}}
$$
