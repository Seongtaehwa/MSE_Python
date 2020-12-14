#!/usr/bin/env python
# coding: utf-8

# In[18]:


if True : #참이면 실행
     if False : #참이 아니므로 1,2 를 출력하지 않고 else로 넘어감
        print("1")
        print("2")
     else :
        print("3") #3을 출력
else :
    print("4") #if에서 값이 나왔으므로 출력하지 않음
print("5") #위와 상관없이 5를 출력
# 결과적으로 3,5가 출력

