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


expirydate = datetime.date(2022, 3, 18)
#expirydate = datetime.date(2021, 8, 30)
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
                sys.stdout.write('\rhacking in the parity server for next colour--------- ' + c)
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
    def getSum(n):
        sum=0
        for digit in str(n):
            sum+= int(digit)
        return sum
    clear()
    y=1
    newperiod=period
    banner='figlet RXCEV2.1|lolcat'
    numbers=[]
    while(y):
        clear()
        system(banner)
        print(f"{red}Contact me on telegram @HACKMGK")
        print(f"{yellow}Enter ",newperiod," Parity Price :")
        current=input()
        current=int(current)
        chalo()
        print("\n---------Successfully hacked the server-----------")
        chalo1()
        print("\n---------Successfully got the colour -------------")
        print('\n')
        last2=str(current)[-2:]
        #samjha_maadarchod=lawde_time_pe_khel(last2)
        if(newperiod%2==0):
            sum=getSum(current)
            if(sum%2==0):
                print(newperiod+1," : 🔴, RED")
            else:
                print(newperiod+1,"  : 🟢, GREEN")
        else:
            sum=getSum(current)
            if(sum%2==0):
                print(newperiod+1,"   : 🔴, RED")
            else:
                print(newperiod+1,"   : 🟢, GREEN")
        newperiod+=1
        numbers.append(current)
        y=input("Do you want to play : Press 1 and 0 to exit \n")
        if(y==0):
            y=False
        if (len(numbers)>11):
            clear()
            system('figlet Thank you!!')
            print("Play on next specified time!!")
            print("-----------Current Time UP----------")
            sys.exit(" \n \n \n Contact on Telegram @HACKMGK")
            print(numbers)
  



if(expirydate>today):
    now = datetime.datetime.now()
    First = now.replace(hour=13, minute=55, second=0, microsecond=0)
    Firstend = now.replace(hour=14, minute=35, second=0, microsecond=0)
    Second = now.replace(hour=16, minute=25, second=0, microsecond=0)
    Secondend = now.replace(hour=17, minute=35, second=0, microsecond=0)
    Third = now.replace(hour=15, minute=55, second=0, microsecond=0)
    Thirdend = now.replace(hour=16, minute=35, second=0, microsecond=0)
    Final = now.replace(hour=17, minute=55, second=0, microsecond=0)
    Finalend = now.replace(hour=18, minute=35, second=0, microsecond=0)

    if (now>First and now<Firstend):
            period=320
            hero()
    elif(now>Second and now<Secondend):
            period=340
            hero()
    elif(now>Third and now<Thirdend):
            period=340
            hero()
    elif((now>Final and now<Finalend):
            period=360
            hero()
    else:
        banner='figlet RXCE V2.1'
        system(banner)
        print(f"{red}"Hi!! Thanks for buying the hack")
        print("Hi! thanks for trying our DEMO")
        print("----------Your play time-----------")
        print("18th March 2022, 11:00 AM- 11:30 AM")
        print("18th March 2022, 02:00 PM- 02:30 PM")
        print("18th March 2022, 04:00 PM- 04:30 PM")
        print("18th March 2022, 08:00 PM- 08:30 PM")
        print("Please play on the given time, and ")
        print("If you think it is an error contact")
        print(" admin on telegram @HACKMGK ")



else:
    def clear():
         for windows
        if name == 'nt':
            _ = system('cls')
        for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')
    code="MSDFX55"
    code1="BD23"
    code2="ASXS56"
    test="SDF43"
    night="NX13"
    nextday="NSD"
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
    print(" on telegram ----@HACKMGK for activating")
    print("     Plan Amount --    Total limit " )
    print(" 1.  200 INR -------  1 Day (30 Games")
    print(" 2.  500 INR -------  10 Days(90 Games")
    print(" 2.  1500 INR ------- 30 Days(210 Games")
    print("*---------*----------*-------------*----------*")
    print("If you need any discount contact me")
    print("Beware of fraudsters!!!")
    while(True):
        print("My banking name is SUNNY KUMAR")
        print(f"{red}After You Pay to The UPI ID above You Can Automatically")
        print(f"Activate Hack By Entering The Correct ")
        print(f"{green}(UTR) Or Upi Reference Number") 
        print(f"{neon}To Activate The Hack")
        print(f"If It Does'nt Open Contact Me On Telegram {yellow}@HACKMGK")
        print(f"{neon}*---------*----------*-------------*----------*")
        print(f"{red}*---------*----------*-------------*----------*")
        print("payhere--- UPI : ")
        print(f"{yellow}UPI1 : mkeditor@ybl")
        print("UPI2 : mkeditor@axl")
        print("If you have already paid to above UPI")
        print(f"{neon}Enter Your Activation Code Or Upi Reference for Opening Hack")
        bhai=input(": ")
        if(bhai==code or bhai==test or bhai==code1 or bhai==code2):
            clear()
            print("You have bought hack for 1 day")
            print(f"{purple}---------------Your play time----------------")
            print("19th March 2022, 02:30 PM- 03:00 PM")
            print("19th March 2022, 05:30 PM- 06:00 PM")
            print("19th March 2022, 08:30 PM- 09:00 PM")
            print("Please play on the given time, and ")
            print(f"If you think it is an {red}error {yellow}contact {green}me ")
            print(f"{neon}On Telegram {red}@HACKMGK")
            print("wait.... starting....")
            time.sleep(20)
            period=rava
            hero()
            print("Today Server is off RXCE try tomorrow ")
            rint(" of town, Tomorrow It will work as usual.")
            print(" Thank You!!")
            rint("To all the weekly members next week, cost will be  ")
            print(" 4000 INR , because in this week 2 days off " )
            print("Thank You!! ")
            sys.exit(" \n \n \n Contact on Telegram @HACKMGK")
        elif(bhai==nextday):
            clear()
            banner='figlet RXCE V2.1|lolcat'
            system(banner)
            print("----------Your play time-----------")
            print("19th March 2022, 02:30 PM- 03:00 PM")
            print("19th March 2022, 06:00 PM- 06:30 PM")
            print("19th March 2022, 08:30 PM- 09:00 PM")
            print("Please play on the given time, and ")
            print("If you think it is an error contact")
            print("wait.... starting....")
            time.sleep(20)
            period=rava
            hero()
            period("Sorry too many people(>20) using hack in same time ")
            sys.exit(" \n \n \n Contact on Telegram @HACKMGK")
        elif(bhai==night):
            clear()
            print("----------Your play time-----------")
            print("19th March 2022,  08:30 PM- 09:00 PM")
            print("19th March 2022, 08:30 PM- 09:00 PM")
            print("19th March 2022, 08:30 PM- 09:00 PM")
            print("Please play on the given time, and ")
            print("If you think it is an error contact")
            print("wait.... starting....")
            time.sleep(20)
            period=410
            hero()
            sys.exit(" \n \n \n Contact on Telegram @HACKMGK")
        else:
            clear()
            banner='figlet RXCE V2.1|lolcat'
            system(banner)
            print("Incorrect Activation Code :")
