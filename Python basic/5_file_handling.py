############################ 
## Files handling
############################
##
## Open files
##
############################
with open('example.txt','r') as file:
    for line in file:
        print(line)
## vagy
with open('example.txt','r') as file:
    content = file.read()
    print(content)
## írás
with open("example_2.txt","w") as file: # w - overwrite, a -append
    file.write("Hello World\n")
    file.write("End of file")

## binary files
data = b'\x00\x01\x02\x03'
with open('example.bin',"wb") as file:
    file.write(data)
with open('example.bin',"rb") as file:
    print(file.read())

## write and read
with open('example_2.txt','w+') as file:
    file.write("first line\n")
    file.write("second line\n")
    file.seek(0) # file elejére viszi a curzort
    print(file.read())

############################
##
## Use directory
##
## create a new directory
## os.mkdir("new directory")
## os.exists("filename"), os.path.isFile(), os.path.isDir
import os
print(f"Current path: {os.getcwd()}")
items = os.listdir('.')
print(items)
