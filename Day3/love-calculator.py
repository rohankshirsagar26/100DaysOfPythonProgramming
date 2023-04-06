print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")


T = name1.lower().count("t") + name2.lower().count("t")
R = name1.lower().count("r") + name2.lower().count("r")
U = name1.lower().count("u") + name2.lower().count("u")
E = name1.lower().count("e") + name2.lower().count("e")

TRUE = T + R + U + E

L = name1.lower().count("l") + name2.lower().count("l")
O = name1.lower().count("o") + name2.lower().count("o")
V = name1.lower().count("v") + name2.lower().count("v")
E = name1.lower().count("e") + name2.lower().count("e")

LOVE = L + O + V + E

score = TRUE * 10 + LOVE

if score < 10 or score > 90:
    print(f'Your score is {score}, you go together like coke and mentos.')
elif score >=40 and score <=50:
    print(f'Your score is {score}, you are alright together.')
else:
    print(f'Your score is {score}.')