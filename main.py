# Function with keyword aruguents (without positional arguments)

def canVote(name, age):
    if age >= 18:
        print(f"Hi {name} you are eligible to vote")
    else:
        print(f"Hey {name} you are NOT eligible to vote")

canVote(name = "Deepika", age = 32)
canVote(age = 17, name = "Alia")