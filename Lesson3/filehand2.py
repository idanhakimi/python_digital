# filename = "C:/Users/אידן חכימי/Documents/Pycharm/hello.txt"
# file = open(filename, "r")
# my_string=file.read()
# file.close()
# print(my_string)
# my_list=my_string.split(",")
# print(type(my_list))
# print(my_list)


filename = "C:/Users/אידן חכימי/Documents/Pycharm/hello.txt"
file = open(filename, "r")
# print(file.readlines()[2])
new_list=[]
new_list=file.read().splitlines()
print(new_list)
file.close()
for i in new_list:
    print("Available " + i)
