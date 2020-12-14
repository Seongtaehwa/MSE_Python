#!/usr/bin/env python
# coding: utf-8

# In[4]:


def print_max(a, b, c) :
    max_val = 0  #max_val의 초기값을 0으로 지정
    if a > max_val : #a가 0보다 크면 실행
        max_val = a  #max_val의 초기값을 a로 지정
    if b > max_val : #b가 a보다 크면 실행
        max_val = b  #max_val의 초기값을 b로 지정
    if c > max_val : #c가 b보다 크면 실행
        max_val = c  #max_val의 초기값을 c로 지정
    print(max_val)   #max_val을 출력
    
print_max(10,150,300) #3개의 숫자중 가장 큰값인 300 출력

