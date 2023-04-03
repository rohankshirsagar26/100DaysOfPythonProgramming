# Basic Function

def canVote():
    name = input("Enter your name: ")
    age = int(input("How old are you? "))
    if age >= 18:
        print(f"Hi {name} you are eligible to vote")
    else:
        print(f"Hey {name} you are not eligible to vote")

canVote()

# Function with inputs

def greet(name):
    age = int(input(f"Hey {name}, how old are you? "))
    if age >= 18:
        print(f"Hi {name} you are eligible to vote")
    else:
        print(f"Hey {name} you are not eligible to vote")

greet("John Doe")

# Function with multiple inputs

def canVote(name, age):
    if age >= 18:
        print(f"Hi {name} you are eligible to vote")
    else:
        print(f"Hey {name} you are NOT eligible to vote")

canVote("Deepika", 32)