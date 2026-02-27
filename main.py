import turtle
from random import randint

#turtle board
turtle_board = turtle.Screen()
turtle_board.bgcolor("light blue")
turtle_board.title("Catch The Turtle")

#turtle cursor
turtle_instance = turtle.Turtle()
turtle_instance.shapesize(2)
turtle_instance.shape("turtle")
turtle_instance.fillcolor("Green")
turtle_instance.penup()
turtle_instance.hideturtle()

#gameover
gameover = turtle.Turtle()
gameover.hideturtle()
gameover.penup()

#welcome
welcome = turtle.Turtle()
welcome.hideturtle()
welcome.penup()

score=0
countdown = 30

#countdown table
turtle_time= turtle.Turtle()
turtle_time.hideturtle()
turtle_time.penup()
turtle_time.goto(0, 320)

#score table
turtle_score = turtle.Turtle()
turtle_score.shapesize(5)
turtle_score.penup()
turtle_score.hideturtle()
turtle_score.goto(0, 300)

welcome.write("Welcome!\nTab Anywhere To Start", align="center", font=("Courier", 40, "bold"))

def countdownTime():
    global countdown
    countdown -= 1
    if (countdown == 0):
        turtle_board.clear()
        gameover.write("GAME OVER\nScore: " + str(score), align="center", font=("Courier", 40, "bold"))
        turtle.done()
    turtle_time.clear()
    turtle_time.write("Time " + str(countdown), align="center", font=("Courier", 20, "normal"))
    turtle.ontimer(countdownTime, 1000)

# increase points
def turtle_on_click(x,y):
    global score
    score += 1
    turtle_score.clear()
    turtle_score.write("Score: " + str(score), align="center", font=("Courier", 20, "normal"))

#random location
def turtle_move():
    if (countdown > 0):
        turtle_instance.hideturtle()
        turtle_instance.goto(randint(-300, 300), randint(-300, 300))
        turtle_instance.showturtle()
        turtle.ontimer(turtle_move, 500)

def gamestart(x,y):
    welcome.clear()
    turtle_board.onscreenclick(None)
    countdownTime()
    turtle_instance.showturtle()
    turtle_time.write("Time " + str(countdown), align="center", font=("Courier", 20, "normal"))
    turtle_score.write("Score: " + str(score), align="center", font=("Courier", 20, "normal"))
    turtle_instance.onclick(fun = turtle_on_click, btn=1, add=None)
    if countdown>0:
        turtle_move()

    turtle.mainloop()

turtle.onscreenclick(fun = gamestart, btn=1, add=None)
turtle.mainloop()