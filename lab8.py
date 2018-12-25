import turtle
from turtle import turtle
import random
import math

class Ball(Turtle):
	def __init__ (self,radius,color,speed,dx,dy):
		Turtle.__init__(self)
		self.shape("circle")
		self.shapesize(radius/10)
		self.radius= radius
		self.color(color)
		self.speed(speed)
		self.dx= dx
		self.dy=dy
	def border(self):
		high= 300
		low= 300
		right=300
		left= 300
		if self.xcor()> right or self.xcor()< left or self.ycor() >high or self.ycor()< low:
			self.dx= -self.dx
			self.dy= -self.dy

	def move(self):
		self.goto(self.xcor()+self.dx, self.ycor()+ self.dy)
turtle.penup()
turtle.pensize(5)
turtle.goto(300,500)
turtle.speed(0)


def check_collision(ball1, ball2):
	x1=ball1.xcor()
	y1=ball1.ycor()
	x2=ball2.xcor()
	y2=ball.ycor()


turtle.mainloop()
