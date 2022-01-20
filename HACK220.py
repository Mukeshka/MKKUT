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

expirydate = datetime.date(2022,  1, 30 )
#expirydate = datetime.date(2021, 12, 30)
today=date.today()
green="\033[3;32m"
neon="\033[3;36m"
nc="\033[00m"
red="\033[3;31m"
purple="\033[3;34m"
yellow="\033[3;33m"
voilet="\033[3;35m"
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
    banner='figlet RXCE8.1|lolcat'
    thisway=[2,6,8,11,12,15,16,18,19,20]
    thatway=[1,3,4,5,7,9,10,14,13,17]
    numbers=[]
    i=1
    while(y):
        clear()
        system(banner)
        print("Contact me on telegram @hackmgk")
        print(f"{yellow}Enter ",newperiod," Price :")
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
                    print(newperiod+1," : 💥🟢GREEN1🟢💥")
                else:
                    print(newperiod+1," : 💥🔴RED2🔴💥")
            else:
                if current in numbers:
                    print(newperiod+1," :  💥🔴RED2🔴💥")
                else:
                    print(newperiod+1," : 💥🟢GREEN1🟢💥")
        if i in thatway:
            m=getSum(current)+1
            n=int(current)%10
            if((m%2==0 and n%2==0) or (m%2==1 and n%2==1)):
                if current in numbers:
                    print(newperiod+1,": 💥💥🟢GREEN2🟢💥💥")
                else:
                    print(newperiod+1,": 💥💥🔴RED6🔴💥💥")
            else:
                if current in numbers:
                    print(newperiod+1,": 💥💥🔴RED4🔴💥💥")
                else:
                    print(newperiod+1,": 💥💥🟢GREEN4🟢💥💥")
        i=i+1
        newperiod+=1
        numbers.append(current)
        y=input("Do you want to play : Press 1 and 0 to exit \n")
        if(y==0):
            y=False
        if (len(numbers)>15):
            clear()
            system('figlet Thank you!!')
            print("Play on next specified time!!")
            print("-----------Current Time UP----------")
            sys.exit(" \n \n \n Contact on Telegram @Hackmgk")
            print(numbers)
  



if(expirydate>today):
    now = datetime.datetime.now()
    First = now.replace(hour=10, minute=55, second=0, microsecond=0)
    Firstend = now.replace(hour=11, minute=35, second=0, microsecond=0)
    Second = now.replace(hour=13, minute=55, second=0, microsecond=0)
    Secondend = now.replace(hour=14, minute=35, second=0, microsecond=0)
    Third = now.replace(hour=16, minute=55, second=0, microsecond=0)
    Thirdend = now.replace(hour=17, minute=35, second=0, microsecond=0)
    Final = now.replace(hour=20, minute=55, second=0, microsecond=0)
    Finalend = now.replace(hour=21, minute=35, second=0, microsecond= 0)
    FFinal = now.replace(hour=22, minute=55, second=0, microsecond= 0)
    FFinalend = now.replace(hour=23, minute=35, second=0, microsecond= 0)

    if (now>First and now<Firstend):
            period=220
            hero()
    elif(now>Second and now<Secondend):
            period=280
            hero()
    elif(now>Third and now<Thirdend):
            period=340
            hero()
    elif(now>Final and now<Finalend):
            period=420
            hero()
    elif(now>FFinal and now<FFinalend):
            period=460
            hero()
    else:
        banner='figlet RXCE8.1|lolcat'
        print("Hi!! Thanks for buying Life time the hack")
        print("----------Your play time-----------")
        print("30th JAN 2022, 11:00 PM- 11:35 PM")
        print("30th JAN 2022, 02:00 PM- 02:35 PM")
        print("30th JAN 2022, 05:00 PM- 05:35 PM")
        print("30th JAN 2022, 09:00 PM- 09:35 PM")
        print("30th JAN 2022, 11:00 PM- 12:35 PM")
        print("Please play on the given time, and ")
        print("If you think it is an error contact")
        print(" admin on telegram @Hackmgk ")
 

else:
    def clear():
        # for windows
        if name == 'nt':
            _ = system('cls')
        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')
    code="BART983"
    test="PBHGY32"
    night="NICMJY13"
    nextday="NNMKJHFD"
    banner='figlet RXCEV2.1|lolcat'
    rava=0
    now = datetime.datetime.now()
    Second = now.replace(hour=10, minute=55, second=0, microsecond=0)
    Secondend = now.replace(hour=14, minute=55, second=0, microsecond=0)
    Third = now.replace(hour=15, minute=30, second=0, microsecond=0)
    Thirdend = now.replace(hour=18, minute=34, second=0, microsecond=0)
    Final = now.replace(hour=18, minute=35, second=0, microsecond=0)
    Finalend = now.replace(hour=22, minute=35, second=0, microsecond=0)

    if(now>Second and now<Secondend):
            rava=290
    elif(now>Third and now<Thirdend):
            rava=350
    elif(now>Final and now<Finalend):
            rava=410
    system(banner)
    print(f"{neon}*--------*--------*-------*---------*---------*")
    print("Your hack has expired--- Please contact")
    print(" on telegram ----@hackmgk for activating")
    print("     Plan Amount --    Total limit " )
    print(" 1.  500 INR -------  10 Day (30 Games")
    print(" 2.  1500 INR ------- 20 Days(90 Games")
    print(" 2.  3000 INR ------- 30 Days(210 Games")
    print("*---------*----------*-------------*----------*")
    print("If you need any discount contact me")
    print("Beware of fraudsters!!!")
    while(True):
        print("My banking name is MUKESH")
        print(f"{red}After You Pay to The UPI ID above You Can Automatically")
        print(f"Activate Hack By Entering The Correct ")
        print(f"{green}(UTR) Or Upi Reference Number") 
        print(f"{neon}To Activate The Hack")
        print(f"If It Does'nt Open Contact Me On Telegram {yellow}@hackmgk")
        print(f"{neon}*---------*----------*-------------*----------*")
        print(f"{red}*---------*----------*-------------*----------*")
        print("payhere--- UPI : ")
        print(f"{yellow}UPI1 : mkeditor778@ybl")
        print("UPI2 :  mkeditor778@axl")
        print("If you have already paid to above UPI")
        print(f"{neon}Enter Your Activation Code Or Upi Reference for Opening Hack")
        bhai=input(": ")
        if(bhai==code or bhai==test):
            clear()
            print(f"{purple}---------------Your play time----------------")
              
            print("02:00 PM- 02:30 PM")
            print("05:00 PM- 05:30 PM")
            print("08:00 PM- 08:30 PM")
            print("Please play on the given time, and ")
            print(f"If you think it is an {red}error {yellow}contact {green}me ")
            print(f"{neon}On Telegram {red}@hackmgk")
            print("wait.... starting....")
            time.sleep(20)
            period=rava
            hero()
            #print("Today Server is off RXCE try tomorrow ")
            #rint(" of town, Tomorrow It will work as usual.")
            #print(" Thank You!!")
            #rint("To all the weekly members next week, cost will be  ")
            #print(" 4000 INR , because in this week 2 days off " )
            #print("Thank You!! ")
            sys.exit(" \n \n \n Contact on Telegram @hackmgk")
        elif(bhai==nextday):
            clear()
            banner='figlet RXCEV2.1|lolcat'
            system(banner)
            print("----------Your play time-----------")
            print("30th JAN,2022 02:00 PM- 02:30 PM")
            print("30th JAN,2022 05:00 PM- 05:30 PM")
            print("30th JAN,2022 08:00 PM- 08:30 PM")
            print("Please play on the given time, and ")
            print("If you think it is an error contact")
            print("wait.... starting....")
            time.sleep(20)
            period=rava
            hero()
            #period("Sorry too many people(>20) using hack in same time ")
            sys.exit(" \n \n \n Contact on Telegram @hackmgk")
        elif(bhai==night):
            clear()
            print("----------Your play time-----------")
            print("30th JAN,2022 11:00 PM- 11:30 PM")
            print("30th JAN,2022 08:00 PM- 08:30 PM")
            print("30th JAN,2022 08:30 PM- 09:00 PM")
            print("Please play on the given time, and ")
            print("If you think it is an error contact")
            print("wait.... starting....")
            time.sleep(20)
            period=410
            hero()
            sys.exit(" \n \n \n Contact on Telegram @hackmgk")
        else:
            clear()
            banner='figlet RXCEV2.1|lolcat'
            system(banner)
            print("Incorrect Activation Code :")
     
