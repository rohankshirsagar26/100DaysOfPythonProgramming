# While loop

https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json

# Reeborg Challenege Hurdle 4

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def skip_wall():
    count = 0
    turn_left()
    while not right_is_clear():
        move()
        count+=1
    turn_right()
    move()
    turn_right()
    while not count==0:
        move()
        count-=1
    turn_left()
   
while not at_goal():
    if wall_in_front():
        skip_wall()
    elif front_is_clear():
        move()