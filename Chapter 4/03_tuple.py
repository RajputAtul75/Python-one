# Tuple is a immutable data type in python programming language

tuple = (2,6,8,9,12, False, 12, "Rohan", "Parash")
print(type(tuple))
print(tuple)
# tuple cannot be changed once is declare as a string because both are immutable data types

# Method of tuple
# .count method
no = tuple.count(12) # Count the number of 12 in tuple variable 
print(no)
# .index method
i = tuple.index(False)# Find the index of False in tuple variable
print(i)

# Concatenation of tuple using + operator we achive the concatenationo of tuple
tuple1 = (1,2,3)
tuple2 = (4,5,6)
# using (+) operator we can concatenate the tuple
tuple3 = tuple1 + tuple2
print(tuple3)

# Repetition of tuple using * opearator we can repeat the tuple
my_tuple = (1,2,3)
repeat = my_tuple * 3
print(repeat)
# length method
print(len(my_tuple)) # find the length of the my_tuple