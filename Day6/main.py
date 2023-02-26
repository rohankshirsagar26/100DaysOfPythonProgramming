# Functions

def my_function():
  print('Hello')
  print('Bye')

my_function()

# Reeborg Challenege

https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

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
   
while not at_goal():
    one_hurdle()
    number_of_hurdles -= 1

# Reeborg Challenege with while and if

https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def skip_wall():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()   
   
while not at_goal():
    if wall_in_front():
        skip_wall()
    elif front_is_clear():
        move()