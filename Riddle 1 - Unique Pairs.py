#!/usr/bin/env python
# coding: utf-8

# ## Given an integer array, output all the * *unique ** pairs that sum up to a specific value k.

# In[1]:


def pair_sum(arr, k):
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
