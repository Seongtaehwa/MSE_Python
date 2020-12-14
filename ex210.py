#!/usr/bin/env python
# coding: utf-8

# In[2]:


def message1(): #message1()은
    print("A")  #A가 출력

def message2(): #message2()는
    print("B")  #B가 출력

def message3():
    for i in range (3) :  #for문으로 3번반복
        message2() #message2인 B를 출력
        print("C") #그다음 C출력
    message1()     #for문이 끝나므로 BC를 3번씩 출력하고 message1()인 A출력

message3()         #결과적으로 BCBCBCA 출력

