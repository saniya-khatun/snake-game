# import random
# from turtle import Turtle
# class Food(Turtle):
#     def __init__(self):
#         super().__init__()
#         self.shape("circle")
#         self.color("white")
#         self.penup()
#         self.shapesize(stretch_wid=0.5 , stretch_len=0.5)
#         self.speed(0)
#         self.refresh()

#     def refresh(self):
#         randomx = random.randint(-280,280)
#         randomy = random.randint(-280,280)
#         self.goto(randomx,randomy)

from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("orange")
        self.speed(0)
        self.refresh()
        

    def refresh(self):    
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)