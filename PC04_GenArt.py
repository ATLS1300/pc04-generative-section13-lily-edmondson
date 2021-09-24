"""
Created on Thu Sep 15 11:39:56 2020
PC04 start code
@author: JoJo Rinzler & Lily Edmondson

********* HEY, READ THIS FIRST **********
Our code depicts a circle of circles and a circle of triangles. 
The circle represents a smooth easy life going round and round. 
The triangle represents ups and downs in life.
Both change colors indicating new beginnings. 
In whole, its the circle of life that is commonly spoken about 
with an added triangle of life that is somewhat taboo to talk about but is very much prevalent in everyones lives
"""

import turtle
import math, random

turtle.colormode(255)
# turtle.tracer(0) # uncomment this line to turn off turtle's animation. You must update the image yourself using panel.update() (line 42)

# Create a panel to draw on. 
panel = turtle.Screen()
w = 600 # width of panel
h = 600 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making 

# You must make 2 turtle variables
# You must use 2 for loops (a nested for loop counts as 2!)
# You must use at least 1 random element (something from the random library)
# Don't forget to comment your code! (what does each for loop do? What does the random function you'll use do?)

# =============== ADD YOUR CODE BELOW! =================

spin = turtle.Turtle() # first turtle
spin.up()
spin.speed(20)
spin.goto(-150,150)
palette = ("red", "orange", "yellow", "green", "blue", "indigo", "violet")
rainbow = palette

inc = 15 # angle increment between shapes in pattern
numInt = int(360/inc) # the number of iterations to make a complete cirlce
innerCirc = 15 # radius of inner circle
radius = 40 # radius of circle drawn in pattern

spin.color(random.choice(rainbow))

for i in range(numInt):
    spin.down()
    spin.circle(radius)
    spin.forward(innerCirc)
    spin.right(inc)
    
spin.up()

# second shape

cone = turtle.Turtle() # first turtle
cone.up()
cone.speed(15)
cone.goto(60,-150)
palette = ("red", "orange", "yellow", "green", "blue", "indigo", "violet")
rainbow = palette

cone.color(random.choice(rainbow)) # takes colors from our palette to randomize each time the code is run

# modified from https://www.pythonclassroom.com/turtle-graphics/turtle-graphics-with-loops
for i in range(13): # 20% or less other code
        cone.down()
        cone.forward(200)
        cone.left(150)
    
cone.up()

# panel.update() # uncomment this if you've turned off animation (line 26). I recommend leaving this outside of loops, for now.
# =================== CLEAN UP =========================
# uncomment the line below when you are finished with your code (before you turn it in)
# turtle.done()