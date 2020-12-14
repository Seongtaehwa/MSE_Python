#!/usr/bin/env python
# coding: utf-8

# In[5]:


def my_print (a, b) :
    print("왼쪽:", a) #왼쪽: 이라 입력된 a를 출력
    print("오른쪽:", b) #오른쪽: 이라 입력된 b를 출력

my_print(b=100, a=200) 
#a와 b의 순서가 바뀌어도 def함수에서 200과 100을 대입하라 하였으므로 
#순서와 상관없이 a자리에 200, b자리에 100이 대입

