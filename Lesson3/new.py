def create_file(file):
    f = open("C:/Users/אידן חכימי/Documents/Pycharm/" + file + ".txt" , "x")
    f.close()

def read_file(file):
    filename = "C:/Users/אידן חכימי/Documents/Pycharm/" + file
    file = open(filename, "r")
    print(file.read())
    file.close()

def write_file(file):
    filename = "C:/Users/אידן חכימי/Documents/Pycharm/" + file
    file = open(filename, "w")
    file.write(input("Enter IP: ") + "\n" + input("Enter IP: "))
    file.close()

def append_file(file):
    filename = "C:/Users/אידן חכימי/Documents/Pycharm/" + file
    file = open(filename, "a")
    file.write(input("Enter IP: ") + "\n" + input("Enter IP: "))
    file.close()

def menu():
    while(True):
        choice=input("Enter your choice:\n1.Create a file\n2.Read a file\n3.Write a file\n4.Append to a file\n")
        if(choice=="1"):
            create_file(input("Enter file name: "))
        elif(choice=="2"):
            read_file(input("Enter file name: "))
        elif(choice=="3"):
            write_file(input("Enter file name: "))
        elif(choice=="4"):
            append_file(input("Enter file name: "))
        else:
            print("fuck off")


########Main Code##########
menu()