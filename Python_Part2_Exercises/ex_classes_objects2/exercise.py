
class Animal:
    def __init__(self,legs_count):
        print("Animal object was created")
        self.number_of_legs = legs_count

    def runs(self):
        print("Running started")

    def count_legs(self):
        print(f"It has {self.number_of_legs}")

    def return_legs(self):
        return self.number_of_legs

animal = Animal(4)
animal.runs()
animal.count_legs()
print("Number of Legs:", animal.return_legs())
