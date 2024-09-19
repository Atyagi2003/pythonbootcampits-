from datetime import datetime
def cal_age(birth_year):
    curr_year= datetime.now().year
    age= curr_year - birth_year
    return age
birth_year= int(input("Enter your born year\n"))
age= cal_age(birth_year)
print(f"Your age is: {age} years")