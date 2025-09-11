# Solution

1. First, let the input $n$ be 5, and the array be 5, 3, 8, 7, 9 (the values here are just an example, you can choose whatever numbers you like)

2. Because each of the elements should be at least as large as the previous element, let's take the second element "$3$" for an instance-as we can see, "$3$" is smaller than its previous element "$5$", so we need to increase its by at least 2. And because you can only increase 1 at a time, this process takes **2** steps

3. And so on, you work out that the third element "$8$" is greater than the second element, so it stays the same and no steps were taken

4. Finally we get that the minimum steps for it to take to let the modified array meet the requirements is **3**