############################ 
## Modules and packages
############################
import math
from math import pi # csak egy részét importálja
from math import * # mindent importál és rövidnéven hivatkozható
import numpy as np # kap egy rövidítést
print(math.sqrt(16)) # ki kell írni az elérést
print(pi) # nem kell kiírni az elérést
print(np.array([1,2,3,4]))

## Saját pacakge
## Külön mappa, __init__.py definiciós fájl készítése, kód fájl készítése
print("-----------------")
print("Saját csomag importálás package elól")
print("-----------------")
from package.my_math import my_addition
from package import my_math
print(my_addition(4,5))
## van "sub" csomag is
import package.sub_package.my_sub_math as sb
print(sb.my_sub(4,3))

############################ 
## Strandard library overview
############################
"""
array : töümbök kezelése
math
random : random szám generálása
os : file and directory access
shutils : file műveletek (copyfile)
json: data serilalization (json-string oda vissza)
csv: csv file kezelés
datetime, time: dátum, idő kezelés
re : regular expressions
"""
