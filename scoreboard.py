# from turtle import Turtle
# class Scoreboard(Turtle):
#     def __init__(self):
#         self.score = 0
#         super().__init__()
#         self.color("white")
#         self.penup()
#         self.hideturtle()
#         self.goto(0,270)
#         self.update_scoreboard()
#     def update_scoreboard(self):
#         self.write(align="center", font=("Verdana", 15, "normal"),arg=f"Score: {self.score}")

#     def increase_score(self):
#         self.score += 1
#         self.clear()
#         self.update_scoreboard()

#     def game_over(self):
#         self.penup()
#         self.goto(0,0)
#         self.write(align="center",font = ("Verdana", 15,"normal"),arg="GAME OVER")

from turtle import Turtle


ALIGNMENT = 'center'
FONTS = ("Verdana", 15, "normal")
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score= int(data.read())
        print('a')

        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 270)

        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(align=ALIGNMENT, move=False, font=FONTS, arg=f"Score: {self.score} High-Score: {self.high_score}")

    def increase_score(self):
        self.score += 1    
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt",mode="w") as data:
                data.write(f"{self.high_score}")
                
        self.score = 0    
        self.update_scoreboard()    


    # def game_over(self):
    #     self.penup()
    #     self.goto(0,0)
        
    #     self.write(align=ALIGNMENT,move=False, font=FONTS, arg="Game Over" )