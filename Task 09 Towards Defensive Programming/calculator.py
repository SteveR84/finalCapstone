"""
Part 1
Create simple calculator application.
Ask user for 2 numbers to import and the opperation -like + - / x (replace with *)
Display the answer.
Every equation emtered must be written to a text file.
Defensive programming must be used to catch unextected errors.

Part 2
as before 2 numbers and an opperator also to be able to read the previous equations from a text file.
the user needs to be albe to name the file and print all extations.
IT MUST NOT CRASH
if the file does not exist, the program must create one.
"""

# Constants
awaiting_input = True
continuing = True

# File naming
while True:
    file_name = input("Please name your file to save equations: ")
    try:
        with open(f"{file_name}.txt", "a") as file:
                file.write("Your Equations\n")
        break
    except:
        print("Please enter valid file name: ")


# while loop for inputting
while continuing == True:
    # Number one
    while awaiting_input == True:
        input_one = input("Please enter the first number: ")
        try:
            if float(input_one) + 1 > float(input_one):
                awaiting_input = False
        except:
            print("Please Enter Valid Number")
    number_one = (float(input_one))
    awaiting_input = True

    # Opperator

    while awaiting_input == True:
        opperator = input("Please add opperator: ")
        try:
            if opperator.lower() == "x" or opperator =="*" or opperator =="+" or opperator =="-" or opperator =="/":
                awaiting_input = False
        except:
            print("Opperator muse be add, plus, minus or devide")
    awaiting_input = True

    # Number two
    while awaiting_input == True:
        input_two = input("Please enter the second number: ")
        try:
            if float(input_two) + 1 > float(input_two):
                awaiting_input = False
        except:
            print("Please Enter Valid Number")
    number_two = (float(input_two))
    awaiting_input = True

    # Output and print

    if opperator.lower() == "x" or opperator == "*":
        print(f"{number_one} x {number_two} = {round((number_one * number_two),2)}")
        with open(f"{file_name}.txt", "a") as file:
            file.write(f"{number_one} x {number_two} = {round((number_one * number_two),2)}\n")

    elif opperator == "+":
        print(f"{number_one} + {number_two} = {round((number_one + number_two),2)}")
        with open(f"{file_name}.txt", "a") as file:
            file.write(f"{number_one} + {number_two} = {round((number_one + number_two),2)}\n")

    elif opperator == "-":
        print(f"{number_one} - {number_two} = {round((number_one - number_two),2)}")
        with open(f"{file_name}.txt", "a") as file:
            file.write(f"{number_one} - {number_two} = {round((number_one - number_two),2)}\n")

    elif opperator == "/":
        print(f"{number_one} / {number_two} = {round((number_one / number_two),2)}")
        with open(f"{file_name}.txt", "a") as file:
            file.write(f"{number_one} / {number_two} = {round((number_one / number_two),2)}\n")
    end = input("Type END to finish, any other input to add more numbers\n")
    if end.lower() == "end":
        continuing = False
        print(f"You can now view \"{file_name}.txt\" for all equations.\n")