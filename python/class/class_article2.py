#  Python Inheritance

# Inheritance allows us to define a class that inherits all the methods and properties from another class.

# Parent class is the class being inherited from, also called base class.

# Child class is the class that inherits from another class, also called derived class.






class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

# Use the Person class to create an object, and then execute the printname method:

# x = Person("John", "Doe")
# x.printname()

# print()

# Add a child class

# class Student(Person):
#   pass

# x = Student("Mike", "Olsen")
# x.printname()

# Add the __init__() Function

# The child's __init__() function overrides 
# the inheritance of the parent's __init__() function.

# class Student(Person):
#     def __init__(self, fname, lname):
#         Person.__init__(self, fname, lname)
#     def over(self):
#         print('Method indenpend from parent')

# y = Student('Bob', 'Dole')
# y.printname()

class Teacher(Person):
    def __init__(self, course_name):
        Person.__init__(self, fname='aaa', lname='bbb')
        self.cn = course_name
    def print_course(self):
        print('course: ', self.cn)



class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

y = Student("Mike", "Olsen", 2019)

y.welcome()

