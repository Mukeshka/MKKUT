#!/usr/bin/python
# -*- coding: UTF-8 -*-

from os import system, name
import itertools
import threading
import time
import sys
import datetime
from base64 import b64decode,b64encode
from datetime import date

expirydate = datetime.date(2022,  2, 25 )
#expirydate = datetime.date(2021, 12, 30)
today=date.today()
def hero():

    def chalo():
        done = False
        #here is the animation
        def animate():
            for c in itertools.cycle(['|', '/', '-', '\\']) :
                if done:
                    break
                sys.stdout.write('\rconnecting to server for next colour--------- ' + c)
                sys.stdout.flush()
                time.sleep(0.1)
            sys.stdout.write('\rDone!     ')

        t = threading.Thread(target=animate)
        t.start()

        #long process here
        time.sleep(20)
        done = True

    def chalo1():
        done = False
        #here is the animation
        def animate():
            for c in itertools.cycle(['|', '/', '-', '\\']):
                if done:
                    break
                sys.stdout.write('\rgetting the colour wait --------- ' + c)
                sys.stdout.flush()
                time.sleep(0.1)
            sys.stdout.write('\rDone!     ')

        t = threading.Thread(target=animate)
        t.start()

        #long process here
        time.sleep(20)
        done = True

    def clear():
        # for windows
        if name == 'nt':
            _ = system('cls')
        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')

    clear()
    y=1
    newperiod=period
    banner='figlet RXCE 7.o'
    thisway=[2,6,8,11,12,15,16,18,19,20]
    thatway=[1,3,4,5,7,9,10,14,13,17]
    numbers=[]
    i=1
    while(y):
        clear()
        system(banner)
        print("Contact me on telegram @Hackmgk")
        print("Enter" ,newperiod,"Price :")
        current=input()
        current=int(current)
        chalo()
        print("\n---------Successfully Connected to the server-----------")
        chalo1()
        print("\n---------Successfully got the colour -------------")
        print('\n')
        def getSum(n):
            sum=0
            for digit in str(n):
                sum += int(digit)
            return sum
        if i in thisway:
            m=getSum(current)
            n=int(current)%10
            if((m%2==0 and n%2==0) or (m%2==1 and n%2==1)):
                if current in numbers:
                    print(newperiod+1," : 💥🟢GREEN🟢💥")
                else:
                    print(newperiod+1," : 💥🔴RED🔴💥")
            else:
                if current in numbers:
                    print(newperiod+1," :  💥🔴RED🔴💥")
                else:
                    print(newperiod+1," : 💥🟢GREEN🟢💥")
        if i in thatway:
            m=getSum(current)+1
            n=int(current)%10
            if((m%2==0 and n%2==0) or (m%2==1 and n%2==1)):
                if current in numbers:
                    print(newperiod+1,": 💥💥🔴RED🔴💥💥")
                else:
                    print(newperiod+1,": 💥💥🟢GREEN🟢💥💥")
            else:
                if current in numbers:
                    print(newperiod+1,": 💥💥🟢GREEN🟢💥💥")
                else:
                    print(newperiod+1,": 💥💥🔴RED🔴💥💥")
        i=i+1
        newperiod+=1
        numbers.append(current)
        y=input("Do you want to play : Press 1 and 0 to exit \n")
        if(y==0):
            y=False
        if (len(numbers)>12):
            clear()
            system('figlet Thank you!!')
            print("Play on next specified time!!")
            print("-----------Current Time UP----------")
            sys.exit(" \n \n \n Contact on Telegram @Hackmgk")
            print(numbers)
  



if(expirydate>today):
    now = datetime.datetime.now()
    First = now.replace(hour=9, minute=55, second=0, microsecond=0)
    Firstend = now.replace(hour=10, minute=35, second=0, microsecond=0)
    Second = now.replace(hour=15, minute=55, second=0, microsecond=0)
    Secondend = now.replace(hour=16, minute=18, second=0, microsecond=0)
    Third = now.replace(hour=18, minute=55, second=0, microsecond=0)
    Thirdend = now.replace(hour=19, minute=18, second=0, microsecond=0)
    Final = now.replace(hour=20, minute=55, second=0, microsecond=0)
    Finalend = now.replace(hour=21, minute=18, second=0, microsecond= 0)
    FFinal = now.replace(hour=22, minute=55, second=0, microsecond= 0)
    FFinalend = now.replace(hour=23, minute=18, second=0, microsecond= 0)

    if (now>First and now<Firstend):
            period=200
            hero()
    elif(now>Second and now<Secondend):
            period=320
            hero()
    elif(now>Third and now<Thirdend):
            period=380
            hero()
    elif(now>Final and now<Finalend):
            period=420
            hero()
    elif(now>FFinal and now<FFinalend):
            period=460
            hero()
    else:
        banner='figlet Rxce 7.o '
        print("Hi!! Thanks for watching our video")
        print("----------Your play time-----------")
        print(" 10:00 PM- 10:35 PM")
        print(" 04:00 PM- 04:15 PM")
        print(" 07:00 PM- 07:15 PM")
        print(" 09:00 PM- 09:15 PM")
        print(" 11:00 PM- 11:15 PM")
        print("Please play on the given time, and ")
        print("If you think it is an error contact")
        print(" admin on telegram @Hackmgk ")
else:
    banner='figlet Thank '
    system(banner)
    print("*---------*----------*-------------*----------*")
    print("Your hack has expired--- Please contact")
    print(" on telegram ----@Hackmgk for activating")
    print(" Recharge Amount :        Total limit " )
    print(" 2.     700 INR -------  7 Days")
    print("*---------*----------*-------------*----------*")
    print("Your custom hack can be made request from us.")
    print( "Msg me on telegram @Hackmgk")
