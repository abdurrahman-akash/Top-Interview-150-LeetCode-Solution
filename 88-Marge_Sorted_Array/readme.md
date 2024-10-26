# [LeetCode- 88. Merge Sorted Arrat](https://leetcode.com/problems/merge-sorted-array)
## Problem Description
 You are given two integer arrays **nums1** and **nums2**, sorted in non-decreasing order, and two integers *m* and *n*, representing the number of elements in **nums1** and **nums2** respectively.

Merge **nums1** and **nums2** into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array **nums1**. To accommodate this, **nums1** has a length of *m + n*, where the first *m* elements denote the elements that should be merged, and the last *n* elements are set to 0 and should be ignored. **nums2** has a length of *n*.

## Solution: A story example
Imagine you and your friend each have a collection of books. You have a bookshelf (let’s call it **nums1**) that contains *m* books sorted in order, while the remaining *n* slots are empty (represented by zeros). Your friend has another bookshelf (**nums2**) filled with *n* sorted books.



𝗘𝘅𝗮𝗺𝗽𝗹𝗲: Your bookshelf (**nums1**) looks like this: [1, 2, 3, 0, 0, 0]

Here, *m* = 3, meaning you have three books (1, 2, 3), and the last three slots are empty.

Your friend's bookshelf (**nums2**) is: [2, 5, 6]

Here, *n* = 3, meaning your friend has three books (2, 5, 6).



### 𝗧𝗵𝗲 𝗖𝗵𝗮𝗹𝗹𝗲𝗻𝗴𝗲:

Your task is to merge these two collections into one sorted bookshelf.



### 𝗔𝗽𝗽𝗿𝗼𝗮𝗰𝗵:

1. Start from the Back: Begin comparing the last books of **nums1** and **nums2**. Since **nums1** has space, you can add the new books at the end.



2. Compare Books: Compare the last book in **nums1** (where the zeros are) with the last book in **nums2**. Place the larger book at the end of **nums1**, and update the positions accordingly.



3. Sequential Addition: Continue this process until you've compared all the books in **nums2**.



This problem-solving approach is not only applicable to coding challenges but also a great metaphor for merging different ideas and experiences in life.

## Complexity
- #### Time Complexity: O(m+n)
- #### Space Complexity: O(1)


### I'm excited to dive deeper into data structures and algorithms as I prepare for my next coding challenges! If you have tips or resources to share, I’d love to hear from you!



### 𝗛𝗮𝗽𝗽𝘆 𝗰𝗼𝗱𝗶𝗻𝗴! 🚀