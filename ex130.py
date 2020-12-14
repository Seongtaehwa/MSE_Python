#!/usr/bin/env python
# coding: utf-8

# In[6]:


import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']
#btc의 가격 정보를 딕셔너리로 가져오는 코드
#requests를 통해 서버에 요청


# In[7]:


변동폭 = float(btc['max_price']) - float(btc['min_price'])
#btc값이 문자열이므로 float을 이용하여 소숫점이 있는 숫자로 바꿈
#변동폭 = [최근 24시간 내 최고 거래금액] - [최근 24시간 내 최저 거래금액]


# In[8]:


시가 = float(btc['opening_price'])
#시가 = 최근 24시간 내 시작 거래금액


# In[9]:


최고가 = float(btc['max_price'])


# In[10]:


if (시가+변동폭) > 최고가:
    print("상승장") #(시가+변동폭) 이 최고가 보다 크면 if를 실행
else:
    print("하락장") #그렇지 않으면 else를 실행

