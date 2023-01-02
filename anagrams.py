
# https://www.hackerrank.com/challenges/java-anagrams/problem
# commit
print("Hello world! \n") 
word1 = input("Add meg az első szót! ")
word2 = input("Add meg a második szót! ")
if (len(word1)!=len(word2)):
    print("Nem egyeznek\n")
else:
    print("Egyeznek\n")
print(word1[1])
for x in range(len(word1)):
    print(word1[x])