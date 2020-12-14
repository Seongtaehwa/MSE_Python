#!/usr/bin/env python
# coding: utf-8

# In[6]:


리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']


# In[7]:


for 변수 in 리스트: #리스트를 변수로 지정 후 하나씩 출력
    split = 변수.split(".") #split()를 사용해 "."을 두고 문자열을 나눔
    if (split[1] == "h") or (split[1] == "c"): #"."뒤의 문자가 "h"와 "c" 이면 if를 실행
        print(변수) #변수값 출력

