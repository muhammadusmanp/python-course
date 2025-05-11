firt_name = "Muhammad"
second_name = "Usman"
full_name = firt_name + " " + second_name
print(full_name)
# convert string into upper case 
name = "muhammad usman"
print(name.upper())
# convert string into lower case
city = "CHAKWAL"
print(city.lower())
# length of string
print("the length of string is",len(city))
# Converts the first character to upper case
language = "python"
print(language.capitalize())
# repeat the string
laugh = "ha"
repeat_string = "ha" * 5
print(repeat_string)
# split the string
i = "hi i am usman"
myself = i.split()
print(myself)
# join the string
greeting = ["hello", "usman", "how", "are", "you"]
greet = " ".join(greeting)
print(greet)
# join the string
student = ("Muhammad", "Usman", "is", "learning", "python")
learning = " ".join(student)
print(learning)
# replace string in python
student = "i love java"
teacher = student.replace("java", "python")
print(teacher)
# strip in python
whoami  = " usman "
print(whoami.strip())
# remove ! from string
programming = "python!!!!!!!!!!!!!!!!!!!!"
print(programming)
print(programming.rstrip("!"))