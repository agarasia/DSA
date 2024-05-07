
# DSA Preparation Cheat Sheet

## Arrays : Easy

1. Move Zeros to end
2. Find the union
3. Longest subarray of Sum K (positive numbers)
4. Longest subarray of Sum K (positive and negative numbers)

## Approaches to remember for each question

### Move Zeros to end
1.  First, using a loop, we will place the pointer j. If we don’t find any 0, we will not perform the following steps.
2.  After that, we will point i to index j+1 and start moving the pointer using a loop.
3.  While moving the pointer i, we will do the following:
    1.  **If a[i] != 0 i.e. a[i] is a non-zero element:** We will swap a[i] and a[j]. Now, the current j is pointing to the non-zero element a[i]. So, we will shift the pointer j by 1 so that it can again point to the first zero.
4.  Finally, our array will be set in the right manner.

### Find the union
Use Set data structure or a map data structure.

### Longest subarray of Sum K (positive numbers)

First, check brute-force (find all possible subarrays and find the longest)
Optimal algorithm:
1.  First, we will take two pointers: left and right, initially pointing to the index 0.
2.  The sum is set to a[0] i.e. the first element initially.
3.  Now we will run a while loop until the right pointer crosses the last index i.e. n-1.
4.  Inside the loop, we will do the following:
    1.  We will use another while loop and it will run until the sum is lesser or equal to k.
        1.  Inside this second loop, from the sum, we will subtract the element that is pointed by the left pointer and increase the left pointer by 1.
    2.  After this loop gets completed, we will check if the sum is equal to k. If it is, we will compare the length of the current subarray i.e. (right-left+1) with the existing one and consider the maximum one.
    3.  Then we will move forward the right pointer by 1. If the right pointer is pointing to a valid index(< n) after the increment, we will add the element i.e. a[right] to the sum.
5.  Finally, we will return the maximum length.


#### Note: Time complexity is still O(n). HOW?
##### The second loop is not running for n times for all n elements.
