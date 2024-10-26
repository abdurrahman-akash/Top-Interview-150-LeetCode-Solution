from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
         # Initialize pointers for nums1 and nums2
        left = m-1
        right = n-1
        index = m+n-1 # Pointer for the last position in nums1.

        # Merge in reverse order
        while left >=0 and right >=0:
            if nums1[left] > nums2[right]:
                nums1[index] = nums1[left]
                left -= 1
            else:
                nums1[index] = nums2[right]
                right -= 1
            index -= 1

        # If there are remaining elements in nums2, copy them over
        while right >=0:
            nums1[index] = nums2[right]
            right -= 1
            index -= 1
        
        
def main():
    # Input for nums1
    nums1_input = input("Enter the elements of nums1 (followed by zeros for the empty slots), separated by commas: ")
    nums1 = list(map(int, nums1_input.split(',')))
    
    # Input for m (number of valid elements in nums1)
    m = int(input("Enter the number of valid elements in nums1 (m): "))
    
    # Input for nums2
    nums2_input = input("Enter the elements of nums2, separated by commas: ")
    nums2 = list(map(int, nums2_input.split(',')))
    
    # Input for n (number of valid elements in nums2)
    n = int(input("Enter the number of valid elements in nums2 (n): "))
    
    # Create a Solution object
    solution = Solution()
    
    # Call the merge function
    solution.merge(nums1, m, nums2, n)
    
    # Print the merged result
    print("Merged array:", nums1)

if __name__ == "__main__":
    main()