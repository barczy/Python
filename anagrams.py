
# https://www.hackerrank.com/challenges/java-anagrams/problem
# commit

def my_function(a):
    if a % 2 == 0:
        print("Páros")
    else:
        print("Páratlan")

print("Hello world! \n") 
my_function(3)
word1 = input("Add meg az első szót! ")
word2 = input("Add meg a második szót! ")
if (len(word1)!=len(word2)):
    print("Nem egyeznek\n")
else:
    print("Egyeznek\n")
for x in range(len(word1)):
    print(word1[x])


