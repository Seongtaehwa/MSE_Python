#!/usr/bin/env python
# coding: utf-8

# In[6]:


date = ['09/05', '09/06', '09/07', '09/08', '09/09']


# In[7]:


close_price = [10500, 10300, 10100, 10800, 11000]


# In[8]:


close_table = dict(zip(date, close_price))


# In[9]:


#zip()으로 data와 close_price의 원소를 묶는다


# In[10]:


#dict()로 값을 딕셔너리로 만든 후 close_table에 대입


# In[11]:


print(close_table)


# In[12]:


#close_table값을 출력

