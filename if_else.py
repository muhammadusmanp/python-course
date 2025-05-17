# this block of code check the voter age of print either you can vote or not.
age = int(input("Enter your age :"))
if age >= 18:
  print("You can vote")
else:
  print("You can not vote")
#  
driver_age = int(input("Enter your age :"))
print("Your age is :", driver_age)
if driver_age >= 18:
  print("you can drive the car")
else:
  print("You can not drive the car")

marks = 60
if marks >= 90:
  print("A+ Grade")
elif marks >= 75:
  print("B Grade")
elif marks >= 50:
  print("Grade C")
else:
  print("You are Fail !")

# Ask the user how they're feeling:

user_mood = input("what are you feeling :")
if user_mood == "happy":
    print("that is great to hear")
elif user_mood == "sad":
    print("i hope you day gets better")
elif user_mood == "bored":
    print("go for a walk")
else:
    print("Thanks for sharing your mood")