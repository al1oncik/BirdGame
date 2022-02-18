import pygame
pygame.init()

class Img:
    def __init__(self):
        self.icon            = pygame.image.load("game_icon.png")
        self.bird_right      = pygame.image.load("bird_right.png")
        self.bird_left       = pygame.image.load("bird_left.png")
        self.dead_bird_right = pygame.image.load("dead_bird_right.png")
        self.dead_bird_left  = pygame.image.load("dead_bird_left.png")
        self.thorn           = pygame.image.load("thorn.png")
        self.thorn_down      = pygame.transform.rotate(self.thorn,180)
        self.thorn_right     = pygame.transform.rotate(self.thorn,90)
        self.thorn_left      = pygame.transform.rotate(self.thorn,270)
