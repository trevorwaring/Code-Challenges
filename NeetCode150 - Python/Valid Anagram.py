"""
# LeetCode 242 - Valid Anagram

Questions:
1. What is Time and Space Complexity ?
2. Data Structure used in the solution? HashMap or Array
"""
# Code Prompt: Given 2 strings s and t, return true if t is an anagram of s, and false otherwise.

# # First Solution using Array:
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         """
#         :type s: str
#         :type t: str
#         :rtype: bool
#         """
#         # Check if the lengths of the strings are equal
#         if len(s) != len(t):
#             return False
        
#         count = [0] * 26  # Assuming only lowercase letters a-z
        
#         for char in s:
#             count[ord(char) - ord('a')] += 1
        
#         for char in t:
#             count[ord(char) - ord('a')] -= 1
#             if count[ord(char) - ord('a')] < 0:
#                 return False
        
#         return True
    

    
# Second Solution using HashMap:
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Check if the lengths of the strings are equal
        if len(s) != len(t):
            return False
        
        # Create a frequency dictionary for both strings
        count = {}
        
        # Count the frequency of each character in the first string
        for char in s:
            count[char] = count.get(char, 0) + 1
        
        # Decrease the frequency for each character in the second string
        for char in t:
            if char not in count or count[char] == 0:
                return False
            count[char] -= 1
        
        return all(value == 0 for value in count.values())



# #  Third Solution:
# class Solution2:
#     def isAnagram(self, s: str, t: str) -> bool:
#         """
#         :type s: str
#         :type t: str
#         :rtype: bool
#         """
#         if len(s) != len(t):
#             return False
        
#         # Create a frequency dictionary for both strings
#         count_s = {}
#         count_t = {}
        
#         # Count the frequency of each character in both strings
#         for char in s:
#             count_s[char] = count_s.get(char, 0) + 1
        
#         for char in t:
#             count_t[char] = count_t.get(char, 0) + 1
        
#         # Compare the frequency dictionaries
#         return count_s == count_t



# # Fourth Solution using count():
# class Solution3:
#     def isAnagram(self, s: str, t: str) -> bool:
#         """
#         :type s: str
#         :type t: str
#         :rtype: bool
#         """
#         # Check if the lengths of the strings are equal
#         if len(s) != len(t):
#             return False
        
#         # Check if the count of each character in both strings is the same
#         for char in set(s):
#             if s.count(char) != t.count(char):
#                 return False
#         return True
    


# # Fifth solution from YouTube Python Playlist:
# """
# Action to solve the problem:
# 1. Check if the lengths of the strings are equal
# 2. Create a frequency dictionary or HashMap for both strings
# 3. Compare the frequency dictionaries
# """

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         """
#         :type s: str
#         :type t: str
#         :rtype: bool
#         """

#         # Check if the lengths of the strings are equal
#         if len(s) != len(t):
#             return False
        
#         # Create a frequency dictionary or HashMaps for both strings
#         countS, counntT = {}, {}

#         # Count the frequency of each character in both strings
#         for i in range(len(s)):
#             countS[s[i]] = 1 + countS.get(s[i], 0)
#             counntT[t[i]] = 1 + counntT.get(t[i], 0)
        
#         # Compare the frequency dictionaries
#         for char in countS:
#             if countS[char] != counntT.get(char, 0):
#                 return False
#         return True
    

# # Sixth Solution
# """
# [Not the most efficient solution, but a good one]

# Returns True when both sorted strings are equal, indicating they are anagrams.
# Returns False when the lengths of the strings are not equal, indicating they cannot be anagrams.
        
# """

# class Solution4:
#     def isAnagram(self, s: str, t: str) -> bool:
#         """
#         :type s: str
#         :type t: str
#         :rtype: bool
#         """
#         if len(s) != len(t):
#             return False
        
#         # Sort both strings and compare
#         return sorted(s) == sorted(t)
    

        
# # Seventh Solution using counter
# """
# [Not the most efficient solution, but a good one]

# Returns True if the character counts in both strings are equal, indicating they are anagrams.
# Returns False if the character counts differ, indicating they are not anagrams.
        
# """
# from collections import Counter
# class Solution5:
#     def isAnagram(self, s: str, t: str) -> bool:
#         """
#         :type s: str
#         :type t: str
#         :rtype: bool
#         """
#         # Use Counter to count the frequency of characters in both strings
#         return Counter(s) == Counter(t)


#  Provide me 2 test cases to validate the solution
# Test cases for the isAnagram function
def test():
    solution = Solution()
    assert solution.isAnagram("anagram", "nagaram") == True, "Test Case 1 Failed"
    assert solution.isAnagram("rat", "car") == False, "Test Case 2 Failed"
    assert solution.isAnagram("listen", "silent") == True, "Test Case 3 Failed"
    assert solution.isAnagram("hello", "world") == False, "Test Case 4 Failed"
    assert solution.isAnagram("", "") == True, "Test Case 5 Failed"  # Edge case: both strings are empty
    return "All test cases passed!"

if __name__ == "__main__":
    v = test()  # Run the test cases
    print(v)  # Output: All test cases passed!
    


