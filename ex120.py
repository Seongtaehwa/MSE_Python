#!/usr/bin/env python
# coding: utf-8

# In[ ]:


fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}


# In[ ]:


user = input("좋아하는 과일은?") #input함수로 어떠한 값을 받음
if user in fruit.values(): #values()를 사용하여 if문 사용
    print("정답입니다.") #fruit이 values()에 들어가면 "정답입니다."를 출력
else:
    print("오답입니다.") #들어가지 않는다면 "오답입니다."를 출력

