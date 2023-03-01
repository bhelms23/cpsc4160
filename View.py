import pygame,sys

class View():
    def __init__(self, model, controller):
        self.model = model
        self.controller = controller
        pygame.init()
        self.screen = pygame.display.set_mode((800, 400))
        
    
    ##use the move paddle in the view
    def getControl(self, data):
        self.controller.movePaddle(data) 
    
    ##displaying entities
    def displayBall(self):
        pygame.draw.rect(self.screen, (255, 255, 255), (self.model.ball.x, self.model.ball.y, self.model.ball.width, self.model.ball.height))

    def displayPaddles(self):
        pygame.draw.rect(self.screen, (255, 255, 255), (self.model.paddle1.x, self.model.paddle1.y, self.model.paddle1.width, self.model.paddle1.height))
        pygame.draw.rect(self.screen, (255, 255, 255), (self.model.paddle2.x, self.model.paddle2.y, self.model.paddle2.width, self.model.paddle2.height))
   
    ##creating scoreboard
    def displayScore(self):
        font = pygame.font.SysFont(None, 50)
        text = font.render(str(self.model.score1), False, (255,255,255))
        self.screen.blit(text, (280, 10))

        text = font.render(str(self.model.score2), False, (255, 255, 255))
        self.screen.blit(text, (500, 10))
    
    def DisplayWinner(self):
        if self.model.score1 == 5:
            font = pygame.font.SysFont(None, 50)
            text = font.render(str("Game Over: Player 1 Wins"), False, (255,255,255))
            self.screen.blit(text,(200,100))
        elif self.model.score2 == 5:
            font = pygame.font.SysFont(None, 50)
            text = font.render(str("Game Over: Player 2 Wins"), False, (255,255,255))
            self.screen.blit(text,(200,100))

        
    def display(self):
        exit = 0

        while not exit:
            # Background color
            self.screen.fill((0,0,0))
           
            self.DisplayWinner()
            self.displayPaddles()
            self.displayBall()
            self.displayScore()

            pygame.display.update()

            self.getControl(pygame.key.get_pressed())
            self.controller.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit = 1
                    pygame.quit()
