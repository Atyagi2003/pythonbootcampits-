def cal_bmi(weight, height):
    bmi= weight / (height ** 2)
    return bmi
def interpret_bmi(bmi):
    if bmi < 18.5:
        return "Under weight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi <29.9:
        return "Over weight"
    else:
        return "Obesity"
    
try:
    weight= float(input("Enter your weight in kg:\n"))
    height= float(input("Enter your height in metres:\n"))

    bmi= cal_bmi(weight,height)
    interpretation= interpret_bmi(bmi)
    print(f"Your BMI is: {bmi:.2f}")
    print(f"Category: {interpretation}")
except ValueError:
    print("Please enter valid numerical values for weight and height.") 