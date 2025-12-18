############################ 
## Functions
############################

print("-----------------")
print("Fnnctions")
print("-----------------")
def ftest(arguments=3): # default paraméter
    """Function description"""
    value=2*arguments
    print(value)
    return value
ftest()
ftest(2)

print("-----------------")
print("Arguments")
print("-----------------")
##variable length argument
def ftest_2(arg1=1, arg2=5, arg3=5, arg4=1): 

    print(arg1+arg2+arg3+arg4)

ftest_2()
ftest_2(5, arg4=5)

##variable length argument, position and keywords arguments
def ftest_3(start_sum, *args):
    sum=start_sum
    for number in args:
        sum=sum+number
    print(sum)


ftest_3(0,2,3,4)
ftest_3(100,4,5,6,7,8)

print("-----------------")
##variable length argument, position and keywords arguments
def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")

print_details(name="Bob", age=23, detail="misc")


print("-----------------")
##variable length argument, position and keywords arguments (kwargs)
def print_details(*args, **kwargs):
    for val in args:
        print(f"{val}")
    for key, value in kwargs.items():
        print(f"{key} : {value}")

print_details("alma", 45, name="Bob", age=23, detail="misc")

print("-----------------")
## return multiply parameters (tuples)
def func_return(a,b):
    return a*b, a

print(func_return(2,3))

print("-----------------")
print("Recursive:")
## recursion
def factorial(n):
    if n==0:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(5))


print("-----------------")
print("Map, filter:")
## lambda functions: function without a name
## lambda argumets: expression
addition = lambda a,b : a+b
print(addition(5,6))

## map() : apply a functions to all element of a list (iterable) return a map object (iterable)
## min 2 areguments: function, iterable(s)
numbers = [1,2,3,4,5]
numbers_2 = [5,6,7,8,9]
print(list(map(lambda x: x**2, numbers)))
print(list(map(lambda x,y: x+y, numbers, numbers_2)))

## filter(cond_function, iterable)
## filter out from an iterable, where the function return true
numbers = [1,2,3,4,5,6,7,8,9,10]
print(list(filter(lambda x : x%2==0 and x>5, numbers)))