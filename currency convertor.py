#currency convertor program...
currency= str(input("Enter the country of currency\n"))
if (currency == "ind"):
    ind_curr= float(input("Enter the amount\n"));
    print("The amount is converted from INR to $:-\n", (ind_curr/83.98));
elif (currency == "usa"):
    for_curr= float(input("Enter the amount\n"));
    print("The amount is converted from $ to INR :-\n", (for_curr*83.98));
else:
    print("Invalid input. Please input either ind or usa")