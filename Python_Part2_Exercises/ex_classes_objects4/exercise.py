list1 = ["lion", "monkey", "dog","fish"]
for l in list1:
    print(l)
tuple1 = ("lion", "monkey", "dog","fish")
for tu in tuple1:
    print(tu)
set1 = {"lion", "monkey", "dog","fish"}
for s in set1:
    print(s)
dict1 = {"lion":"land", "monkey":"land", "dog":"land","fish":"water"}
for x, y in dict1.items():
    if y == 'land':
        print(f"{x} lives in {y}")

