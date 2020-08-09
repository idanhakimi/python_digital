from time import sleep

##################################################
def menu(list_ip):
    while(True):
        choice=input("\nMenu:\n---------\n1. Create a new file\n2. add new IP address\n3. remove specific IP address\n4. search for an IP\n5. print specific IP\n6. print all IPs\n")
        if(choice=="1"):
            create_file()
        elif(choice=="2"):
            list_ip=add_IP(list_ip)
        elif(choice=="3"):
            list_ip=remove_ip(list_ip)
        elif(choice=="4"):
            search_ip(list_ip)
        else:
            print("Enter 1-6 only!!!!\n")
            continue
        if(input("\nDo you want to quit? y/n")=="y"):
            break
        else:
            print("\nWelcome back\n")
    print("\nBye Bye\n")
##############################################################
def create_file():
    print("Creating file...\n")

##############################################################
def add_IP(list_ip):
    new_ip=search_ip(list_ip)
    if(new_ip!=False):
        print("\nAdding new IP...\n")
        sleep(3)
        list_ip.append(new_ip)
    print("Your new List of IPs: " + str(list_ip))
    return list_ip

##############################################################
def search_ip(list_ip):
    new_ip=input("Enter IP: ")
    print("\nSearching...\n")
    sleep(3)
    if(new_ip in list_ip):
        print("This IP is already in use!")
        return False
    else:
        print("This IP is available")
        return new_ip

##############################################################
def remove_ip(list_ip):
    ip=search_ip(list_ip)
    if(ip==False):
        print("\nDeleting the IP...\n")
        sleep(3)
        list_ip=list_ip.remove(ip)
        print("The new list: " + str(list_ip))
    else:
        print("\nThis IP doesn't exist...\n")
    return list_ip


##########main code###############
my_list=["192.168.1.1","1.1.1.1","55.55.55.55"]
menu(my_list)