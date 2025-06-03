from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time




screen = Screen()
screen.bgcolor("black")
screen.setup(800, 800)
screen.title("Prong")
screen.tracer(0)


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()



screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")



game_is_on = True




while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 380 or ball.ycor() < -380:
        ball.bounce_y()

    # paddle-ებზე დაჯახება
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        print("Right paddle hit")
        ball.bounce_x()

    elif ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        print("Left paddle hit")
        ball.bounce_x()

    # გოლი – როცა ბურთი გავა მარჯვნივ ან მარცხნივ
    if ball.xcor() > 380:
        print("Right side missed – LEFT player scores!")
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        print("Left side missed – RIGHT player scores!")
        ball.reset_position()
        scoreboard.r_point()

    
screen.exitonclick()
