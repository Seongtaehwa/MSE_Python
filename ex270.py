#!/usr/bin/env python
# coding: utf-8

# In[16]:


class Stock: #stock이라는 클래스를 생성
    def __init__(self, name, code, per, pbr, dividend):
        self.name = name  # self.name에 클래스의 name을 대입
        self.code = code  # self.code에 클래스의 code를 대입
        self.per = per  # self.per에 클래스의 per을 대입
        self.pbr = pbr  # self.pbr에 클래스의 pbr을 대입
        self.dividend = dividend # self.dividend에 클래스의 dividend를 대입


# In[17]:


종목 = [] #종목이라는 리스트를 생성

삼성 = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
현대차 = Stock("현대차", "005380", 8.70, 0.35, 4.27)
LG전자 = Stock("LG전자", "066570", 317.34, 0.69, 1.37)
# stock 클래스에 각각의 객체를 생성

종목.append(삼성)
종목.append(현대차)
종목.append(LG전자)
#아까만든 종목이라는 리스트에 위에 객체들을 대입

for i in 종목: #i에 종목(삼성,현대차,LG전자)을 대입
    print(i.code, i.per) #i에 code와 per을 출력

