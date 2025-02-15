"""
7-1. Rental Car: Write a program that asks the user what kind of rental car they would like. 
Print a message about that car, such as “Let me see if I can find you a Subaru.”

"""

rentalCar = input("what choice of vehicle do you prefer? ")
print(f"we'll try out best of accommodate your choice of {rentalCar}\n")

"""
7-2. Restaurant Seating: Write a program that asks the user how many people are in their dinner group. 
If the answer is more than eight, print a message saying they’ll have to wait for a table. Otherwise, report that their table is ready.

"""

dinner_guest = int(input("How many people are in your party? "))
if dinner_guest <= 8: 
    print(f"we have room for {dinner_guest}! right this way please\n")
else: 
    print(f"your number of guest ({dinner_guest}) requires a wait time.\n")

"""
7.3 Multiples of Ten: Ask the user for a number, and then report whether the number is a multiple of 10 or not.

"""

number = int(input("enter a number to see if it's multiple by 10: "))
if number % 10 == 0:
    print(f"{number} is a multiple of 10.\n")
else: 
    print(f"{number} is not a multiple of 10.\n")

"""
7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. 
As they enter each topping, print a message saying you’ll add that topping to their pizza.

"""
choices = []
while True:
    topping = input("Enter your choice of toppings: ")
    
    if topping != 'quit': 
        print(f"Your topping choice of {topping.title()} has been added.\n")
        choices.append(topping)
    else: 
        break
print(f"Here are your selections:")
for choice in choices:
    print(choice)

print("\n")

""" 
Originally i had an infinity loops due to my input statement sitting out the loops and i didn't make quit a string. 
for extended practice: 
i added the topping choices into a list then looped through the list to be printed for the user to be reminded of what toppings were added.

"""

"""
7-5. Movie Tickets: A movie theater charges different ticket prices depending on a person’s age. 
If a person is under the age of 3, the ticket is free; if they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15. 
Write a loop in which you ask users their age, and then tell them the cost of their movie ticket.

"""
print("Welcome To Python Theater")
print("Prices:\nFree -\tUnder 3\n$10.00 -\tBetween 3 and 12\n$15.00 -\tOver 12\n")

guestTotal = int(input("How Tickets Will You Need? "))
tickets = 0
ages = []
total = 0
while tickets in range(guestTotal):
    age = int(input("Enter Movie Goer Age: "))
    if age < 3:
        print("This Person is Free\n")
        ages.append(age)
        total += 0
        tickets += 1
    elif age <= 12:
        print("$10.00 Added To Total\n")
        ages.append(age)
        total += 10
        tickets += 1
    else:
        print("$15.00 Added To Total\n")
        ages.append(age)
        total += 15
        tickets += 1

print("Ages Entered:")
for tickets, age in enumerate(ages, start=1):
    print(f"Ticket {tickets}: {age} years old")

print("\n")
print(f"Grand Total of ${total}\n")

print("\n")

"""
7-7. Infinity: Write a loop that never ends, and run it. 
(To end the loop, press CTRL-C or close the window displaying the output.)

"""
"""
count = 1
while count > 0:
    print("this will loop forever")

    
commented out to avoid the infinite loop.
"""

"""
7-8. Deli: Make a list called sandwich_orders and fill it with the names of various sandwiches. 
Then make an empty list called finished_sandwiches. 
Loop through the list of sandwich orders and print a message for each order, such as I made your tuna sandwich. As each sandwich is made, move it to the list of finished sandwiches. 
After all the sandwiches have been made, print a message listing each sandwich that was made.

"""

sandwichOrders = ['BLT','Big Mac', 'Club','PB&J','pastrami','pastrami','pastrami']
finishedSandwiches = []

while sandwichOrders:
    current = sandwichOrders.pop()
    print(f"I made you a {current.title()} sandwich!")
    finishedSandwiches.append(current)

print("\n")

for sandwich in finishedSandwiches:
    print(f"{sandwich}")

print("\n")

"""
7-9. No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times. 
Add code near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all occurrences of 'pastrami' from sandwich_orders. 
Make sure no pastrami sandwiches end up in finished_sandwiches.

"""

while 'pastrami' in finishedSandwiches:
    finishedSandwiches.remove('pastrami')

for sandwiches in finishedSandwiches:
    print(sandwich)

"""
7-10. Dream Vacation: Write a program that polls users about their dream vacation. 
Write a prompt similar to If you could visit one place in the world, where would you go?
 Include a block of code that prints the results of the poll.

"""
namePrompt = "\nWhat's your name? "
placePrompt = "If you could visit one place in the world, where would it be? "
continuePrompt = "\nWould you like to let someone else respond? (yes/no) "

responses = {}

while True:
    name = input(namePrompt)
    place = input(placePrompt)

    responses[name] = place

    repeat = input(continuePrompt)
    if repeat != 'yes':
        break

print("\n--- Results ---")
for name, place in responses.items():
    print(f"{name.title()} would like to visit {place.title()}.")