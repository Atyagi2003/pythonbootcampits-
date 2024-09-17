num= int(input("Enter any number\n"))
i= int(num) - 1
while i > 0:
  num *= i
  i -= 1

print("Factorial of given number is ", num)