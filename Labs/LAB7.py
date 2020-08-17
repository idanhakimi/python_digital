''' Lab7- Cube project
נקבל כקלט כמה כסף יש לנו לשחק
עלות משחק 3 ש"ח
אם יש עוד נחזיר אותו ללקוח
בכל תור נגריל 2 קוביות , אם הן זהות זכינו ב- 100 ש"ח, אם הן זהות אבל שוות גם ל-6, זכינו ב- 1000 ש"ח
אם הן לא זהות, אבל קוביה 2 שווה ל-2 זכינו ב- 40 ש"ח
אם הן לא זהות אבל קוביה 1 שווה ל-1 זכינו ב- 20 ש"ח
לבסוף נדפיס למסך בכמה כסף זכינו
'''

from random import randint
from time import sleep

print("Welcome to our Cube game\nEach turn cost 3 ILS\n")
money=int(input("Enter how much money do you have?\n "))
turns=(money//3)
print("You have: " + str(turns) + " turns\nYour change: " + str(money%3) + " ILS\n")
prize=0
for i in range(turns):
    print("Rolling Cubes for Round Number " + str(i+1) + " :\n------------------------")
    sleep(3)
    cube1=randint(1,6)
    cube2=randint(1,6)
    print("Cube1: " + str(cube1) + "\nCube2: " + str(cube2) + "\n")
    if(cube1==cube2):
        if(cube1==6):
            prize=prize+1000
        else:
            prize=prize+100
    elif(cube1==1):
        prize = prize + 20
    elif(cube2==2):
        prize = prize + 40

print("Calculating your prize...")
sleep(3)
print("Your prize: " + str(prize) + " ILS")