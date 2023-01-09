# https://www.hackerrank.com/challenges/java-anagrams/problem
# commit

def my_function(a):
    if a % 2 == 0:
        print("Páros")
    else:
        print("Páratlan")

print("Hello world! \n") 
my_function(3)
word1 = input("Add meg az első szót! ").lower()
word2 = input("Add meg a második szót! ").lower()

anagramma=1
if (len(word1)!=len(word2)):
    anagramma=0
else:
    for x in range(len(word1)):
        if (word1.count(word1[x]) != word2.count(word1[x])):
            anagramma=0
            print(word1[x])
if (anagramma==0):
    print("Nem anagramma")
else:
    print("Anagramma")    


