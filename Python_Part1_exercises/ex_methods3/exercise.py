num1 = 1122334455666

num1_str = str(num1)

print(type(num1_str)) #string

print(len(num1_str)) #length

print(num1_str[3]) #Third element

print(num1_str[2:6]) #3-5 Elements of the string (both inclusive)

#There i no vaariable called num2 or num3 but I can create it
num2 = "Hello Develhope"
num3 = 100
print(type(num2), type(str(num3)))

string_with_0 = '0' + num1_str
print(string_with_0) #Concatenate 0

print(string_with_0[:4]) #Charachters from start to position 4

print(string_with_0[4:]) #Characters from position 5 until the end

print(string_with_0[-4:]) #Negative Indexing to reach (567)