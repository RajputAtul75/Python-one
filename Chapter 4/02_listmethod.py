# In this program we were using list methods

friends = ["Grapes", "Mango", 55, 66.0, False, "Atul", "Topgun"]
#Normally print the all element present inside the list
print(friends)

# append method operate with (.append)
friends.append("Jack reacher")
# .append method just simply add the element in the last position of the list
print(friends)

List = [23,76,56,23,1,26,0,11]
# Use sort method for just sorting the element present inside the list
# This method is just simply change it into ascending order
List.sort()
print(List)
# Its just reverse the whole list immedielty 
List.reverse()
print(List)
#Insert method is used to insert the element at particular index
List.insert(3,  "Tom") # Basically "Tom" at index no 3 thats all
print(List)
# Pop method immediately remove the element at the particular index
List.pop(3)
print(List)
# Remove method simply eliminate the element inside the list
List.remove(76)
print(List)