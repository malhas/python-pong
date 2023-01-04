from turtle import Turtle

class scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.ht()
        self.player_score = 0
        self.pc_score = 0
        self.write_score()


    def write_score(self):
        self.clear()
        self.sety(265)
        self.write(arg="Score", move=False, align='center', font=('Arial', 24, 'normal'))
        self.sety(230)
        self.write(arg=f"PC {self.pc_score} | PL {self.player_score}", move=False, align='center', font=('Arial', 24, 'normal'))        

    def inc_player_score(self):
        self.player_score += 1
        self.write_score()

    def inc_pc_score(self):
        self.pc_score += 1
        self.write_score()   