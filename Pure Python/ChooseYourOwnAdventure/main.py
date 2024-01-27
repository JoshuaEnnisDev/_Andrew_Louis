

# Data types
    # String -- anything inside quotes 

# function to display text on the screen
print("Choose your own adventure")


# function that allows the user to type into the program
name = input("What is your name? ") 

# words without quotes are variables
# variables store data and they give data meaning

print("Hello " + name + ". Welcome to the game!")
print()
print("You wake up at your house. Your head is hurting.")
print("You notice blood spatter on the door.")

answer = input("Do you want to inspect the door?(Y/N)").upper()

# check IF the answer is Y
if answer == "Y":
    print("You find the blood is dry, and you see a handprint in it.")
    answer = input("Do you walk out the door or turn around?")
    if "door" in answer:
        print("You walk out the door")
else:
    print("A man comes out from the other room and attacks you.")
    

