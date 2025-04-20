class Animal:
    def __init__(self, name):
        print("Animal __init__ called")
        self.name = name

    def speak(self):
        print("Generic animal sound")

class Dog(Animal):  # Dog inherits from Animal
    def __init__(self, name, breed):
        print("Dog __init__ called")
        # Call the __init__ method of the parent class (Animal)
        super().__init__(name)
        self.breed = breed

    # Override the speak method of the parent class
    def speak(self):
        print(f"{self.name} says Woof!")

    def wag_tail(self):
        print(f"{self.name} is wagging its tail.")

class Cat(Animal):  # Cat also inherits from Animal
    def speak(self):
        print(f"{self.name} says Meow!")

# Creating instances of the child classes
my_dog = Dog("Buddy", "Golden Retriever")
my_cat = Cat("Whiskers")

# Calling the inherited and overridden methods
my_dog.speak()    # Output: Buddy says Woof! (overridden)
my_cat.speak()    # Output: Whiskers says Meow! (overridden)

# Calling a method specific to the Dog class
my_dog.wag_tail() # Output: Buddy is wagging its tail.

# Accessing an inherited attribute
print(f"My dog's name is {my_dog.name}") # Output: My dog's name is Buddy
print(f"My cat's name is {my_cat.name}") # Output: My cat's name is Whiskers