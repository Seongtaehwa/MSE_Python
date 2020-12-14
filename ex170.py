#!/usr/bin/env python
# coding: utf-8

# In[7]:


result = 1 #변수 result의 초기값을 1로 지정


# In[8]:


for i in range(1, 11) : #1부터 11전까지(10) i 의 범위를 정함
    result *= i #result = result * i
    #오른쪽 result에 i를 곱한 값이 왼쪽 result
    #i가 10이 될 때까지 반복
print(result) #result값 출력

