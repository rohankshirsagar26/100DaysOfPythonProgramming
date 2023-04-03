# Basic Function

def canVote():
    name = input("Enter your name: ")
    age = int(input("How old are you? "))
    if age >= 18:
        print(f"Hi {name} you are eligible to vote")
    else:
        print(f"Hey {name} you are not eligible to vote")

canVote()