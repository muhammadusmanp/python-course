color = ['Red', 'Blue', 'Green']
print(color)
print("length of color is",len(color)) # length of list
print("type of color is", type(color))
color.append("Gray") # we can add item at the end of the list by append method
print("this is updated color list", color)
print(color[(0)]) # positive index
print(color[(1)])
print(color[-1]) #negative index

marks = [90, 80, 73, 49, 59, 53] # list of marks
print(marks) # print marks
print(len(marks))  # length of list
print(marks.append(70)) # add at the end of the list
print(marks,len(marks)) 
# How to define a list 
user_list = ["usman", "numan", "faisal", "rizwan"]
print(user_list)

# How to get values from list ?
print(user_list[0])
print(user_list[1])
# adding item to the list
print(user_list.append("adil"))
print(user_list)
# How to delete values from the list ?
print(user_list.remove("numan"))
print(user_list)
# How to modify values from a list ?
user_list[3] = "Adil"
print(user_list)