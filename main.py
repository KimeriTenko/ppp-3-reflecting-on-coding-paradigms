# Functional Prompt
def flatten_and_sort(array):
    arr = []
    for item in array:
        for i in item:
            arr.append(i)
    return sorted(arr)

# Object Oriented Prompt 
class Podracer:
  def __init__(self, max_speed, condition, price):
    self.max_speed = max_speed
    self.condition = condition
    self.price = price
    
  #   The code above implements the following coding principles: 
#   Encapsulation: The code encapsulates the data attributes max_speed, condition, and price by defining them as instance variables in the class constructor (__init__ method). This is an example of data encapsulation, which helps to maintain the integrity of the data.
# Abstraction: The class provides a simple and abstract representation of a Podracer object, without revealing the implementation details of its attributes. This is an example of abstraction, which helps to simplify complex processes and improve code readability.
# Object-Oriented Programming: The code defines a class, which is a blueprint for creating objects, and encapsulates the data and behavior of a Podracer object. This is an example of Object-Oriented Programming (OOP), a programming paradigm that focuses on the concepts of objects and classes.


  # Define a repair() method that will update the condition of the podracer to "repaired".
  def repair(self):
    self.condition = "repaired"
    
# The code above implements the following coding principles:
# Encapsulation: The function encapsulates the implementation details of the condition attribute by modifying its value. This is an example of data encapsulation, which helps to maintain the integrity of the data.
# Abstraction: The function provides a simple and abstract way to modify the condition of an object, without revealing the implementation details. This is an example of abstraction, which helps to simplify complex processes and improve code readability.
    
    
# Define a new class, AnakinsPod that inherits the Podracer class, but also contains a special method called boost that will multiply max_speed by 2.
class AnakinsPod(Podracer):
  def __init__(self, max_speed, condition, price):
    super.init(max_speed, condition, price):
  
  def boost(self):
    self.max_speed *= 2
    
#   The code above implements the following coding principles:
# Inheritance: The AnakinsPod class inherits from the Podracer class, indicated by the syntax class AnakinsPod(Podracer).
# Encapsulation: The code encapsulates the implementation details of max_speed by defining the boost method to modify its value. This is an example of data encapsulation, which helps to maintain the integrity of the data.


# Define another class that inherits Podracer and call this one SebulbasPod. 
# This class should have a special method called flame_jet that will update the condition of another podracer to "trashed".
class SebulbasPod(Podracer):
  def __init__(self, max_speed, condition, price):
    super.init(max_speed, condition, price):
  
  def flame_jet(self,other):
    other.condition = "trashed"
    
# The above code implements the following code principles:

# Inheritance: The SebulbasPod class inherits from the Podracer class, indicated by the syntax class SebulbasPod(Podracer).
# Method Overriding: The __init__ method of the SebulbasPod class overrides the __init__ method of the parent class Podracer.
# Method Overloading: The flame_jet method of the SebulbasPod class is not defined in the parent class Podracer, indicating method overloading.
# Method Chaining: The super method is used to call the __init__ method of the parent class Podracer by chaining the method calls, indicated by the syntax super().__init__(max_speed, condition, price).

# Would it have been easier to implement a solution using a different coding style? Why or why not?
# How did object oriented programming assist in solving this problem?

# The code in the previous example follows Object-Oriented Programming (OOP) principles, which is a popular coding style for implementing complex systems and encapsulating data and behavior. This coding style is well-suited for tasks that require the creation of objects that have specific attributes and behaviors, and can be easily extended or modified to add new features.
# However, other coding styles, such as procedural programming or functional programming, may be more suitable for other types of tasks, such as those that require a simple and straightforward implementation of a specific algorithm.
# Ultimately, the choice of coding style depends on the complexity of the task, the preferences of the programmer, and the requirements of the project.

