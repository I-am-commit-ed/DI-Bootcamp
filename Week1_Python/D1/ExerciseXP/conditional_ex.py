# Ask the user
number = int(input("Please enter a number between 1 and 100: "))

# Check conditions
if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
elif number % 3 == 0:
    print("Fizz")
elif number % 5 == 0:
    print ("Buzz")
else:
    print(number)