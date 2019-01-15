import turtle
import time
import random
from ball import Ball

turtle.tracer(0,0)
turtle.hideturtle()

global running 
running = True 
global sleep
sleep= 0.0077
global screen_width
screen_width= turtle.getcanvas().winfo_width()/2
global screen_height
screen_height= turtle.getcanvas().winfo_height()/2

my_ball=Ball(0,0,2,2,50,"blue")


number_of_balls=5
minimum_ball_radius=10
maximum_ball_radius=60
minimum_ball_dx=-5
maximum_ball_dx=5
minimum_ball_dy=-5
maximum_ball_dy=5
balls=[]

for i in range(number_of_balls):
	x= random.randint(-screen_width+maximum_ball_radius,screen_width-maximum_ball_radius)
	y=random.randint(-screen_height+maximum_ball_radius,screen_height-maximum_ball_radius)
	dx=0
	while dx==0:
		dx=random.randint(minimum_ball_dx,maximum_ball_dx)
	dy=0
	while dy==0:
		dy=random.randint(minimum_ball_dy,maximum_ball_dy)
	radius=random.randint(minimum_ball_radius,maximum_ball_radius)
	color=(random.random(),random.random(),random.random())
	new_ball= Ball(x,y,dx,dy,radius,color)
	balls.append(new_ball)

def timer():
    global n
    n = n - 1
    clock.penup()
    clock.hideturtle()
    clock.goto(0,300)
    clock.clear()
    clock.write(str(n), move = True, align = 'center', font=("Times New Roman",30,"normal"))
    if n == 0:
        print("Your battery ran out! Good luck next time!")
        quit()
    turtle.ontimer(timer, 1000)

def move_all_balls():
	for ball in balls:
		ball.move(screen_width,screen_height)

def collide(ball1,ball2):
	if ball1==ball2:
		return False 
	x1=ball1.xcor()
	x2=ball2.xcor()
	y1=ball1.ycor()
	y2=ball2.ycor()
	d=((x1-x2)**2 + (y1-y2)**2)**0.5
	if ball1.r+ball2.r >= d:
		return True
	else:
		return False

def check_all_ball_collision():
	for ball1 in balls:
		for ball2 in balls:
			if collide(ball1,ball2):
				rad1= ball1.r
				rad2= ball2.r
				x= random.randint(-screen_width+maximum_ball_radius,screen_width-maximum_ball_radius)
				y= random.randint(-screen_height+maximum_ball_radius,screen_height-maximum_ball_radius)
				dx=random.randint(minimum_ball_dx,maximum_ball_dx)
				dy=random.randint(minimum_ball_dy,maximum_ball_dy)
				radius=random.randint(minimum_ball_radius,maximum_ball_radius)
				color=((random.random(),random.random(),random.random()))

				if rad1>=rad2:
					if ball1.r < maximum_ball_radius:
						ball1.r+=1
						ball1.shapesize(ball1.r/10)
					ball2.shapesize(radius/10)
					ball2.r=radius
					ball2.penup()
					ball2.goto(x,y)
					ball2.shape("circle")
					ball2.color(color)
					ball2.x=x
					ball2.y=y
					ball2.dx=dx
					ball2.dy=dy
				else:
					if ball2.r < maximum_ball_radius:
						ball2.shapesize(ball2.r/10)
						ball2.r+=1
					ball1.shapesize(radius/10)
					ball1.r=radius
					ball1.penup()
					ball1.goto(x,y)
					ball1.shape("circle")
					ball1.color(color)
					ball1.x=x
					ball1.y=y
					ball1.dx=dx
					ball1.dy=dy
			else:
				print("no collide ")

def check_myball_collision():
	for ball in balls:
		if collide(my_ball,ball):
			rad1=my_ball.r
			rad2=ball.r
			x= random.randint(-screen_width+maximum_ball_radius,screen_width-maximum_ball_radius)
			y= random.randint(-screen_height+maximum_ball_radius,screen_height-maximum_ball_radius)
			dx=0
			while dx==0:
				dx=random.randint(minimum_ball_dx,maximum_ball_dx)
			dy=0
			while dy==0:
				dy=random.randint(minimum_ball_dy,maximum_ball_dy)
			radius=random.randint(minimum_ball_radius,maximum_ball_radius)
			color=(random.random(),random.random(),random.random())
			if rad2>=rad1:
				return False
			else:
				my_ball.r+=1
				my_ball.shapesize((rad1+1)/10)
				ball.shapesize(rad2/10)
				ball.r=radius
				ball.penup()
				ball.goto(x,y)
				ball.shape("circle")
				ball.color(color)
				ball.x=x
				ball.y=y
				ball.dx=dx
				ball.dy=dy
	return True


def movearound(event):
	x=event.x-screen_width
	y=screen_height-event.y
	my_ball.goto(x,y)

turtle.getcanvas().bind("<Motion>",movearound)
turtle.listen()

while running:
	screen_width= int(turtle.getcanvas().winfo_width()/2)
	screen_height= int(turtle.getcanvas().winfo_height()/2)
	move_all_balls()
	check_all_ball_collision()
	running=check_myball_collision()
	turtle.update()
	time.sleep(sleep)











