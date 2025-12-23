############################ 
## OOP
############################
##
## Classes
############################
class Car:  #blueprint
    pass # üres parancs

audi=Car()
print(type(audi))

############################
## inicializálás
class Dog:  
    ## constructor, variables, methods
    def __init__(self, name, age): # self egy keyword, itt soroljuk fel az összes használ változót
        self.name = name
        self.age = age
    def bark(self):
        print(f"{self.name} says woof")

dog1 = Dog("Buddy",3)
print(dog1.name)
dog1.bark()

############################
## inheritence
class RealCar:
    def __init__(self, windows, doors, enginetype):
            self.windows = windows
            self.doors = doors
            self.enginetype = enginetype
    def drive(self):
            print(f"The person will drive {self.enginetype} car")

class Tesla(RealCar):
    def __init__(self, windows, doors, enginetype, is_selfdriving):
        super().__init__(windows, doors ,enginetype) # meghívja az ős függvényét
        self.is_selfdriving = is_selfdriving
    def __str__(self):
         return f"Tesla {self.windows}"
    def selfdriving(self):
         print(f"Tesla support self driving: {self.is_selfdriving}")


car1 = RealCar(4,5,"petrol")
car1.drive()
tesla1 = Tesla(4,5,"electric",True)
tesla1.selfdriving()
tesla1.drive()

############################
## Multiple inheritence
##
## class Dog(Animal, Pet):
##      def __init__(self, name, owner)
##            Animal.__init__(self, name)
##            Pet.__init__(self, owner)
## ...

############################
##  Polimofphism (single action, different froms like method overridings, interfaces)
##
class Animal:
    def speak(self):
        return "Sound of the animal"
class Dog(Animal):
    def speak(self):
        return "Woof!"
class Cat(Animal):
    def speak(self):
        return "Maow!"
def animal_speak(animal): ## ős osztályt használom, más lesz más entitásnál
     print(animal.speak())

dog = Dog()
cat = Cat()
print(dog.speak())
print(cat.speak())
animal_speak(dog)

############################
##  Abstract base class (abc), an empty class
##
from abc import ABC, abstractmethod

class Vehicle(ABC):
     @abstractmethod
     def start_engine(self):
        pass # üres utasítás, absctract metódus definíciója

class Car(Vehicle):
     def start_engine(self):
          return "Car engine started"
class Motorcycle(Vehicle):
     def start_engine(self):
          return "Motorcycle engine started"

def start_vehicle(vehicle):
     print(vehicle.start_engine())

car = Car()
motorcycle = Motorcycle()
start_vehicle(car)
start_vehicle(motorcycle)

############################
##  Encapsulation : Egységbezárás. Legyen egy helyen, minden ami kell. Csak ott legyen elérhető, 
##  ahol kell, public, protected, private
##  Abstraction: csak azt mutassam, ami kifele szükséges. Ami az abstract osztályban abstract függvény
##  az kötelező implementálni a leszármazottban.
##
print("-----------------")
print("Encapsulation")
print("-----------------")
class Person:
    def __init__(self, name = "Tom"):
        self.name=name # alapból publlic
        self.__id = 'id14' # ez privát lesz! dupla __
        self._age = 34 # ez a protected. örököltből elérhető, kintről nem
    ## privatenál getter, setter kell
    def __str__(self):
         return f"Person: {self.name}"
    def get_id(self):
        return self.__id
    def set_id(self, id): 
        self.__id = id
    def __add__(self, other):
        return Person(self.name+ " - " + other.name) 
    def __eq__(self, other):
        return self.name == other.name

person = Person()
print(person.name)
print(person.get_id())
print(dir(person)) #mutatja a publikus cuccait 

############################
##  Magic methods, Double underscore methods (dunder methods), start and ends with double underscore
##  általános beépített függvények
## __init__ : initialize
## __str__  : string representation
## __len__, ... 
print(dir(person))
print(person) # meghívja a definiált __str__ függvényt


############################
##  Custom exception
## 
class Error(Exception): # ebből kell örököltetni
    pass

class dobException(Error): # date of birth
    pass

year=int(input("Enter the dob: "))
age = 2025 - year
try:
    if age < 100:
        print("Ok")
    else:
        raise dobException
except dobException:
    print("Invalid date of birth")


############################
##  Operator overloading
##  __add__ + , __sub__ - , __mul__ *, __eq__ ==...
person1 = Person("Adam")
person2 = Person("Eva")
person3 = person1 + person2
print(person3.name)
print(person1 == person2)