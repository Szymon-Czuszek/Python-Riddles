#!/usr/bin/env python
# coding: utf-8

# ## Given a string,determine if it is compreised of all unique characters.

# In[1]:


def has_unique_characters(s):
    character_set = set()

    for char in s:
        if char in character_set:
            return False
        else:
            character_set.add(char)

    return True


# In[2]:


# Test the function without creating separate variables
print(has_unique_characters('abcde'))  # Should print True
print(has_unique_characters('aabcde'))  # Should print False


# ###### The End
