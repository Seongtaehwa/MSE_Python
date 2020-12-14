#!/usr/bin/env python
# coding: utf-8

# In[4]:


apart = [ [101, 102], [201, 202], [301, 302] ]


# In[5]:


for row in apart: #row는 층 
    #층에 대한 for문을 생성
    for col in row: #col은 호수
    #층안에 호수에 대한 for문을 생성
        print(col, "호") #호수 + 호 를 출력
print("-" * 5) #마지막줄에 "-"5개를 출력

