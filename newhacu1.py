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

expirydate = datetime.date(2022,  1, 13 )
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
    banner='figlet Rxce 7.o '
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
                  with st.spinner('In Progress....'):
				d=pd.read_excel("1234.xlsx")
				#clf = svm.SVC(kernel="")
				#clf = DecisionTreeClassifier(random_state=0)
				PRICE=getSum(current)
				X=d[['A'+PRICE+'B']]
				y=d['D']
				X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.001)
				#st.write("The shape is ",d.shape)
				clf = LogisticRegression(random_state=0).fit(X, y)
				#st.write("You selected ",s_type)
				p=clf.predict([[a,b]])
				if p%2==0:
					#r=r+1
					st.success("Next is GREEN")
				elif p%2==1:
					#g=g+1
					st.error("Next is RED")
          
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
        banner='figlet Rxce 7.o '
        print("Hi!! Thanks for buying Life time the hack")
        print("----------Your play time-----------")
        print(" 11:00 PM- 11:35 PM")
        print(" 02:00 PM- 02:35 PM")
        print(" 05:00 PM- 05:35 PM")
        print(" 09:00 PM- 09:35 PM")
        print(" 11:00 PM- 12:35 PM")
        print("Please play on the given time, and ")
        print("If you think it is an error contact")
        print(" admin on telegram @Hackmgk ")
else:
    banner='figlet Thank '
    system(banner)
    print("*---------*----------*-------------*----------*")
    print("Your hack has expired--- Please contact")
    print(" on telegram ----@hackmgk for activating")
    print(" Recharge Amount :        Total limit " )
    print(" 2.     3000 INR -------  30 Days")
    print("*---------*----------*-------------*----------*")
    print("Your custom hack can be made request from us.")
    print( "Msg me on telegram @hackmgk")
