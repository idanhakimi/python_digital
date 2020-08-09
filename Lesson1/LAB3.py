'''Create 2 variables : string of your full name, another string of your mail.
Create variable of your age (integer)
print all of them to the screen

then Print your name from the end to the beginning and print it only with your age*3

then check if your name is stored inside this full string:
"idan ben dudu yuval shimon yael gal adam shahar yana"
'''
name="idan hakimi"
age=28
mail="idan@gmail.com"
print("Full name: " + name + "\nage: " + str(age) + "\nmail: " + mail)
print("\n\nFull name: " + name[::-1] + "\nage: " + str(age*3) )
print("elia" in "idan ben dudu yuval shimon yael gal adam shahar yana")
