# Function with multiple inputs

def canVote(name, age):
    if age >= 18:
        print(f"Hi {name} you are eligible to vote")
    else:
        print(f"Hey {name} you are NOT eligible to vote")

canVote("Deepika", 32)