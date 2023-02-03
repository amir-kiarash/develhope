import random

number1 = random.randint(-100,100)
number2 = random.randint(-100,100)

if abs(number1) > abs(number2):
    print("X's absolute value greater than Y's absolute value")

elif abs(number1) < abs(number2):
    print("Y's absolute value greater than X's absolute value")

else:
    print("X's absolute value is Equal to Y's absolute value")
    