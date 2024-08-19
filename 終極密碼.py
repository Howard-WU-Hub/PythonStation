# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 00:22:49 2024

@author: user
"""
import random

guess=0
count=1
minvalue = 1
maxvalue = 100  
ans=random.randint(minvalue,maxvalue)

#當count>5就要離開,在判斷是否猜對的才離開 

while ans != guess and count <=5 :
    guess = int(input("請輸入"+str(minvalue)+"~"+str(maxvalue)+"整數:"))
    if guess >=     minvalue and guess <=maxvalue:
        if guess > ans:
            maxvalue = guess
            print(minvalue, "至" ,maxvalue)
        elif guess < ans:
            minvalue = guess
            print(minvalue, "至" ,maxvalue)
        count +=1   
    else:
        print("請輸入",minvalue," 至 ",maxvalue ," 之間 " )
if ans == guess:
    print("猜對了")
else:
    print("答案是: ",ans)
    print("猜錯了,次數已滿")       
