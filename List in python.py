friendname= ["Pawan","Atul","Bharat"]
print("before",friendname)
# #to add the new friend name in list
friendname.append("Ashish Tyagi")
# #print after adding name
print("After", friendname)
# #to add the name in specific position
friendname.insert(0,"Harsh")
# #print after adding name at 0 index
print("Add name at index 0", friendname)
# #to remove the name from list
friendname.remove("Harsh")
# #print after removing name from the list
print(friendname)
# #to clear the list
# friendname.clear()
# print(friendname)
# # #to remove the data in list with specific index
# friendname.pop(2)
# print(friendname)
# # #before sorting
# print(friendname)
# # #to sort the list
# friendname.sort()
# print(friendname)
# #to print element in the given list
for names in friendname:
    print(names)
# #to print number from 1 to 10
for name in range(1,11):
    name= input("Enter the name.\n");
    print("\n",name)