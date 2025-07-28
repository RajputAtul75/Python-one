# A list can be  indexed just like a string

friends = ["Grapes", "Mango", 55, 66.0, False, "Atul", "Topgun"]
# It will print that element who supposed to present at index no 6 means Topgun
print(friends)
print(friends[6]) 

#Change the items in this list
# We can change the name element which are present inside the list,because list is muttable
friends[0] = "Apple"

print(friends[0])
# Slicing of the list
print(friends[1:3])