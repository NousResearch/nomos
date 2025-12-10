# putnam_2024_B3

## Problem

Let $r_n$ be the $n$th smallest positive solution to $\tan x = x$, where the argument of tangent is in radians. Prove that
$$0 < r_{n+1} - r_n - \pi < \frac{1}{(n^2 + n)\pi}$$
for $n \ge 1$.

## Submission

To prove the inequality

$$
0 < r_{n+1} - r_n - \pi < \frac{1}{(n^2 + n)\pi}
$$

for all $ n \geq 1 $, where $ r_n $ is the $ n $th smallest positive solution to $ \tan x = x $, we proceed as follows:

---

### **Step 1: Understanding the Structure of Solutions**

The equation $ \tan x = x $ has infinitely many solutions in the positive real numbers. The tangent function has vertical asymptotes at $ x = (k + \frac{1}{2})\pi $ for integer $ k $, and between each pair of consecutive asymptotes $ ((k - \frac{1}{2})\pi, (k + \frac{1}{2})\pi) $, $ \tan x $ increases from $ -\infty $ to $ +\infty $, so it intersects the line $ y = x $ exactly once in each such interval.

Thus, for each $ n \geq 1 $, there exists a unique solution $ r_n \in ((n - \frac{1}{2})\pi, (n + \frac{1}{2})\pi) $ such that $ \tan r_n = r_n $. This defines the sequence $ r_n $ of positive solutions.

---

### **Step 2: Change of Variables**

Let us define:
$$
r_n = n\pi + \theta_n
$$
Then $ \theta_n \in (0, \frac{\pi}{2}) $ because $ r_n \in ((n - \frac{1}{2})\pi, (n + \frac{1}{2})\pi) $.

Substituting into the equation $ \tan r_n = r_n $, we get:
$$
\tan(n\pi + \theta_n) = n\pi + \theta_n \Rightarrow \tan \theta_n = n\pi + \theta_n
$$
So $ \theta_n $ satisfies:
$$
\tan \theta_n = n\pi + \theta_n, \quad \text{with } \theta_n \in (0, \frac{\pi}{2})
$$

This implies that $ \theta_n = \arctan(n\pi + \theta_n) $.

---

### **Step 3: Expressing the Difference $ r_{n+1} - r_n - \pi $**

We now compute:
$$
r_{n+1} - r_n = (n+1)\pi + \theta_{n+1} - n\pi - \theta_n = \pi + (\theta_{n+1} - \theta_n)
$$
Therefore,
$$
r_{n+1} - r_n - \pi = \theta_{n+1} - \theta_n
$$

So the inequality becomes:
$$
0 < \theta_{n+1} - \theta_n < \frac{1}{(n^2 + n)\pi}
$$

---

### **Step 4: Proving the Inequality**

Let’s denote:
$$
A = n\pi + \theta_n, \quad B = (n+1)\pi + \theta_{n+1}
$$
From the definition of $ \theta_n $, we have:
$$
\tan \theta_n = A, \quad \tan \theta_{n+1} = B
$$
Hence:
$$
\theta_n = \arctan A, \quad \theta_{n+1} = \arctan B
$$
So:
$$
\theta_{n+1} - \theta_n = \arctan B - \arctan A
$$

Using the identity for the difference of arctangents:
$$
\arctan B - \arctan A = \int_A^B \frac{1}{1 + t^2} \, dt
$$
Since $ \frac{1}{1 + t^2} < \frac{1}{t^2} $ for all $ t > 0 $, we can bound the integral:
$$
\int_A^B \frac{1}{1 + t^2} \, dt < \int_A^B \frac{1}{t^2} \, dt = \frac{1}{A} - \frac{1}{B}
$$

Now, observe:
- $ A = n\pi + \theta_n > n\pi $ since $ \theta_n > 0 $
- $ B = (n+1)\pi + \theta_{n+1} > (n+1)\pi $ since $ \theta_{n+1} > 0 $

So:
$$
\frac{1}{A} < \frac{1}{n\pi}, \quad \frac{1}{B} < \frac{1}{(n+1)\pi}
$$
Thus:
$$
\theta_{n+1} - \theta_n < \frac{1}{n\pi} - \frac{1}{(n+1)\pi} = \frac{1}{n(n+1)\pi}
$$

Also, since $ \theta_n $ is strictly increasing (as $ \tan \theta_n = n\pi + \theta_n $ increases with $ n $), we have:
$$
\theta_{n+1} > \theta_n \Rightarrow \theta_{n+1} - \theta_n > 0
$$

Therefore:
$$
0 < \theta_{n+1} - \theta_n < \frac{1}{n(n+1)\pi}
$$

Recall that $ n(n+1) = n^2 + n $, so the inequality becomes:
$$
0 < r_{n+1} - r_n - \pi < \frac{1}{(n^2 + n)\pi}
$$

---

### **Final Answer**

$$
\boxed{0 < r_{n+1} - r_n - \pi < \frac{1}{(n^2 + n)\pi}}
$$

for all $ n \geq 1 $.
