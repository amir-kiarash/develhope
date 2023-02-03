import random

number1 = random.randint(1,100)
number2 = random.randint(1,100)

# Compare the numbers to eachother 

if number1 > number2:
    print("X greater than Y")

elif number2 > number1:
    print("Y greater than X") 

else:
    print("X And Y are Equal")