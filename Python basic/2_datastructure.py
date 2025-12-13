############################ 
## Data types
############################
##
## list
##
############################
print("-----------------")
print("List")
print("-----------------")
to_do_list=["Shopping","Cleaning","Pay bills"]
to_do_list.append("Schedule meegint")
to_do_list.remove("Cleaning")

if "Pay bills" in to_do_list:
    print("Lets pay")

for task in to_do_list:
    print(f"-{task}")

print(to_do_list)
############################
##
## sets: collection of unique items, unordered
##
############################
print("-----------------")
print("Set")
print("-----------------")
my_set = {1,2,3,4,5}
your_set = {9,10}
print(my_set)
my_set = {1,2,3,4,5,5,5,5} #duplication will eliminate
print(my_set)
my_set.add("akarmi")
my_set.remove(4)
my_set.discard(10) # nem ad hibát, ha nincs benne
print(my_set)
removed_element = my_set.pop() # kivesz egy elemet
print(removed_element); print(my_set)
if (3 in my_set):
    print(f"Benne van: {my_set}")
union_set=my_set.union(your_set) # halmazműveletek: intersection, intersection_update, defference, issubset, ..
print(union_set)
my_set.clear() #kiüríti

text="This is a text. This is an example" ## kiszedni belőle az egyedi szavakat!
words=text.split()
unique_word_set=set(words)
print(unique_word_set)

############################
##
## Tuples : ordered collections of items that are immutables (mint egy lista, rendezett elemek, megváltoztathatatlan)
##
############################
print("-----------------")
print("Tuples")
print("-----------------")
numbers = tuple([0,6,1,2,3,4,5,6,2])
print(numbers)
print(numbers[3]) # indexelt
print(numbers[2:4]) # indexelt
mixed = (1, "akarmi", 3.14)
print(mixed)
## operations: + (concatenation), * (megsokszorozza a halmazt ua elemekkel)
## mixed[1]="Barmi", hibát dob, nem változtatható meg....
print(numbers.count(2)) # hányszor van benne ez az elem
print(numbers.index(6)) # mi az első előfordulása ennek az elemnek
numbers2 = 0,6,1,5,6,7 # így is definiálható (packing)
print(numbers2)
first,*midle,last = numbers2 # szétszedhető változókba, unpacking
print(first)
print(midle)
## nested list, tuples
lst=[[1,2,3],[5,6]]
print(lst)


############################
##
## Dictionaries: unordered collection of items. Data in key-value pair
##
############################
print("-----------------")
print("Dictionaries")
print("-----------------")
student = {"name":"thomas", "age":15, "tmp": 17}
print(student)
print(student['name'])
print(student.get("name"))
## add, upddate, delete
student["age"]=17
student["city"]="Budapest"
del student["tmp"]
print(student)
print(student.keys())
print(student.values())
print(student.items()) #tuples formára hozza
# shallow copy
student_copy=student
student_copy2=student.copy() # valós másolat
student["name"]="Thomas2" # másik példány is változik!!! csak pointer van
print(student_copy)
print(student_copy2)
for key, value in student.items():
    print(f"{key} - {value}")
# nested dictionaries
students = {
    "student1" : {"name" : "A"},
    "student2" : {"name" : "B"}
}
print(students["student1"]["name"])
# conditional dictionary comprehensions !!!!!
squares = { x:x**2 for x in range(10) if x%2==1}
print(squares)
