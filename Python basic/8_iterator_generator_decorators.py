############################ 
## Iterators: access element of a collection sequentially
############################
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