#!/usr/bin/env python
# coding: utf-8

# In[4]:


def 함수0(num) : #함수0이 num을 받으면
    return num * 2 #num값에 2를 곱해 리턴

def 함수1(num) : #함수1이 num을 받으면 .
    return 함수0(num + 2) #함수0(num에 2를 더해)을 리턴

def 함수2(num) : #함수2가 num을 받으면 
    num = num + 10 #num = num + 10인 새로운 num을 갖고
    return 함수1(num) #함수1(num)을 리턴

c = 함수2(2) #함수2가 (num=2)를 가짐으로
#num+10이므로 2+10 = 12
#함수1이 12라는 값을 가짐으로
#num+2이므로 12+2 = 14
#함수0은 14라는 값을 가짐으로 
#num*2이므로 14*2 = 28
print(c) #c의 값을 출력

