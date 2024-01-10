#!/usr/bin/env python
# coding: utf-8

# ## Given an integer array, output all the * *unique ** pairs that sum up to a specific value k.

# In[1]:


def pair_sum(arr, k):
    """
    Find unique pairs in the given array whose sum equals the specified target value.

    Args:
    - arr (list of int): The input array containing integers.
    - k (int): The target sum value.

    Returns:
    - list of tuples: A list of unique pairs (tuple) whose sum equals the target value 'k'.
    
    The function iterates through the input array, searching for pairs whose sum equals the target value 'k'.
    It stores unique pairs in a set and returns a list containing these unique pairs.
    Pairs are sorted to maintain consistency in the result (smaller number first).
    """
    seen = set()  # Store unique pairs
    result = set()  # Store final unique pairs to return

    for num in arr:
        complement = k - num
        if complement in seen:
            # Sort the pair to maintain consistency
            pair = (min(num, complement), max(num, complement))
            result.add(pair)
        seen.add(num)

    return list(result)


# In[2]:


pair_sum([1, 3, 2, 2], 4)


# ###### The End
