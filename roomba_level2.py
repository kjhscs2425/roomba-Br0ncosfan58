# -----------------------------------------------------------------------------
# Roomba in Python
# This file implements an algorithm for a roomba cleaning a room.
#
# Author: Max Wasserstein
# -----------------------------------------------------------------------------
 
from turtle import right, left, forward, backward, speed
import room

# Make the turtle go faster
speed(7)

# Draw the Level 2 version of the room
window = room.draw_room(level = 2)

###
# Start your code here
forward(560)
left(90)
speed(10)
forward(760)
left(90)
forward(560)
left(90)
forward(720)
left(90)
forward(520)
left(90)
forward(680)
left(90)
forward(480)
left(90)
forward(640)
left(90)
forward(440)
left(90)
forward(600)
left(90)
forward(400)
left(90)
forward(560)
left(90)
forward(360)
left(90)
forward(520)
left(90)
forward(320)
left(90)
forward(480)
left(90)
forward(280)
left(90)
forward(440)
left(90)
forward(240)
left(90)
forward(400)
left(90)
forward(200)
left(90)
forward(360)
left(90)
forward(160)
left(90)
forward(320)
left(90)
forward(120)
left(90)
forward(280)
left(90)
forward(80)
left(90)
forward(240)
left(90)
forward(40)
left(90)
forward(200)
# End your code here
###
 
window.exitonclick()