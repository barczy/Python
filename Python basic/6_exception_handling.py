############################ 
## Exception handling
############################
##
## Open files
##
############################
a=10
try:
    a = 5 / 0
except:
    print("Division by zero. Please")


try:
    a = 5 / 2 # ha 0-val osztunk
    b = 2 # ha b nincs definiálva 
    a = b
except ZeroDivisionError as ex:
    print(ex)
    print("Division by zero. Please")
except Exception as ex: # származtatott fő osztály, ez legyen az utolsó, sorban értékeli ki
    print(ex)
else: # sikeres ág, ha nincs hiba
    print("Minden rendben")
finally: # bármi is, ez lefut
    print("Blokk lefutott")
