#!/usr/bin/env python
# coding: utf-8

# ## Consider an array of non-negative integers. A second array is formed by shuffling the elements of the first array and deleting a random element. Given these two arrays, find which element is missing in the second array.

# In[1]:


from collections import Counter

def finder(arr1, arr2):
    """
    Finds the missing element in arr2 compared to arr1.

    Args:
    - arr1 (list): First input array
    - arr2 (list): Second input array

    Returns:
    - Any: The missing element if found, None otherwise
    """
    count = Counter(arr1)

    for item in arr2:
        count[item] -= 1

    # Find the element with a count that isn't zero
    for key, value in count.items():
        if value != 0:
            return key

    # Check if arr2 is shorter by one element
    if len(arr1) > len(arr2):
        for key, value in count.items():
            if value == -1:
                return key

    # Handle scenarios where the missing element is not found
    return None


# In[2]:


finder([1, 2, 3, 4, 5, 6, 7], [3, 7, 2, 1, 4, 6])


# ###### The End
