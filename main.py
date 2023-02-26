# Reeborg Challenge

https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

# Python Code

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def step_one():
    move()
    turn_left()
    move()
    turn_right()

def step_two():
    move()
    turn_right()
    move()
    turn_left()

def one_hurdle():
    step_one()
    step_two()

for step in range(6):
    one_hurdle()