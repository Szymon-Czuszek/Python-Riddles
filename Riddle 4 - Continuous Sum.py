#!/usr/bin/env python
# coding: utf-8

# ## Given an array of integers (positive and negative) find the largest continuous sum.

# In[1]:


def large_cont_sum(arr):
    """
    Find the largest sum of a contiguous subarray within the given array.

    Args:
    - arr (list of int): The input array containing positive and negative integers.

    Returns:
    - int: The largest sum of a contiguous subarray.
    
    The function iterates through the array while keeping track of the current sum and the maximum sum encountered.
    It returns the maximum sum found within any contiguous subarray in the input array.
    """
    if len(arr) == 0:
        return 0
    
    max_sum = current_sum = arr[0]
    
    for num in arr[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    
    return max_sum


# In[2]:


large_cont_sum([1, 2, -1, 3, 4, -1])


# ###### The End
