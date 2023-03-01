import pygame

BALLSPEED = 3
class Ball():
    def __init__(self, x, y, width, height, direction):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.XPos = direction = BALLSPEED
        self.YPos = 0

class Paddle():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height