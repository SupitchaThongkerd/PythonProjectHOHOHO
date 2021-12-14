import pygame, sys
import os
import time
import random

from pygame import draw
pygame.font.init()
os.chdir("/Users/pearsupitcha/Documents/python project/PythonProjectHOHOHO")

WIDTH, HEIGHT = 1000, 650
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("HOHOHO GIVE MY SLEIGH BACK!")

#current_disc = os.getcwd()
#game_folder = os.path.dirname(current_disc)
#img_folder = os.path.join(game_folder,"santa")

#santa = pygame.transform.scale(pygame.image.load(path.join(img_folder, "santa.png")).convert_alpha(), (50, 50))

#player image
santa = pygame.image.load(os.path.join("/Users/pearsupitcha/Documents/python project/PythonProjectHOHOHO", "santa_pixel.png"))
santa2 = pygame.transform.scale(santa, (60, 60))
#characters
grinch = pygame.image.load(os.path.join("/Users/pearsupitcha/Documents/python project/PythonProjectHOHOHO", "grinch.png"))
grinch2 = pygame.transform.scale(grinch, (60, 60))
pumpkin = pygame.image.load(os.path.join("/Users/pearsupitcha/Documents/python project/PythonProjectHOHOHO", "pumpkin.png"))

#magic(weapon)

#santa's candycane
candycane = pygame.image.load(os.path.join("/Users/pearsupitcha/Documents/python project/PythonProjectHOHOHO", "candycane.png"))
candycane2 = pygame.transform.scale(candycane, (20, 20))
#grinch's tomato
tomato = pygame.image.load(os.path.join("/Users/pearsupitcha/Documents/python project/PythonProjectHOHOHO", "tomato.png"))
tomato2 = pygame.transform.scale(tomato, (20, 20))
#pumpkin's fire
fire = pygame.image.load(os.path.join("/Users/pearsupitcha/Documents/python project/PythonProjectHOHOHO", "fire.png"))
fire2 = pygame.transform.scale(fire, (20, 20))
#background
BG = pygame.transform.scale(pygame.image.load(os.path.join("/Users/pearsupitcha/Documents/python project/PythonProjectHOHOHO", "cmbg.jpg")), (WIDTH, HEIGHT))

class Characters:
    def __init__(self, x, y, health = 100):
        self.x = x
        self.y = y
        self.health = health
        self.characters_img = None
        self.magic_img = None
        self.magics = []
        self.cool_down_counter = 0

    def draw(self, window):
        window.blit(self.characters_img, (self.x, self.y))
    
    #make the picture of the player not go off the screen
    def get_width(self):
        return self.characters_img.get_width()
    
    def get_height(self):
        return self.characters_img.get_height()

class Player(Characters):
    def __init__(self, x, y, health = 100):
        super().__init__( x, y, health)
        self.characters_img = santa2
        self.magic_img = candycane
        #make the mask of the player to tell wheres the pixels are
        #so when theres a collition we will know whether it hits the pixels or not
        self.mask = pygame.mask.from_surface(self.characters_img)
        self.max_health = health

def main():
    run = True
    FPS = 60
    level1 = 1
    lives = 5
    main_font = pygame.font.SysFont("8-BIT WONDER.TTF", 40)
    player_velocity = 7 #lower clock speed = nedd higher velocity

    player = Player(10, 300)

    clock = pygame.time.Clock()

    def redraw_window():
        win.blit(BG, (0, 0))
        #draw text
        lives_label = main_font.render(f"Lives: {lives}", 1, (0, 0, 0))
        level1_label = main_font.render(f"Level: {level1}", 1, (0, 0, 0))

        win.blit(lives_label, (10, 10))
        win.blit(level1_label,(WIDTH - level1_label.get_width() - 10, 10))

        
        player.draw(win)

        pygame.display.update()
    #run/check 60 times every second
    while run:
        clock.tick(FPS)
        redraw_window()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        #making keys to move object (WASD)
        keys = pygame.key.get_pressed()
        #moving left and not off the screen which is more than zero
        if keys[pygame.K_a] and player.x - player_velocity > 0:
            player.x -= player_velocity
        #moving right and not off the screen width
        if keys[pygame.K_d] and player.x + player_velocity + (player.get_width()+650) < WIDTH:
            player.x += player_velocity
        #moving up and not off the screen which is more than zero
        if keys[pygame.K_w] and player.y - player_velocity > 0:
            player.y -= player_velocity
        #moving down and not off the screen height
        if keys[pygame.K_s] and player.y + player_velocity + player.get_height() < HEIGHT:
            player.y += player_velocity
        

main()