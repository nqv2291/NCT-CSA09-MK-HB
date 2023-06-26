class Dog:
    """A simple attempt to model a dog."""
    
    def __init__(self, name, age, breed):
        """ Initialize name and age attributes """
        
        self.name = name
        self.age = age
        self.breed = breed
        
    def rolling(self):
        """ Simulate a dog sitting in response to a command """
        
        print(f"{self.name} is rolling on the ground")

dog_1 = Dog("Mèo", 3, "husky")
dog_1.rolling()
