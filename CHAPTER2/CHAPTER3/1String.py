# String is a squence of characters enclosed with qoutes 
# String is immutable means it can not be changed once is initialize 

x = "Atulsingh"
print(x)

# Slice of string 
# x[0:4] start from 0 index and goes to index 3 not consider indexing 4
nameshort = x[0:4]
print(nameshort)

# Its only print index no 2 as you can see in the output
character1 = x[2]
print(character1)

#Negative slicing of strings
nslice = x[-5 : -1] 
print(nslice)

#Slice skiping in string 
#Understand here focus on 2. 2 is basically skiping the character in a string 
# from the selected indexing the given string[1:4]
skip =x[0:4:2]
print(skip)