# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def myfunc(self):
#     print("Hello my name is " + self.name)

# p1 = Person("John", 36)
# p1.myfunc()

class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)
    print('My age is ', + abc.age)


p1 = Person("John", 36)
p1.myfunc()

# Modify object
p1.age = 40
p1.myfunc()

# del p1.age
# p1.myfunc()

# class Person:
#   pass