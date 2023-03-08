class Animal:
    def __init__(self, leg_count):
        self.leg_count = leg_count
        print("Animal object was created")
    
    def runs(self):
        print("Running started")


animal = Animal(4)
animal.runs()