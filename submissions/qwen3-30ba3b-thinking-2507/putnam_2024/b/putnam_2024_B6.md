# putnam_2024_B6

## Problem

For a real number $a$, let $F_a(x) = \sum_{n \ge 1} n^a e^{2n} x^{n^2}$ for $0 \le x < 1$. Find a real number $c$ such that
$$\lim_{x \to 1^-} F_a(x) e^{-1/(1-x)} = 0 \text{ for all } a < c, \text{ and}$$
$$\lim_{x \to 1^-} F_a(x) e^{-1/(1-x)} = \infty \text{ for all } a > c.$$

## Submission

To solve the problem, we are given a function:

$$
F_a(x) = \sum_{n \ge 1} n^a e^{2n} x^{n^2}, \quad \text{for } 0 \le x < 1,
$$

and asked to find a real number $ c $ such that:

$$
\lim_{x \to 1^-} F_a(x) e^{-1/(1 - x)} = 
\begin{cases}
0 & \text{if } a < c, \\
\infty & \text{if } a > c.
\end{cases}
$$

---

### Step 1: Change of Variables

Let us define $ t = 1 - x $, so as $ x \to 1^- $, we have $ t \to 0^+ $. Then $ x = 1 - t $, and we approximate $ \ln x \approx -t $ for small $ t $. Therefore,

$$
x^{n^2} = e^{n^2 \ln x} \approx e^{-n^2 t}.
$$

The general term in the sum becomes approximately:

$$
n^a e^{2n} x^{n^2} \approx n^a e^{2n - n^2 t}.
$$

We complete the square in the exponent:

$$
2n - n^2 t = -t(n^2 - \frac{2}{t}n) = -t\left( n - \frac{1}{t} \right)^2 + \frac{1}{t}.
$$

Thus, the general term is approximately:

$$
n^a e^{1/t - t(n - 1/t)^2} = n^a e^{1/t} e^{-t(n - 1/t)^2}.
$$

So the entire sum becomes:

$$
F_a(x) \approx e^{1/t} \sum_{n=1}^\infty n^a e^{-t(n - 1/t)^2}.
$$

Now consider the expression we're interested in:

$$
F_a(x) e^{-1/t} \approx \sum_{n=1}^\infty n^a e^{-t(n - 1/t)^2}.
$$

Let us denote this sum by $ S(t) $, so:

$$
S(t) = \sum_{n=1}^\infty n^a e^{-t(n - 1/t)^2}.
$$

---

### Step 2: Asymptotic Analysis Using Laplace's Method

As $ t \to 0^+ $, the peak of the exponential $ e^{-t(n - 1/t)^2} $ occurs at $ n = 1/t $, and the width of the peak is $ O(1/\sqrt{t}) $. The function $ n^a $ is slowly varying near the peak (since $ n \sim 1/t $), so we can approximate the sum by an integral over $ n $.

Let’s make the substitution:

$$
u = \sqrt{t}(n - 1/t), \quad \text{so that } n = \frac{1}{t} + \frac{u}{\sqrt{t}}, \quad dn = \frac{du}{\sqrt{t}}.
$$

Then:

$$
n^a = \left( \frac{1}{t} + \frac{u}{\sqrt{t}} \right)^a = t^{-a} \left( 1 + u \sqrt{t} \right)^a \approx t^{-a} \left( 1 + a u \sqrt{t} \right),
$$

and the exponent becomes:

$$
-t(n - 1/t)^2 = -u^2.
$$

Therefore, the integral approximation gives:

$$
S(t) \approx \int_{-\infty}^\infty t^{-a} \left(1 + a u \sqrt{t} \right) e^{-u^2} \cdot \frac{du}{\sqrt{t}} = t^{-a - 1/2} \int_{-\infty}^\infty e^{-u^2} du + \text{higher order terms}.
$$

Since $ \int_{-\infty}^\infty e^{-u^2} du = \sqrt{\pi} $, we get:

$$
S(t) \sim \sqrt{\pi} \cdot t^{-a - 1/2}, \quad \text{as } t \to 0^+.
$$

---

### Step 3: Behavior of the Limit

Recall that $ t = 1 - x $, so:

$$
\lim_{x \to 1^-} F_a(x) e^{-1/(1 - x)} = \lim_{t \to 0^+} S(t) \sim \sqrt{\pi} \cdot t^{-a - 1/2}.
$$

Now analyze the behavior of $ t^{-a - 1/2} $ as $ t \to 0^+ $:

- If $ -a - 1/2 > 0 $, i.e., $ a < -1/2 $, then $ t^{-a - 1/2} \to 0 $.
- If $ -a - 1/2 < 0 $, i.e., $ a > -1/2 $, then $ t^{-a - 1/2} \to \infty $.

Hence, the critical value of $ a $ where the limit switches from 0 to $ \infty $ is when $ -a - 1/2 = 0 $, or:

$$
a = -\frac{1}{2}.
$$

At $ a = -1/2 $, the leading term is constant, and the limit is finite and non-zero.

---

### Final Answer

$$
\boxed{-\dfrac{1}{2}}
$$
