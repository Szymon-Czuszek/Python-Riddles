#!/usr/bin/env python
# coding: utf-8

# ## Given a string in the form 'AAAA' compress it to become 'A4'.

# In[1]:


def compress_string(s):
    compressed_string = ""
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            compressed_string += s[i - 1] + str(count)
            count = 1

    compressed_string += s[-1] + str(count)

    return compressed_string


# In[3]:


compress_string('AAAABBBBCCCCCDDEEEE')


# ###### The End
