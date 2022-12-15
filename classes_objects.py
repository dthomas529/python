# YouTube: Amigoscode
# a class ClassName consists of properties and behaviors

# define a class ClassName
class Person:

# define properties of the class
# Define an instance of the current class
# "self" represents the defined class
  def __init__(self, name, age):
    self.name = name
    self.age = age


# define behaviors of the class
# A sample method; in OOP a method is a function
# "self" allows access to the properties 
# that are already defined in class
    def walk(self):
      print(self.name + 'is walking...')
    def speak(self):
      print('Hello, my name is ' + self.name + 'and I am' + str(self.age) + 'years old.')
      
john = Person("John", (22)
john.speak()
john.walk()

print('-----------------')

mariam = Person("Mariam", 18)
mariam.speak()
mariam.walk()

              
