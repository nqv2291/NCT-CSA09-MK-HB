class Employee:
    def __init__(self, name, poss):
        self.name = name
        self.poss = poss
    def say_hi(self):
        print("hello my name is ", self.name)

    def tell_position(self):
        print("I am a ", self.poss)

john=Employee("john", "software engineer")
john.say_hi()
john.tell_position()