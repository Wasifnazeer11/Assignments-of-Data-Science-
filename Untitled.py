#!/usr/bin/env python
# coding: utf-8

# In[34]:


print ("Assalmualikum sir")


# In[33]:


def full_name(x):
  return x[::-1]
first_name = input("Enter your first name")
Last_name = input("Enter your last name")
mytxt = full_name(first_name + Last_name)

print(mytxt)


# In[36]:


pi = 3.14 
value = float(input("Enter the radius of circle"))
area = pi * value * value
print ("the area of the circle is = %.1f" %area)


# In[ ]:


from platform import python_version
print(python_version())


# In[ ]:


import time;

localtime = time.asctime( time.localtime(time.time()) )
print ("Local current time :", localtime)


# In[ ]:


print ("Twinkle, twinkle, little star, \n \t How I wonder what you are.")
print ("\t \t Up above the world so high, \n \t \t  Like a diamond in the sky  ")
print ("Twinkle, twinkle, little star, \n \t How I wonder what you are.")
 


# In[ ]:


first_name = input("Enter your first name")
Last_name = input("Enter your last name")
full_name = first_name + Last_name
print (full_name)


# In[ ]:





# In[ ]:




