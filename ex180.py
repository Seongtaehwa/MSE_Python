#!/usr/bin/env python
# coding: utf-8

# In[11]:


low_prices  = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]


# In[12]:


volatility = [] #리스트를 하나 생성


# In[13]:


for i in range(len(low_prices)) :  #low_price 리스트에 있는 값들을 i에 대입
    #low_price의 길이(5)만큼을 실행
    volatility.append(high_prices[i] - low_prices[i]) #volatility에 변동값(high_prices - low_prices)을 추가


# In[14]:


print(volatility) #변동값을 출력

