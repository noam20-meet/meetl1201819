import turtle
import time
import random
import ball
from ball import Ball

turtle.tracer(1)
turtle.hideturtle()

running= True 
sleep= 0.0077
screen_widht= turtle.getcanvas().winfo_width()/2
screen_height= turtle.getcanvas().winfo_height()/2

my_ball=Ball(0,0,2,2,50,"blue")
ball1=Ball(0,0,4,4,30,"pink")

number_of_balls=5
minimum_ball_radius=10
maximum_ball_radius=100
minimum_ball_dx=-5
maximum_ball_dx=5
minimum_ball_dy=-5
maximum_ball_dy=5

balls=[]

for i in range(number_of_balls):
	x= random.randint(-screen_widht+maximum_ball_radius,screen_widht-maximum_ball_radius)
	y=random.randint(-screen_height+maximum_ball_radius,screen_height-maximum_ball_radius)
	dx=random.randint(minimum_ball_dx,maximum_ball_dx)
	dy=random.randint(minimum_ball_dy,maximum_ball_dy)
	radius=random.randint(minimum_ball_radius,maximum_ball_radius)
	color=(random.random(),random.random(),random.random())





turtle.mainloop()