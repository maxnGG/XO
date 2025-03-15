import turtle
#setup
wind = turtle.Screen()
wind.title('Ping Pong')
wind.bgcolor("black")
wind.setup(width=800, height=600)
wind.tracer(0)

#Score
redP = 0
greenP = 0
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)



#md1
madrab1 = turtle.Turtle()
madrab1.speed(0)
madrab1.shape("square")
madrab1.color("green")
madrab1.penup()
madrab1.goto(-350, 0)
madrab1.shapesize(stretch_wid=5 ,stretch_len=1)
#md2
madrab2 = turtle.Turtle()
madrab2.speed(0)
madrab2.shape("square")
madrab2.color("red")
madrab2.penup()
madrab2.goto(350, 0)
madrab2.shapesize(stretch_wid=5 ,stretch_len=1)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 1
ball.dy = 1


#mds movement
def madrab1_Up():
    y = madrab1.ycor()
    y += 20
    madrab1.sety(y)
def madrab1_Down():
    y = madrab1.ycor()
    y -= 20
    madrab1.sety(y)
def madrab2_Up():
    y = madrab2.ycor()
    y += 20
    madrab2.sety(y)
def madrab2_Down():
    y = madrab2.ycor()
    y -= 20
    madrab2.sety(y)


wind.listen()
wind.onkeypress(madrab1_Up, "z")
wind.onkeypress(madrab1_Down, "s")
wind.onkeypress(madrab2_Up, "Up")
wind.onkeypress(madrab2_Down, "Down")



while True:
    wind.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    if ball.xcor() == 390:
        greenP += 1
        ball.goto(0, 0)
        ball.dx *= -1
        score.clear()
        score.write("Green:" + str(greenP) + " Red:" + str(redP), align="center", font=("Courier", 20, "normal"))
    elif ball.xcor() == -390:
        redP += 1
        ball.goto(0, 0)
        ball.dx *= -1
        score.clear()
        score.write("Green:" + str(greenP) + " Red:" + str(redP), align="center", font=("Courier", 20, "normal"))

    if ball.ycor() == 290 or ball.ycor() == -290:
        ball.dy *= -1

    if ball.xcor() == madrab2.xcor() - 20 and madrab2.ycor() +25> ball.ycor() -10 and ball.ycor() + 10 > madrab2.ycor() -25 :
        ball.dy *= -1
        ball.dx *= -1

    if ball.xcor() == madrab1.xcor() + 20 and madrab1.ycor() +25> ball.ycor() -10 and ball.ycor() + 10 > madrab1.ycor() -25 :
        ball.dy *= -1
        ball.dx *= -1

