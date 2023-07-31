# from snake import Snake
# from turtle import Screen
# from food import Food
# from scoreboard import Scoreboard
# import time

# screen = Screen()
# screen.tracer(10)
# screen.setup(width=600,height=600)
# screen.bgcolor("black")

# snake = Snake()
# food = Food()
# scoreboard = Scoreboard()

# screen.listen()
# screen.onkey(snake.up , "Up")
# screen.onkey(snake.down,"Down")
# screen.onkey(snake.left ,"Left")
# screen.onkey(snake.right ,"Right")

# game_is_on = True
# while game_is_on:
#     screen.update()
#     time.sleep(0.1)
    

#     snake.move()
#     if snake.head.distance(food) < 15:
#         food.refresh()
        
#         snake.extend()
#         scoreboard.increase_score()


#     #detect collision with wall
#     if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
#         game_is_on = False
#         scoreboard.game_over()


#     #detect collision with tail
#     for segment in snake.segments[1:]:
#         if snake.head.distance(segment) < 10:
#             # if snake.head == segment:
#             #     pass
#             # else:
#             game_is_on = False
#             scoreboard.game_over()






# screen.exitonclick()

from turtle import  Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen =Screen()
screen.setup(width=600, height=600)
screen.title("snake game")
screen.bgcolor("black")
screen.tracer(10)


snake = Snake()
food = Food()
scoreboard= ScoreBoard()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    snake.move()

    # detect collision with food using distance method
    if snake.head.distance(food) < 15:
           # print('detect')
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #detect collision with wall         ss
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or  snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset_snake()
        # game_is_on = False
        # scoreboard.game_over()

    # detect collision with tail:  
    # if head collides with any of the segments of the snake then game over
    for segment in snake.segments[1:]:
        # if segment == snake.head:
        #     pass
        if snake.head.distance(segment) < 10:
            pass
            # game_is_on = False
            # scoreboard.game_over() 
        

screen.exitonclick()