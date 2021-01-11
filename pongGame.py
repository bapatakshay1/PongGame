import turtle

# Create screen
sc = turtle.Screen()
sc.title("Ping Pong game")
sc.bgcolor("white")
sc.setup(width=1000, height=600)

# Left paddle
left_pad = turtle.Turtle()# we just assigned the left paddle to another object named turtle
left_pad.speed(0)#it will intially move at speed zero
left_pad.shape("square")#it will have a black square shape and will move a certain speed as well.
left_pad.color("black")
left_pad.shapesize(stretch_wid=6, stretch_len=2)
left_pad.penup()
left_pad.goto(-400, 0)
right_pad = turtle.Turtle()# wejust assigned the right paddle to object turtle
right_pad.speed(0)#we indicate that it starts at no speed and we indicate its initial shape
right_pad.shape("square")
right_pad.color("black")
right_pad.shapesize(stretch_wid=6, stretch_len=2)
right_pad.penup()
right_pad.goto(400, 0)
hit_ball = turtle.Turtle()#we create a new ball objecct
hit_ball.speed(40)#we assign it to a speed
hit_ball.shape("circle")#we change the shape and color of it
hit_ball.color("blue")
hit_ball.penup()
hit_ball.goto(0, 0)
hit_ball.dx = 5#we also assign it a movement when it gets hit
hit_ball.dy = -5
left_player = 0
right_player = 0
sketch = turtle.Turtle()
sketch.speed(0)
sketch.color("blue")
sketch.penup()
sketch.hideturtle()
sketch.goto(0, 260)
sketch.write("Left_player : 0    Right_player: 0",
             align="center", font=("Times", 24, "normal"))
def paddleaup():
    y = left_pad.ycor()
    y += 20
    left_pad.sety(y)
def paddleadown():
    y = left_pad.ycor()
    y -= 20
    left_pad.sety(y)
def paddlebup():
    y = right_pad.ycor()
    y += 20
    right_pad.sety(y)
def paddlebdown():
    y = right_pad.ycor()
    y -= 20
    right_pad.sety(y)
sc.listen()
sc.onkeypress(paddleaup, "e")
sc.onkeypress(paddleadown, "x")
sc.onkeypress(paddlebup, "Up")
sc.onkeypress(paddlebdown, "Down")

while True:#this function allows us to play the game while running and will constantly update to see that all the requirements are satisfied
    sc.update()
    hit_ball.setx(hit_ball.xcor() + hit_ball.dx)
    hit_ball.sety(hit_ball.ycor() + hit_ball.dy)
    # Checking borders
    if hit_ball.ycor() > 280:
        hit_ball.sety(280)
        hit_ball.dy *= -1
    if hit_ball.ycor() < -280:
        hit_ball.sety(-280)
        hit_ball.dy *= -1

    if hit_ball.xcor() > 500:
        hit_ball.goto(0, 0)
        hit_ball.dy *= -1
        left_player += 1
        sketch.clear()
        sketch.write("Left_player : {}    Right_player: {}".format(
            left_player, right_player), align="center",
            font=("Courier", 24, "normal"))
    if hit_ball.xcor() < -500:
        hit_ball.goto(0, 0)
        hit_ball.dy *= -1
        right_player += 1
        sketch.clear()
        sketch.write("Left_player : {}    Right_player: {}".format(
            left_player, right_player), align="center",
            font=("Courier", 24, "normal"))
    if (hit_ball.xcor() > 360 and hit_ball.xcor() < 370) and (hit_ball.ycor() < right_pad.ycor() + 40 and hit_ball.ycor() > right_pad.ycor() - 40):
        hit_ball.setx(360)
        hit_ball.dx *= -1

    if (hit_ball.xcor() < -360 and hit_ball.xcor() > -370) and (hit_ball.ycor() < left_pad.ycor() + 40 and hit_ball.ycor() > left_pad.ycor() - 40):
        hit_ball.setx(-360)
        hit_ball.dx *= -1
