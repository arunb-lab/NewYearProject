my_list = [1, 2, 3]
my_tuple = (1, 2, 3)

my_list.append(4)
print(my_list)
print(my_tuple)
# The above code will raise an AttributeError because tuples are immutable
# In Python, tuples are immutable, meaning once they are created, their elements cannot be changed, added, or removed.
# Uncommenting the next line will raise an error
# my_tuple.append(4)  # This will raise an AttributeError
# Tuples support indexing and slicing just like lists
print("First element of tuple:", my_tuple[0])
print("Sliced tuple:", my_tuple[1:3])
# Tuples can be used as keys in dictionaries because they are immutable
my_dict = {my_tuple: "This is a tuple key"}
print("Dictionary with tuple key:", my_dict)
#In Python, when defining methods inside a class, first parameter is always self.
# It is not a keyword, but a naming convention that plays a key role in Python’s object-oriented programming.
# The self parameter represents instance of the class itself, allowing you to access and modify its attributes and methods.
class Car:
    def __init__(self, brand, model):
        self.brand = brand  # Set instance attribute
        self.model = model  # Set instance attribute

    def display(self):
        return self.brand, self.model
# Create an instance of Car
car1 = Car("Toyota", "Corolla")
# Call the display method
print(car1.display())
########################################################################
class gfg:
    def __init__(self, topic):
        self._topic = topic  # Store parameter value in instance variable

    def topic(self):
        print("Topic:", self._topic)  # Access the renamed variable
# Creating an instance of gfg
ins = gfg("Python")
# Calling the topic method
ins.topic()
#In Python, when defining methods inside a class, first parameter is always self.
# It is not a keyword, but a naming convention that plays a key role in Python’s object-oriented programming.
# The self parameter represents instance of the class itself, allowing you to access and modify its attributes
# and methods.
class Car:
    def __init__(self, brand, model):
        self.brand = brand  # Set instance attribute
        self.model = model  # Set instance attribute

    def display(self):
        return self.brand, self.model
# Create an instance of Car
car1 = Car("Toyota", "Corolla")
# Call the display method
print(car1.display()) and methods.
class Car:
    def __init__(self, brand, model):
        self.brand = brand  # Set instance attribute
        self.model = model  # Set instance attribute
    def display(self):
        return self.brand, self.model
# Create an instance of Car
car1 = Car("Toyota", "Corolla")
# Call the display method
print(car1.display())
########################################################################