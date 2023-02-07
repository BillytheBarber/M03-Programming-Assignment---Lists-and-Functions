#!/usr/bin/env python
# coding: utf-8

# In[55]:


# 7.4 Make a list called things with these three strings as elements: "mozzarella", "cinderella", "salmonella".

things = ['mozzarella', 'cinderalla', 'salmonella']


# In[56]:


# 7.5 Capitalize the element in things that refers to a person and then print the list. Did it change the element in the list?

things[1] = things[1].title()
print(things)

#Yes it change the second element


# In[59]:


# 7.6 Make the cheesy element of things all uppercase and then print the list.

things[0] = things[0].upper()
print(things)


# In[60]:


# 7.7 Delete the disease element from things, collect your Nobel Prize, and print the list.

del things[2]
print(things)


# In[64]:


# 9.1 Define a function called good() that returns the following list: ['Harry', 'Ron', 'Hermione'].

def good():
    return ['Harry', 'Ron', 'Hermione']


# In[99]:


# 9.2 Define a generator function called get_odds() that returns the odd numbers from range(10). Use a for loop to find and print the third value returned.


def get_odds():
    x = 0
    for num in range(0,10):
        if num % 2 != 0:
            if x == 3:
                return print(num)
            else:
                x += 1
        else:
            pass

get_odds()


# In[ ]:




