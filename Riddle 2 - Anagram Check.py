#!/usr/bin/env python
# coding: utf-8

# ## Given two strings, check to see if they are anagrams. An anagram is when the two strings can be written using the exact same letters (so you can just rearrange the letters to get a different phrase or word).

# In[1]:


def anagram(s1, s2):
    s1 = s1.lower().replace(" ", "")
    s2 = s2.lower().replace(" ", "")

    # Check if the lengths of the strings are equal
    if len(s1) != len(s2):
        return False

    # Create dictionaries to count character occurrences
    char_count_s1 = {}
    char_count_s2 = {}

    # Count occurrences of characters in s1
    for char in s1:
        char_count_s1[char] = char_count_s1.get(char, 0) + 1

    # Count occurrences of characters in s2
    for char in s2:
        char_count_s2[char] = char_count_s2.get(char, 0) + 1

    # Check if the character counts are equal
    return char_count_s1 == char_count_s2


# In[2]:


anagram('Halsey','Ashley')


# ###### The End
