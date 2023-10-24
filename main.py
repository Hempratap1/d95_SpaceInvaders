import random
import time
import turtle
import winsound

player_dx = 15
bullet_speed = 15
invader_speed = 2
score = 0
level = 1


def move_left():
    x = player.xcor() - player_dx
    if x < -190:
        x = -190
    player.setx(x)


def move_right():
    x = player.xcor() + player_dx
    if x > 190:
        x = 190
    player.setx(x)


def fire_bullet():
    winsound.PlaySound("sounds/laser.wav", winsound.SND_ASYNC)
    x = player.xcor()
    y = player.ycor()
    bullet.setposition(x=x, y=y+30)
    bullet.showturtle()


# set up window
wn = turtle.Screen()
wn.setup(width=540, height=540)
wn.bgcolor("black")
wn.title("space invaders")

# drawing a border
border = turtle.Turtle()
border.speed(0)
border.color("white")
border.penup()
border.setposition(-200, -200)
border.pendown()
border.pensize(3)
for side in range(4):
    border.forward(400)
    border.left(90)
border.hideturtle()

# register shape
turtle.register_shape("images/rocket.gif")
turtle.register_shape("images/alien.gif")

# create the player
player = turtle.Turtle()
player.shape("images/rocket.gif")
player.penup()
player.speed(0)
player.setposition(0, -180)
player.setheading(90)

# create the scoreboard
scoreboard = turtle.Turtle()
scoreboard.speed(0)
scoreboard.color("white")
scoreboard.penup()
scoreboard.setposition(-200, 200)
scoreboard.write(f"Score : {score}", align="left", font=("Arial", 18, "normal"))
scoreboard.setposition(200, 200)
scoreboard.write(f"Level : {level}", align="right", font=("Arial", 18, "normal"))
scoreboard.hideturtle()


# create player bullets
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.up()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(.5, .5)
bullet.hideturtle()

# create the invader
invader = turtle.Turtle()
invader.shape("images/alien.gif")
invader.penup()
invader.speed(0)
invader.setposition(-180, 180)

# create keyboard bind
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space ")


while True:
    invader.forward(invader_speed)

    if invader.xcor() > 190 or invader.xcor() < -190:
        invader.right(180)
        invader.forward(invader_speed)

    bullet.forward(bullet_speed)

    if abs(bullet.xcor()-invader.xcor()) < 15 and abs(bullet.ycor()-invader.ycor()) < 15:
        winsound.PlaySound("sounds/explosion.wav", winsound.SND_ASYNC)
        bullet.hideturtle()
        invader.hideturtle()

        # update scoreboard
        invader_speed += 1
        score += 1
        level += 1
        scoreboard.clear()
        scoreboard.setposition(-200, 200)
        scoreboard.write(f"Score : {score}", align="left", font=("Arial", 18, "normal"))
        scoreboard.setposition(200, 200)
        scoreboard.write(f"Level : {level}", align="right", font=("Arial", 18, "normal"))

        time.sleep(2)
        invader.showturtle()

        x = float(random.randint(-180, 180))
        invader.setposition(x=x, y=180)

        player.setposition(0, -180)
