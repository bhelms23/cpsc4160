import Entities

class Model():
    def __init__(self):
        self.ball = Entities.Ball(400,200,25,25,-10)
        self.paddle1 = Entities.Paddle(0,0,25,150)
        self.paddle2 = Entities.Paddle(775,0,25,150)
        self.score1 = 0
        self.score2 = 0
