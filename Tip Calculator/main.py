print("Welcome to Tip Calculator.")
bill = int(input("Please enter Your Bill amount : "))   
percent = int(input("Enter the percentage Tip U wanna give to the waiter : "))
grp = int(input("The number of people in the group to split the Bill : "))
total_bill = bill + bill*percent/100
per_head = total_bill/grp
per_head = round(per_head, 2)
print("The Total Bill is : {} and each member has to pay : {}".format(total_bill, per_head))