# Question:
""" 
Given a stream of numbers, select a random number from the stream with equal probability and O(1) space in selection.
Note:
1. x is the new value from the stream.
2. y is the previously selected value.
3. count is the size of the stream.
"""

# Solution:

import random

# A function to randomly select an item 
# from stream[0], stream[1], .. stream[i-1] 
def random_number(x, y=0, count=1):
    # x is the new value
    # y is the old value, default 0
    
    # If this is the first element 
    # from stream, return it 
    if (count == 1): 
        res = x; 
    else: 
        
        # Generate a random number 
        # from 0 to count - 1 
        rnd = random.randrange(count); 

        # Replace the prev random number 
        # with new number with 1/count 
        # probability 
        if (rnd == count - 1): 
            res = x
        else: 
            res = y
    return res

