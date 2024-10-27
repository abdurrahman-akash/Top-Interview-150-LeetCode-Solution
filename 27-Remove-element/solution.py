class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for num in nums:
            if val != num:
                nums[i] = num
                i += 1
        return i

# Function to take user input
def main():
    # Input: list of numbers
    nums_input = input("Enter a list of numbers (comma-separated): ")
    nums = [int(num) for num in nums_input.split(",")]
    
    # Input: value to remove
    val = int(input("Enter the value to remove: "))
    
    # Create an instance of Solution and call removeElement
    solution = Solution()
    new_length = solution.removeElement(nums, val)
    
    # Output the results
    print(f"New length of the array: {new_length}")
    print(f"Modified array: {nums[:new_length]}")

if __name__ == "__main__":
    main()