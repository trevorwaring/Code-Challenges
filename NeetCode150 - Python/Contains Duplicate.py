"""
# LeetCode 217 - Contains Duplicate

Questtions:
1. What is Time and Space Complexity ?
2. Data Structure used in the solution? HashSet
"""
# Return True if any value appears at least twice in the array, and False if every element is distinct.
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen = set()    # HashSet to store unique elements
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
    
    # Test cases
def test():
    solution = Solution()
    assert solution.containsDuplicate([1, 2, 3, 1]) == True
    assert solution.containsDuplicate([1, 2, 3, 4]) == False
    assert solution.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) == True
    assert solution.containsDuplicate([]) == False
    assert solution.containsDuplicate([1]) == False
    return "All test cases passed!"


if __name__ == "__main__":
    v = test()
    print(v)  # Output: All test cases passed!