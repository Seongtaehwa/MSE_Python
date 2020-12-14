#!/usr/bin/env python
# coding: utf-8

# In[5]:


import random #무작위로 계좌번호를 만들기 위해 random을 import

class Account: #Account 클래스 생성
    # class variable
    account_count = 0 #계좌의 갯수 account_count를 0으로 지정
    def __init__(self, name, balance):
        self.deposit_count = 0 # 입금횟수를 0으로 지정
        self.deposit_log = [] #리스트 생성
        self.withdraw_log = [] #리스트 생성
        
        self.name = name
        self.balance = balance
        self.bank = "SC은행" #self안에 변수들을 생성
        
        num1 = random.randint(0, 999) #랜덤으로 3자리 생성
        num2 = random.randint(0, 99)  #랜덤으로 2자리 생성
        num3 = random.randint(0, 999999) #랜덤으로 6자리 생성

        num1 = str(num1).zfill(3)  # 정수값에서 문자열로 변경 후 zfill로 3자리 생성
        num2 = str(num2).zfill(2)  # 정수값에서 문자열로 변경 후 zfill로 2자리 생성
        num3 = str(num3).zfill(6)  # 정수값에서 문자열로 변경 후 zfill로 6자리 생성
        self.account_number = num1 + '-' + num2 + '-' + num3  # 3자리-2자리-6자리 숫자를 랜덤으로 생성
        Account.account_count += 1 # 계좌 생성시 1 증가
        
    @classmethod #객체에 접근 할 필요가 없으므로 @classmethod사용
    def get_account_num(cls): #account 클래스에 계좌의 갯수인 account_count 추가
        print(cls.account_count)  # Account.account_count

    def deposit(self, amount):
        if amount >= 1: #amount가 1 이상이면
            self.deposit_log.append(amount) #입금내역기록을 리스트에 저장
            self.balance += amount #amount만큼 잔고에 +

            self.deposit_count += 1 #deposit_count값을 1 증가
            if self.deposit_count % 5 == 0: #5의 배수
                self.balance = (self.balance * 1.01) #입금이 5회가 될때 1%이자 잔고를 추가
                
    def withdraw(self, amount):
        if self.balance > amount: #출금액이 잔고보다 적을때
            self.withdraw_log.append(amount) #출금이 될때 리스트에 저장
            self.balance -= amount #출금액만큼 잔고에서 -

    def display_info(self): #계좌의 정보
        print("은행이름: ", self.bank) #은행이름 출력
        print("예금주: ", self.name) #예금주 출력
        print("계좌번호: ", self.account_number) #계좌번호 출력
        print("잔고: ", self.balance) #잔고 출력
 
    def withdraw_history(self):
        for amount in self.withdraw_log:
            print(amount) #출금내역 출력

    def deposit_history(self):
        for amount in self.deposit_log:
            print(amount) #입금내역 출력
            
k = Account("Kim", 1000) #kim씨가 1000원 입금
k.deposit(100) #100원 입금
k.deposit(200) #200원 입금
k.deposit(300) #300원 입금
k.deposit_history() #입금 금액 출력

k.withdraw(100) #100원 출금
k.withdraw(200) #200원 출금
k.withdraw_history() #출금 금액 출력

