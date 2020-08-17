print("Now we will calculate your marketing:\n\nPrices:\n----------\nTomato=3 NIS\nCucamber=2 NIS\nCola=5 NIS\nChicken=20 NIS\n ")
tomatos=int(input("Enter how many tomatos?"))
cucambers=int(input("Enter how many cucamberss?"))
colas=int(input("Enter how many colas?"))
chickens=int(input("Enter how many chickens?"))

print("\nSummary of your order:\n-----------\ntomatos: " + str(tomatos) + "\ncucambers: " + str(cucambers) + "\ncolas: " + str(colas) + "\nchickens: " + str(chickens))

summary=(tomatos*3)+(cucambers*2)+(colas*5)+(chickens*20)
print("\nYou have to pay: " + str(summary) + " NIS without tax")
print("\nYou have to pay: " + str("%.2f" % (summary*1.17)) + " NIS with tax")



