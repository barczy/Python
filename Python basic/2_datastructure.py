############################ 
## Data types
############################
##
## list
##
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
##
## sets: collection of unique items, unordered
##
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