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

# Draw the Level 4 version of the room
window = room.draw_room(level = 4, n_alcoves = 1)

###
# Start your code here

 
 
# End your code here
###
 
window.exitonclick()