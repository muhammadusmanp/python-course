# Print numbers from 1 to 10 using a for loop.
for i in range(1, 11):
    print(i)

# Print numbers from 1 to 5 using a while loop.
i = 1
while i <= 5:
    print(i)
    i += 1

# Ask the user for a number and use a while loop to count down to 1
number  = int(input("Enter a number :"))
while number >= 1:
    print(number)
    number -= 1
# Print a mini multiplication table for numbers 1 to 3
count = 1
for i in range(1, 4):
    for j in range(1, 4):
        # Calculate the result
        result = i * j
        print(f"{count}. {i} x {j} = {result}")
        count += 1
# Use a loop to print numbers from 0 to 10.
# Stop the loop when the number reaches 6 using break.
number = [1,2,3,4,5,6,7,8,9,10]
for num in number:
    if num == 6:
        break
    print(num)

# Use a loop to print numbers from 0 to 5, but skip number 3
numbers = [1,2,3,4,5]
for numb in numbers:
    if numb == 3:
        continue
    print(numb)
# Ask the user to enter a word.
#  Use a for loop to print each letter on a new line.
word = str(input("Enter a word :"))
for i in word:
    print(i)