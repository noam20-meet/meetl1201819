from turtle import *

#create a class
class Ball(Turtle):
	def __init__ (self,x,y,dx,dy,r,color):
		Turtle.__init__(self)
		self.penup()
		self.goto(x,y)
		self.shape("circle")
		self.shapesize(r/10)
		self.color(color)
		self.dx=dx
		self.dy=dy
		self.r=r
#defying method that move the ball
	def move(self,screen_width,screen_height):
		current_x= self.xcor()
		current_y=self.ycor()
		new_x=current_x+self.dx
		new_y=current_y+self.dy
		right_side_ball=new_x+self.r
		left_side_ball=new_x-self.r
		up_side_ball=new_y+self.r
		down_side_ball=new_y-self.r
		self.goto(new_x,new_y)
#defying the ball borders
		if (up_side_ball>=screen_height) or (down_side_ball<=-screen_height):
			self.dy= -self.dy
		elif (right_side_ball>=screen_width) or (left_side_ball<=-screen_width):
			self.dx= -self.dx




