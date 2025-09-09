# Solution 2

1. First, let input $1$ be: $n = 9$, and input $2$ be: $3, 1, 5, 4, 6, 9, 7, 8$ (or any $8$ randomly arranged numbers in the range of $1-9$). Let the missing number be $m$.

2. Create $1$ array:
    
    $A1: 1, 2, 3, 4, 5, 6, 7, 8, 9$ (the original correct sequence)

3. Next, using this formula below to find out the sum of the arithmetic series $A1$:

$$
S_n = \frac{n}{2}(a_1 + a_n)
$$

4. Smilarly, find the sum of the numbers in input $2$ by breaking it down into two series:

$$
S_1 = \frac{m - 1}{2}(1 + m - 1)
$$

$$
S_2 = \frac{n - (m + 1) + 1}{2}(m + 1 + n)
$$

5. Subtract the sum of $S_1$ and $S_2$ from the sum of $A1$

6. Finally we will get the answer $m$, which is the missing number we are looking for!