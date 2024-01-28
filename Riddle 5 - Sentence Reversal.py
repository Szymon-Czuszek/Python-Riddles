#!/usr/bin/env python
# coding: utf-8

# ## Given a string of words, reverse all the words.

# In[1]:


def rev_word(s):
    return " ".join(reversed(s.split()))


# In[2]:


result = rev_word('Żaba skacze nad leniwym stawem')
print(result)


# ###### The End
