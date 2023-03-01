import pygame
import random
BALLSPEED = 3
class Controller():
    def __init__(self, model):
        self.model = model
        self.tick = 0

    def moveBall(self):
        self.model.ball.x += self.model.ball.XPos
        self.model.ball.y += self.model.ball.YPos

        if self.model.ball.y + self.model.ball.height>= 400:
            self.model.ball.YPos = -BALLSPEED
        elif self.model.ball.y <= 0:
            self.model.ball.YPos = BALLSPEED

    ##function to check movement
    def movePaddle(self, data):
        if data[pygame.K_UP]:
            self.model.paddle2.y -= 1
            if self.model.paddle2.y <= 0:
                self.model.paddle2.y += 1
        if data[pygame.K_DOWN]:
            self.model.paddle2.y += 1
            if self.model.paddle2.y  + self.model.paddle2.height>= 400:
                self.model.paddle2.y -= 1
        if data[pygame.K_w]:
            self.model.paddle1.y -= 1
            if self.model.paddle1.y <= 0:
                self.model.paddle1.y += 1
        if data[pygame.K_s]:
            self.model.paddle1.y += 1
            if self.model.paddle1.y  + self.model.paddle1.height>= 400:
                self.model.paddle1.y -= 1
    
    def Bounce(self):
        bottomRight = (self.model.ball.x + self.model.ball.width, self.model.ball.y + self.model.ball.height)

        if self.model.ball.x <= self.model.paddle1.x + self.model.paddle1.width and self.model.ball.x >= self.model.paddle1.x:
            if self.model.ball.y <= self.model.paddle1.y + self.model.paddle1.height and self.model.ball.y >= self.model.paddle1.y:
                self.model.ball.XPos = BALLSPEED
                self.model.ball.YPos = random.randint(1, 10)/10

        if self.model.ball.x + self.model.ball.width <= self.model.paddle2.x + self.model.paddle2.width and self.model.ball.x + self.model.ball.width >= self.model.paddle2.x:
            if self.model.ball.y <= self.model.paddle2.y + self.model.paddle2.height and self.model.ball.y >= self.model.paddle2.y:
                self.model.ball.XPos = -BALLSPEED
                self.model.ball.YPos = -random.randint(1, 10)/10

        if self.model.ball.x <= self.model.paddle1.x + self.model.paddle1.width and self.model.ball.x >= self.model.paddle1.x:
            if bottomRight[1] <= self.model.paddle1.y + self.model.paddle1.height and bottomRight[1] >= self.model.paddle1.y:
                self.model.ball.XPos = BALLSPEED
                self.model.ball.YPos = random.randint(1, 10) / 10

        if self.model.ball.x + self.model.ball.width <= self.model.paddle2.x + self.model.paddle2.width and self.model.ball.x + self.model.ball.width >= self.model.paddle2.x:
            if bottomRight[1] <= self.model.paddle2.y + self.model.paddle2.height and bottomRight[1] >= self.model.paddle2.y:
                self.model.ball.XPos = -BALLSPEED
                self.model.ball.YPos = -random.randint(1, 10)/10



    def scoreUpdate(self):
        if self.model.ball.x <= 0:
            self.model.ball.x = 400
            self.model.ball.y = 200
            self.model.score2 += 1
        elif self.model.ball.x >= 800:
            self.model.ball.x = 400
            self.model.ball.y = 200
            self.model.score1 += 1
    
    def GameOver(self):
        if self.model.score1 == 5:
            self.model.ball.XPos = 0
            self.model.ball.YPos = 0
        elif self.model.score2 == 5:
            self.model.ball.XPos = 0
            self.model.ball.YPos = 0
    
    ##update the game loop
    def update(self):
        self.tick += 1

        if self.tick == 3:
            self.GameOver()
            self.Bounce()
            self.scoreUpdate()
            self.moveBall()
            self.tick = 0

        
