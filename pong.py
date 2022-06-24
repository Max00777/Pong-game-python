#Pong by EnatsuCode

import turtle


wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800,height=600)
wn.tracer(0)

#Score
scoreA = 0
scoreB = 0

# Paddle 1
pad_a = turtle.Turtle()
pad_a.speed(0)
pad_a.shape("square")
pad_a.color("white")
pad_a.shapesize(stretch_wid=5, stretch_len=1)
pad_a.penup()
pad_a.goto(-350, 0)

# Paddle 2
pad_b = turtle.Turtle()
pad_b.speed(0)
pad_b.shape("square")
pad_b.color("white")
pad_b.shapesize(stretch_wid=5, stretch_len=1)
pad_b.penup()
pad_b.goto(350, 0)

# Ball
ba = turtle.Turtle()
ba.speed(0)
ba.shape("square")
ba.color("white")
ba.penup()
ba.goto(0, 0)
ba.dx = 0.08
ba.dy = 0.08


# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)

# function
def pad_a_up():
    y = pad_a.ycor()
    y += 20
    pad_a.sety(y)
def pad_a_down():
    y = pad_a.ycor()
    y -= 20
    pad_a.sety(y)
def pad_b_up():
    y = pad_b.ycor()
    y += 20
    pad_b.sety(y)
def pad_b_down():
    y = pad_b.ycor()
    y -= 20
    pad_b.sety(y)

# Keyboard
wn.listen()
wn.onkeypress(pad_a_up, "z")
wn.onkeypress(pad_a_down, "s")
wn.onkeypress(pad_b_up, "Up")
wn.onkeypress(pad_b_down, "Down")

# Game loop

while True:
    wn.update()

    ba.setx(ba.xcor() + ba.dx)
    ba.sety(ba.ycor() + ba.dy)
    
    if ba.ycor() > 290:
        ba.sety(290)
        ba.dy *= -1
    
    if ba.ycor() < -290:
        ba.sety(-290)
        ba.dy *= -1
        
    if ba.xcor() > 390:
        ba.goto(0, 0)
        ba.dx *= -1
        scoreA += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(scoreA, scoreB),  align="center", font=("Courier", 24, "normal"))
    if ba.xcor() < -390:
        ba.goto(0, 0)
        ba.dx *= -1
        scoreB += 1 
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(scoreA, scoreB),  align="center", font=("Courier", 24, "normal"))

    if ba.xcor() > 350 and (pad_b.ycor() + 40 > ba.ycor() > pad_b.ycor() - 40):
        ba.setx(340)
        ba.dx *= -1
    if ba.xcor() < -350 and (pad_a.ycor() + 40 > ba.ycor() < -pad_a.ycor() - 40):
        ba.setx(-340)
        ba.dx *= -1
