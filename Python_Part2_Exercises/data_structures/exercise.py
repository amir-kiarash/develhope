list1 = ["lion", "monkey", "dog", "fish"]
tuple1 = ("lion", "monkey", "dog", "fish")
set1 = {"lion", "monkey", "dog", "fish"}
dict1 = {"lion":4, "monkey":2, "dog":4, "fish":2}

print(len(list1), len(tuple1), len(set1), len(dict1)) # The Lengths

print(list1[0], tuple1[0]) # First Element

print(dict1.get('lion')) # Value of lion in dict1

#change the 2nd position element of `list1` to "rabbit"
list1[1] = 'rabbit'
print(list1)

#try to change the 2nd position element of the tuple to "rabbit" and explain what happened.
tuple2 = tuple1[:1] + ('rabbit',) + tuple1[2:] 
print(tuple2)   # In Python tuples are immutable, you can not modify it's contents.
# in order to do it you have to create a new tuple with 'rabbit' in second position


#add "monkey" to `list1`
list1.extend(['monkey'])
print(list1)

#remove "rabbit" from `list1`
list1.remove('rabbit')
print(list1)

#in `dict1` the number of feet is written as value to each animal the fish has wrong value just fix it.
dict1.update({"fish": 0})
print(dict1)