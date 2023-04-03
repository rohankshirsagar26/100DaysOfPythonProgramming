# Function with inputs

def canVote(name):
    age = int(input(f"Hey {name}, how old are you? "))
    if age >= 18:
        print(f"Hi {name} you are eligible to vote")
    else:
        print(f"Hey {name} you are not eligible to vote")

canVote("John Doe")