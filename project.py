responses = {}

polling = True
while polling:
    name = input("Enter your name: ")
    response = input("What's your dream vacation? ")
    responses[name] = response
    killingProgram = input("is anybody else? (yes/no) ")

    if killingProgram == 'no':
        polling = False
    else: 
        continue

for k,v in responses.items(): 
    print(f"Name: {k.title()}\tDream Vacation: {v.title()}")