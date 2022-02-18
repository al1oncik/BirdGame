import pygame
import random
from bird  import Bird
from images import Img
from thorn import Thorn

class Game:
    
    pygame.init()
    
    def __init__(self):
        self.win_width  = 550
        self.win_height = 650
        self.win = pygame.display.set_mode((
                self.win_width,
                self.win_height
                ))
        
        self.start_the_game = False
        self.game_pause     = False

        self.clock = pygame.time.Clock()
        self.fps   = 30

        self.img   = Img()
        self.bird  = Bird()
        self.thorn = Thorn()
        
        # left thorns
        self.thorn1  = Thorn()
        self.thorn2  = Thorn()
        # right thorns
        self.thorn3  = Thorn()
        self.thorn4  = Thorn()
        
        # set bird image
        self.bird.image = self.img.bird_left

        #score
        self.score_count = 0 
        self.score_x     = 150
        self.score_font  = pygame.font.SysFont("algerian",600)
        
        pygame.display.set_caption("Bird Game")
        pygame.display.set_icon(self.img.icon)
    
    def draw(self):
        self.win.fill((0,0,0))# set black background
        if len(str(self.score_count)) == 1:
            self.win.blit(self.score,[self.score_x,120])
        else:
            self.win.blit(self.score,[self.score_x-80,120]) # move background score position if score bigger than 9
        self.win.blit(self.bird.image,[self.bird.x,self.bird.y])
        #draw down thorns
        for i in self.thorn.pos_down:
            self.win.blit(self.img.thorn,[i[0],i[1]])
        #draw upper thorns
        for i in self.thorn.pos_up:
            self.win.blit(self.img.thorn_down,[i[0],i[1]])

        # draw side thorns
        self.win.blit(
                self.img.thorn_left,
                [self.thorn1.left_x,self.thorn1.y])
        self.win.blit(
                self.img.thorn_left,
                [self.thorn2.left_x,self.thorn2.y])
        self.win.blit(
                self.img.thorn_right,
                [self.thorn3.right_x,self.thorn3.y])
        self.win.blit(
                self.img.thorn_right,
                [self.thorn4.right_x,self.thorn4.y])

        pygame.display.update()
        self.clock.tick(self.fps)
    

    def run(self):
        img  = self.img
        bird = self.bird
        while True:
            #updating score rendering
            self.score = self.score_font.render(str(self.score_count),True,(10,10,10))
            
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:  #if player press quit button
                    exit()
                # if player press on display or press key space
                if event.type == pygame.MOUSEBUTTONUP or pygame.key.get_pressed()[pygame.K_SPACE]:
                    self.start_the_game = True
                    bird.jump           = True

                if pygame.key.get_pressed()[pygame.K_r] and self.game_pause:
                    bird.x = 275
                    bird.y = 350
                    bird.moving = {
                        "left":True,
                        "right":False,
                        "down":True
                    }
                    self.score_count = 0
                    bird.image = img.bird_left
                    self.start_the_game = False
                    self.game_pause = False
                    # change thorns y positions
                    self.thorn1.rand_y()
                    self.thorn2.rand_y()
                    self.thorn3.rand_y()
                    self.thorn4.rand_y()

            if self.start_the_game and not self.game_pause:
                # bird moving left    
                if bird.moving['left']:
                    if bird.x > 0:
                        bird.x -= bird.speed
                    else:
                        self.score_count += 1
                        bird.moving['left']  = False
                        bird.moving['right'] = True
                        bird.image = img.bird_right
                        self.thorn3.rand_y()
                        self.thorn4.rand_y()

                # bird moving right
                if bird.moving['right'] :
                    if bird.x < self.win_width-bird.width:    
                        bird.x += bird.speed
                    else:
                        self.score_count += 1
                        bird.image = img.bird_left
                        bird.moving['left'] = True
                        bird.moving['right'] = False
                        self.thorn1.rand_y()
                        self.thorn2.rand_y()

                # bird jump
                if bird.jump:
                    bird.force_down = 3
                    bird.moving['down'] = False
                    if bird.force_up > 4:
                        bird.y -= self.bird.force_up
                        bird.force_up /= 1.3
                    else:
                        bird.force_up = 45
                        bird.jump = False
                        bird.moving['down'] = True

                # moving down
                if bird.moving['down']:
                    if bird.y < self.win_height-bird.height:
                        bird.y += bird.force_down
                        bird.force_down += 0.8
                    else:
                        bird.y = self.win_height - bird.height

            if self.game_pause:
                if bird.image == img.bird_left:
                    bird.image = img.dead_bird_left
                if bird.image == img.bird_right:
                    bird.image = img.dead_bird_right

            #check if bird not touch the thorn
            if bird.y < 40 or bird.y > 560:
                self.game_pause = True

            for i in [self.thorn1,self.thorn2]:
                if bird.x < 45 and bird.y > i.y and bird.y < i.y+35:
                    self.game_pause = True

            for i in [self.thorn3,self.thorn4]:
                if bird.x > 460 and bird.y > i.y and bird.y < i.y+35:
                    self.game_pause = True
            
            
            self.draw()


if __name__ == "__main__":
    game = Game()
    game.run()

        