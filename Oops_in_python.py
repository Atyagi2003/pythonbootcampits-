class Ashish:
    currYear= int(input("Enter the current year\n"))
    bornYear= int(input("Enter your born year\n"))
    age= int(currYear) - int(bornYear)
    

x= Ashish()
print("The current year is ",x.currYear,"\nYour born year is ",x.bornYear)
print("\nYour age is ",x.age)