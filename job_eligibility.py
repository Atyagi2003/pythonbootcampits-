#job eligibility check.
gender= input("Enter your gender\n");
age= int(input("Enter your age\n"));
if (gender=='M'):
    if(age>=17):
        print("You can apply for private job only.\n")
    else:
        print("You can't apply for any job.\n")    
elif (gender=='F'):
    if(age>=17):
        print("You can apply for any type of job,i.e., private or government.\n")
    else:
        print("You can't apply for any job.")
#this is must to remind both cases in mind during coding.(Positive and negative conditions.)