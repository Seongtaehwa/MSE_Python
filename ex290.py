#!/usr/bin/env python
# coding: utf-8

# In[5]:


class 부모: #부모라는 class를 생성
    def __init__(self): #생성자
        print("부모생성")

class 자식(부모): #자식이라는 class를 생성
    #자식class는 부모를 상속받음
    def __init__(self): #생성자
        print("자식생성")
        super().__init__() #super()로 부모class에 접근
        #부모class에 있는 생성자를 호출
        
나 = 자식() #자식class에 나 라는 객체를 생성
#자식class생성자 호출 후 출력
#그 다음 부모class생성차 호출 후 출력 이므로
#자식생성 부모생성이 출력

