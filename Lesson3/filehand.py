#‘r’ – Read mode which is used when the file is only being read
#‘w’ – Write mode which is used to edit and write new information to the file (any existing files with the same name will be erased when this mode is activated)
#‘a’ – Appending mode, which is used to add new data to the end of the file; that is new information is automatically amended to the end
#‘r+’ – Special read and write mode, which is used to handle both actions when working with a file

###write 192.168.1.1/1.2
filename = "C:/Users/אידן חכימי/Documents/Pycharm/hello.txt"
file = open(filename, "r+")
print(file.read())
file.write("192.168.1.1\n192.168.1.2")
print(file.read())
file.close()
#
# ###it will append 192.168.1.3/1.4
# file = open(filename, "a+")
# file.write("\n192.168.1.3\n192.168.1.4")
# file.close()
#
# ###print to the screen the new output of the file
# file = open(filename, "r")
# print(file.read())
# file.close()
#
# filename = "C:/Users/אידן חכימי/Documents/Pycharm/hello.txt"
# file = open(filename, "r")
# for line in file:
#     print(line)
# file.close()












