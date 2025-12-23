############################ 
## Iterators: access element of a collection sequentially
## Sufficient memory management
############################
print("-----------------")
print("Iterator")
print("-----------------")
my_list = [1,2,3,4,5,6,7]
for i in my_list:
    print(i)
## Iterator: iter(), next()
iterator=iter(my_list)
print(type(iterator))
print(next(iterator)) # kiveszi a következő elemet

print("Ciklusban:")
while True:
    x = next(iterator, None)
    if x is None:
        break
    print(x)


############################ 
## Generator: sufficient memory management. Generate value on the fly do not store them in memory
## Végigiterál egy szekvencián, nem tárol, on the fly visszaadja az értékét, amikor kell
## yield kulcsszó!
print("-----------------")
print("Generator")
print("-----------------")
def square(n):
    for i in range(3):
        yield i**2

for i in square(3):
    print(i)

## iterátorral is feldolgozható
a = square(3)
print(next(a))
print(next(a))

## return more value
print("-----------------")
print("Függvény ami több értéket is visszaadhat")
def my_generator():
    yield 1
    yield 2
    yield 3

gen=my_generator()
print(next(gen))
print(next(gen))

## Felhasználás, nagy fájlok felolvasása
print("-----------------")
print("Nagy fájl felollvasása generátorral, memóriába történő felolvasás nélkül:")
def read_large_file():
    with open("example.txt",'r') as file:
        for line in file:
            yield line

text=read_large_file()
for line in text:
    print(line.strip())


############################ 
## Decorator: függvények, metódusokhoz add hozzá plusz funkciókat, anélkül, hogy a kódba belenyúlnánk
##
print("-----------------")
print("Decorator")
print("-----------------")
def welcome():
    return "Welcome to the advance pyhon course"

print(welcome())
wel=welcome # function copy!
del welcome # ki is törölhető
print(wel())

## closures: function inside a function
def main_welcome():
    msg="Welcome from main"
    def sub_welcome_method():
        print(msg) # használhatóak a kólső változók is
        print("Welcome from sub!")
    return sub_welcome_method()
main_welcome()


## closures: function inside a function, mint az előző de függvényt adunk át
def main_welcome(func):
    msg="Welcome from main"
    def sub_welcome_method():
        func("Welcome print") # meghívódik az átadott print hívás!
        print("Welcome from sub!")
    return sub_welcome_method()
main_welcome(print) ## átadja a beépített print metódust

## decorator
print("-----------------")
print("Decorator manuálisan:")
def main_welcome(func):
    def sub_welcome_method():
        func() # meghívódik a paramáternek kapott függvény
        print("Welcome from sub!")
    return sub_welcome_method()
def logging():
    print("Loggolás")
main_welcome(logging) ## átadja a beépített naplózó függényt

print("-----------------")
print("Decorator beépítetten:")
def my_decorator(func):
    def wrapper():
        func() # meghívódik a paramáternek kapott függvény
        print("Wrapper kimenete")
    return wrapper

@my_decorator #decorator beépített hívása
def course_introduction():
    print("A vizsgálandó függvény kimenete")

course_introduction()
