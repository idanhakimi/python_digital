'''
Menu:
1. printing 100 numbers
2. check fibo
3. randint numbers until we get 12 or we count 10 times
'''
from random import randint
from time import sleep

while(True):
    choice=input("Menu:\n--------------\n1.printing 100 numbers\n2.check fibo\n3.randint numbers until we get 12 or we count 10 times\n")
########################################################
    if(choice=="1"):
        for i in range(1,101):
            print(i)
########################################################
    elif(choice=="2"):
        #fibo = [1, 2, 3, 5, 8, 13, 21]
        fibo=[]
        for i in range(7):
            fibo.append(int(input("Enter a number: ")))
        boolean = "True"
        for i in range(2, len(fibo)):
            print(fibo[i])
            print(fibo[i - 1])
            print(fibo[i - 2])
            print("\n")
            if fibo[i] != (fibo[i - 1] + fibo[i - 2]):
                boolean = "False"
                break
        if boolean == "True":
            print("It is fibo series")
        else:
            print("It isn't fibo series")
########################################################
    elif(choice=="3"):
        counter = 1
        num=randint(1,12)
        while(num!=12 and counter<11):
            print("Counter:" + str(counter) + "  Number:" + str(num) + "\n")
            counter=counter+1
            num = randint(1, 12)
    else:
        print("Enter 1-3 only!!\n")
        continue
    exit=input("Do you want to exit? yes/no\n")
    if(exit=="yes"):
        print("Thank you and bye bye...\n")
        break



