
class Person():
    def __init__(self, name, age):
        print('creating person')
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age


p = Person(name='bob', age=33)

print('name:', p.get_name(), 'age:', p.get_age())

