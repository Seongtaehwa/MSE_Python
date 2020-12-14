#!/usr/bin/env python
# coding: utf-8

# In[5]:


per = ["10.31", "", "8.00"]

for i in per: #per원소를 i에 대입
    try: #실행코드
        print(float(i))
    except: #예외가 발생 할 경우
        print(0) #0을 출력
    else: #예외가 발생하지 않을 경우
        print("clean data") #clean data출력
    finally: #에외 발생 여부와 상관없이
        print("변환 완료") #변환 완료 출력
        
#1. 10.31 출력
#예외가 발생하지 않았으므로 "clean data"출력
#발생여부 상관없이 "변환 완료" 출력
#2. ""이라는 예외 발생
#예외가 발생했으니 "0"을 출력
#발생여부 상관없이 "변환 완료" 출력
#3. 8.0 출력
#예외가 발생하지 않았으므로 "clean data"출력
#발생여부와 상관없이 "변환 완료" 출력

