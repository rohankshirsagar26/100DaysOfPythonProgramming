# Import class from a module

from turtle import Turtle, Screen

# Create Object from Blueprint
timmy = Turtle()
print(timmy)

# Access attributes of Class
my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()

# Call methods associated with Object
timmy.shape("turtle")
timmy.color("green")
timmy.forward(100)
