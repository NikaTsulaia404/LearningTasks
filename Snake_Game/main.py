from turtle import Screen
from snake import Snake
from food import Food
from score_board import Scoreboard
import time

# ეკრანის დაყენება
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")  
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")  

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #არეფრეშებს საჭმელს 
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #ამოწმებს შეეჯახე თუ არა კედელს
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor()> 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    #გველი თუ დაეჯახა კუდს თამაში მთავრდება
    for segmnet in snake.segments:
        if segmnet == snake.head:
            pass
        elif snake.head.distance(segmnet) < 10:
            scoreboard.reset()
            snake.reset()
          









screen.exitonclick()
