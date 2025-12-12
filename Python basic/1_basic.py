############################ 
## Python basic syntax
############################ 

## simple line comment
'''
Multiline comment

'''
## Python is case sensitive
## Indentation (bekezdés), define the structure
name = 'akarki'
Name = 'Bárki'
print(Name)
for i in [1,2]:
    print(name)

## line continuation
print('Bármilyen hosszú\
      sor  törhetünk így')

## multiply statement in on line
x=5;print(x)

## variable assingment, automatic type detect, dynamic typing
i = 32 # will be int, type inference
print(type(i))
i = "akarmi"
print(type(i))

############################ 
## Python variables, operators
############################ 
## int, string, bool(True, False), float, ...
## Naming conventsion: start with letter or '_', case sensitives
i=True
print(type(i))

## type conversion
age=25
age_str=str(age) # int(), float()

## operators
## + - / * // % power:** 
print(10/3) # normál osztás
print(10//3) # egészre kerekít
print(10%3)  # maradék
## comparison operator
## ==  !=  > < <= =>
## Logical operators
## and not or

############################ 
## Conditional statements
############################ 
## if
age=20
if age>=20:
    print(".")
elif age<10:
    print("..")
else:
    print("...")

############################ 
## Loops
############################
## végigmegy egy collection-ön! collection bármi is lehet. 
for i in range(2,7):  # range(7) , range(0,10,2)-step paraméterrel
    print(i)
    if i==5:
        break

for c in "Zsolt":
    print(c)

count=0
while(count<5): # Amíg igaz!
    print(count)
    if count==3:
        break
    count=count+1