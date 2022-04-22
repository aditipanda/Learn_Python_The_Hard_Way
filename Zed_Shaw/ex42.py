class Animal(object):
    pass

## Dog is an Animal
class Dog(Animal):
    def __init__(self, name):
        self.name = name

## Cat is an Animal
class Cat(Animal):
    def __init__(self, name):
        self.name = name

## Person is a basic simple class
class Person(object):
    def __init__(self, name):
        self.name = name
        self.pet = None

## Employee is a Person
class Employee(Person):
    def __init__(self, name, salary):
        super(Employee, self).__init__(name)
        self.salary = salary

## Fish is a basic simple class
class Fish(object):
    pass

## Salmon is a Fish
class Salmon(Fish):
    pass

## Halibut is a Fish
class Halibut(Fish):
    pass

## rover is a Dog
rover = Dog('Rover')

## satan is a Cat
satan = Cat('Satan')

## mary is a Person
mary = Person('Mary')

## satan is mary's pet
mary.pet = satan

## frank is an Employee
frank = Employee('Frank', 120000)

## rover is frank's pet
frank.pet = rover

## crouse is a salmon
crouse = Salmon()

## harry is a halibut 
harry = Halibut()
