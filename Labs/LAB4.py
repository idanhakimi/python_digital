'''
Create a list with 4 details about you: name, age, mail, phone and print it to the screen
then create another list with 2 IPs , then add 3 more IPs , pop the 3rd IP and print how many
IPs do we have and print them.
'''

details_list=["Idan Hakimi" , 28 , "idan@gmail.com" , "0234234342"]
print("Full name: " + details_list[0] + "\nAge: " + str(details_list[1]) + "\nMail: " + details_list[2] + "\nPhone: " + details_list[3])
ip_list=["1.1.1.1","2.2.2.2"]
print(ip_list)
ip_list.append("3.3.3.3")
ip_list.append("4.4.4.4")
ip_list.append("5.5.5.5")
print(ip_list)
ip_list.pop(2)
print("IP List length is: " + str(len(ip_list)) + "\nAnd the IP list: " + str(ip_list))