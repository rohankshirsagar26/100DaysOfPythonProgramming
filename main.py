# While loop

# Reeborg Challenege

https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%202&url=worlds%2Ftutorial_en%2Fhurdle2.json

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
    
number_of_hurdles = 6
   
while number_of_hurdles > 0:
    one_hurdle()
    if at_goal() == 'true':
        number_of_hurdles = 0
    number_of_hurdles -= 1