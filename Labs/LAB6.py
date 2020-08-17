from time import sleep

choice=input("Menu:\n-----\n1.Insert Number and ** it by 3\n2.Insert 4 IPs to a list and print it\n3.Insert 4 Entries to DNS_Dictionary and print it\n4.Check if a string is Polindrom\n")
if(choice=="1"):
    print("The new number is: " + str((int(input("Enter a number: ")))**3))
elif(choice=="2"):
    list_ip=[]
    list_ip.append(input("Enter new IP: "))
    list_ip.append(input("Enter new IP: "))
    list_ip.append(input("Enter new IP: "))
    list_ip.append(input("Enter new IP: "))
    print("\nThe new list:\n--------------\n" + str(list_ip ))
elif(choice=="3"):
    dns_dict={}
    dns_dict.update({input("Enter a URL: "): input("Enter IP: ")})
    dns_dict.update({input("Enter a URL: "): input("Enter IP: ")})
    dns_dict.update({input("Enter a URL: "): input("Enter IP: ")})
    dns_dict.update({input("Enter a URL: "): input("Enter IP: ")})
    print("\nThe new dns_dict:\n--------------\n" + str(dns_dict))
elif(choice=="4"):
    word=input("Enter a word: ")
    if (word == word[::-1]):
        print("This is polindrom!")
    else:
        print("This isn't polindrom!")
else:
    print("Enter 1-4 only!!...")










