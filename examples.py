

# # class Animal:
# #     def __init__(self):
# #         self.eyes = 2



# #     def breathe(self):
# #         print("inhale , exhale")



# # class Fish(Animal):
# #     def __init__(self):
# #         super().__init__()
        
        

# #     def swim(self):
# #         print("moving in water")


# # fish = Fish()
# # fish.swim()
# # fish.breathe()
# # print(fish.eyes )


# class Homosapiens:
#     def __init__(self):
#         self.leg = 2
#         self.eyes = 2

# class Human(Homosapiens):
#     def __init__(self):
#         super().__init__()


# human = Human()
# print(human.eyes)
# print(human.leg)

# from turtle import Turtle

# starting_positions = [(0,0), (-20, 0), (-40,0)]
# MOVE_DISTANCE = 20
# UP =90
# DOWN = 270
# LEFT = 180
# RIGHT = 0
# class Snake:

#     def __init__(self):
#         self.segments = []
#         self.create_snake()
#         self.head= self.segments[0]
#     def create_snake(self):
#         for position in starting_positions:
#             self.add_segment(position)
          

#     def add_segment(self, position):
#         new_segment=Turtle("square")
#         new_segment.penup()
#         new_segment.color("white")
#         new_segment.goto(position)
#         self.segments.append(new_segment)


#     def extend(self):
#         self.add_segment(self.segments[-1].position())

#     def move(self):
#         for  seg_num in range(len(self.segments)-1, 0, -1):
#             new_x = self.segments[seg_num-1].xcor()
#             new_y = self.segments[seg_num-1].ycor()
#             self.segments[seg_num].goto(new_x,new_y)
#         self.head.forward(10)
#     def up(self):
#         if self.head.heading()!= DOWN:
#             self.head.setheading(UP)
#     def down(self):
#         if self.head.heading()!= UP:
#             self.head.setheading(DOWN)
#     def left(self):
#         if self.head.heading()!= RIGHT:
#             self.head.setheading(LEFT)
#     def right(self):
#         if self.head.heading()!=LEFT:
#             self.head.setheading(RIGHT)


  with open('data.txt') as data:

            self.high_score = int(data.read())



            with open('data.txt', mode='w') as data:
                data_text = data.write(f"{self.high_score}"