
# Solution1: Using Counter from collections
from collections import Counter
def first_uniq_char(s):
    freq = Counter(s)
    for i, c in enumerate(s):
        if freq[c] == 1:
            return i
    return -1

# test = first_uniq_char("leetcode")
# test = first_uniq_char("lleettccoodde")
# print(test)  # Output: 0


# Solution2: without using Counter
def first_non_repeating_char(s: str) -> int:
    char_count = {}

# Calculate the frequency of each character in the string
    for i in s:
        if i in char_count:
            char_count[i] = char_count.get(i, 0) + 1
        else:
            char_count[i] = 1

# Iterate through the string to find the first non-repeating character
    for i in range(len(s)):
        if char_count[s[i]] == 1:
            return i
    return -1  # Return -1 if no non-repeating character is found

# Test the function
test = first_non_repeating_char("lleettccoodde")
print(test)  # Output: -1 (since all characters repeat)


    

