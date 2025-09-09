# Solution 1
1. First, let input 1 be: $n = 9$, and input $2$ be: $3, 1, 5, 4, 6, 9, 7, 8$ (or any $8$ randomly arranged numbers in the range of $1-9$)

2. Next rearrange the numbers in input $2$ in the order of small to large

3. Create $2$ arrays:
    
    $A1: 1, 2, 3, 4, 5, 6, 7, 8, 9$ (the original correct sequence)
    
    $A2: 1, 3, 4, 5, 6, 7, 8, 9$ (the rearranged version of input $2$)

4. Then compare the elements at position of the two arrays

5. Finally we find out that the missing number is $2$ because immediately after the same "$1$"s in $A1$ and $A2$, the "$2$" in $A1$ and "$3$" in $A2$ don't match