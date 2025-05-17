# Variable Naming Rules
# Must start with a letter or underscore (_)
# Can contain letters, numbers, and underscores (_)
# Are case-sensitive (Name and name are different)
# Can’t start with a number
# Can’t use spaces
# Can’t use special characters like @, $, %, 
# A string is a collection of characters enclosed within quotation marks (‘ ‘ or ” “).
name = "usman"
gretting = ("hello", name)
print(gretting)
age = 26  # An integer is a whole number without any decimal point.
print("i five year i will be",age + 5)

hight = 1.8  #in meters  # A float is a number that has a decimal point.
print("my hight is 1.8 meter")

item =  "chocholates" #string
Quantity = 10  # int
price = 500.99 # float
print(f"i bought {Quantity} {item} for a total of {price} Rupees")
student = True # this is bool data type True or False values only.
print(name,type(name)) #will print my name string
print(age,type(age)) # will print age it's int value
print(hight,type(hight)) # will print my hight it's float vlaue
print(student,type(student)) # will print True it's boolean value
# building a shopping program
user_name = input(str("Enter your name :"))
print("hello", user_name)
item = input("Enter the item you want to buy :")
quantity = int(input("Enter the quantity :"))
price = float(input("Enter the price of per item :"))
print(f"{user_name} you bought {quantity} {item}s. Total: price {price * quantity} Dollars")