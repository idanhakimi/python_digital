'''Create a dictionary with 5 names & money
then sum the money of the first & last names and print it to the screen
after, add a new name with the sum of the money you calculated before
in the end, print the number of entries and check if "idan" is inside
'''

dict_names={"dudu":25000,"avi":30000,"itay":76000,"ortal":66000,"gal":120000}
print(dict_names)
summay=dict_names["dudu"]+dict_names["gal"]
print("The summary is: " + str(summay))
# dict_names["yoel"]=summay
# print(dict_names)
dict_names.update({"yoel":summay})
print(dict_names)
print("Number of entries: " + str(len(dict_names)))
print("idan" in dict_names)