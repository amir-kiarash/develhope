class Animal:
    def __init__(self,legs_count):
        print("Animal object was created")
        self._legs = legs_count

    def runs(self):
        print("Running started")

    def count_legs(self):
        print(f"It has {self._legs}")

    def return_legs(self):
        return self._legs
        
animal= Animal(4)
animal.count_legs()
print(animal.return_legs())
print(animal._legs)