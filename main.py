# Reeborg Challenge

https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

# Python Code

def step_one():
    move()
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()

def step_two():
    move()
    turn_left()
    turn_left()
    turn_left()
    move()
    turn_left()

for n in range(1, 13):
    if n%2==1:
        step_one()
    else:
        step_two()