import pygame, sys
import os
import time
import random

from pygame import draw
from pygame.constants import WINDOWHITTEST
from pygame.sprite import collide_circle
from pygame import mixer
pygame.font.init()
os.chdir("/Users/pearsupitcha/Documents/python project/PythonProjectHOHOHO")

WIDTH, HEIGHT = 1000, 650
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("HOHOHO GIVE MY SLEIGH BACK!")

#bgmusic
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("/Users/pearsupitcha/Documents/python project/PythonProjectHOHOHO/pureimagination.wav")
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(1)
pygame.event.wait()


#current_disc = os.getcwd()
#game_folder = os.path.dirname(current_disc)
#img_folder = os.path.join(game_folder,"santa")

#santa = pygame.transform.scale(pygame.image.load(path.join(img_folder, "santa.png")).convert_alpha(), (50, 50))

#player image
santa = pygame.image.load(os.path.join("/Users/pearsupitcha/Documents/python project/PythonProjectHOHOHO", "santa_pixel.png"))
santa2 = pygame.transform.scale(santa, (60, 60))
#characters
grinch = pygame.image.load(os.path.join("/Users/pearsupitcha/Documents/python project/PythonProjectHOHOHO", "grincheiei.png"))
grinch2 = pygame.transform.scale(grinch, (70, 70))
pumpkin = pygame.image.load(os.path.join("/Users/pearsupitcha/Documents/python project/PythonProjectHOHOHO", "pumpkin.png"))
pumpkin2 = pygame.transform.scale(pumpkin, (60, 60))
bhudda = pygame.image.load(os.path.join("/Users/pearsupitcha/Documents/python project/PythonProjectHOHOHO", "bhudda.png"))
bhudda2 = pygame.transform.scale(bhudda, (45, 60))
#magic(weapon)

#santa's candycane
candycane = pygame.image.load(os.path.join("/Users/pearsupitcha/Documents/python project/PythonProjectHOHOHO", "candycane.png"))
candycane2 = pygame.transform.scale(candycane, (30, 30))
#grinch's tomato
tomato = pygame.image.load(os.path.join("/Users/pearsupitcha/Documents/python project/PythonProjectHOHOHO", "tomato.png"))
tomato2 = pygame.transform.scale(tomato, (30, 30))
#pumpkin's fire
fire = pygame.image.load(os.path.join("/Users/pearsupitcha/Documents/python project/PythonProjectHOHOHO", "fire.png"))
fire2 = pygame.transform.scale(fire, (30, 30))
#bhudda's lotus
lotus = pygame.image.load(os.path.join("/Users/pearsupitcha/Documents/python project/PythonProjectHOHOHO", "lotus.png"))
lotus2 = pygame.transform.scale(lotus, (30, 30))

#background
BG = pygame.transform.scale(pygame.image.load(os.path.join("/Users/pearsupitcha/Documents/python project/PythonProjectHOHOHO", "pjbg.png")), (WIDTH, HEIGHT))
BG2 = pygame.transform.scale(pygame.image.load(os.path.join("/Users/pearsupitcha/Documents/python project/PythonProjectHOHOHO", "cmbg.jpg")), (WIDTH, HEIGHT))

class Magic:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)
    
    def draw(self, window):
        window.blit(self.img, (self.x, self.y))
    
    def move(self, velocity):
        self.x += velocity

    def off_screen(self, WIDTH):
        return not(self.x <= WIDTH and self.x >= 0)
    
    def collision(self, object):
        return collide(self, object)

class Characters:
    #FPS is 60
    COOLDOWN = 20

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
        for magic in self.magics:
            magic.draw(window)
    
    #move laser and check collision
    def move_magics(self, velocity, object):
        self.cooldown()
        for magic in self.magics:
            magic.move(velocity)
            if magic.off_screen(WIDTH):
                self.magics.remove(magic)
            elif magic.collision(object):
                object.health -= 10
                self.magics.remove(magic)

    def cooldown(self):
        if self.cool_down_counter >= self.COOLDOWN:
            self.cool_down_counter = 0
        elif self.cool_down_counter > 0:
            self.cool_down_counter += 1

    def shoot(self):
        if self.cool_down_counter == 0:
            magic = Magic(self.x, self.y, self.magic_img)
            self.magics.append(magic)
            #set cool down counter to count up
            self.cool_down_counter = 1

    #make the picture of the player not go off the screen
    def get_width(self):
        return self.characters_img.get_width()
    
    def get_height(self):
        return self.characters_img.get_height()

class Player(Characters):
    def __init__(self, x, y, health = 100):
        super().__init__(x, y, health)
        self.characters_img = santa2
        self.magic_img = candycane2
        #make the mask of the player to tell wheres the pixels are
        #so when theres a collition we will know whether it hits the pixels or not
        self.mask = pygame.mask.from_surface(self.characters_img)
        self.max_health = health

    def move_magics(self, velocity, objects):
        self.cooldown()
        for magic in self.magics:
            magic.move(velocity)
            if magic.off_screen(WIDTH):
                self.magics.remove(magic)
            else: 
                for object in objects:
                    if magic.collision(object):
                        objects.remove(object)
                        if magic in self.magics:
                            self.magics.remove(magic)
    
    def refresh_health(self):
        self.health = self.max_health


    def draw(self, window):
        super().draw(window)
        self.healthbar(window)

    def healthbar(self, window):
        
        pygame.draw.rect(window, (166, 8, 95), (self.x, self.y + self.characters_img.get_height() + 10, self.characters_img.get_width(), 10))
        #self.max_health(health rn)- self.health(full health))/self.max_health got the percent health loss
        pygame.draw.rect(window, (35, 96, 95), (self.x, self.y + self.characters_img.get_height() + 10, self.characters_img.get_width() * (self.health /self.max_health), 10))
        
        
    
class Enemy(Characters):
    COLOR_MAP = {
                "red": (grinch2, tomato2),
                "green": (pumpkin2, fire2),
                "blue": (bhudda2, lotus2)}

    def __init__(self, x, y, color, health = 100):
        super().__init__(x, y, health)
        self.characters_img, self.magic_img = self.COLOR_MAP[color]
        self.mask = pygame.mask.from_surface(self.characters_img)

    def move(self, velocity):
        self.x -= velocity

        def shoot(self):
            if self.cool_down_counter == 0:
                magic = Magic(self.x, self.y - 10, self.magic_img)
                self.magics.append(magic)
                #set cool down counter to count up
                self.cool_down_counter = 1

def collide(object1, object2):
    offset_x = object2.x - object1.x
    offset_y = object2.y - object1.y
    return object1.mask.overlap(object2.mask, (offset_x, offset_y)) != None


def main():
    rounds = 3
    run = True
    FPS = 60
    level1 = 0
    lives = 5

    main_font = pygame.font.Font("/Users/pearsupitcha/Documents/python project/PythonProjectHOHOHO/FFF_Tusj.ttf", 40)
    lost_font = pygame.font.Font("/Users/pearsupitcha/Documents/python project/PythonProjectHOHOHO/Quinquefive.ttf", 21)
    end_font = pygame.font.Font("/Users/pearsupitcha/Documents/python project/PythonProjectHOHOHO/Quinquefive.ttf", 21)

    pewpew = pygame.mixer.Sound("/Users/pearsupitcha/Documents/python project/PythonProjectHOHOHO/Fairy dust, magic sound effect.wav")

    enemies = []
    #wavelemgth =5  = 10 enemies if 6 then +1
    wave_length = 5
    enemies_velocity = 2

    player_velocity = 6 #lower clock speed = need higher velocity
    magic_velocity = 4

    player = Player(10, 300)

    clock = pygame.time.Clock()

    lost = False
    end = False
    lost_count = 0
    end_count = 0


    def redraw_window():
        win.blit(BG, (0, 0))
        #draw text
        lives_label = main_font.render(f"Lives: {lives}", 1, (13, 36, 0))
        level1_label = main_font.render(f"Level: {level1}", 1, (13, 36, 0))
        
        win.blit(lives_label, (10, 10))
        win.blit(level1_label,(WIDTH - level1_label.get_width() - 10, 10))
        
        for enemy in enemies:
            enemy.draw(win)

        player.draw(win)


        if end:
            end_label = end_font.render("YOU SAVE SANTA'S SLEIGH!!", 1, (79, 118, 12))
            win.blit(end_label, (WIDTH/2 - end_label.get_width()/2, 325))
        
        if lost:
            lost_label = lost_font.render("YOU FAILED TO SAVE SANTA'S SLEIGH:(", 1, (255, 0, 0))
            win.blit(lost_label, (WIDTH/2 - lost_label.get_width()/2, 325))

        pygame.display.update()

    #run/check 60 times every second
    while run:
        clock.tick(FPS)

        redraw_window()

        if lives <= 0 or player.health <= 0:
            lost = True
            lost_count += 1

        if rounds == 0:
            end = True
            end_count += 1

        #for healthbar in Player < health:
        # level1 = +1
            #health = 100
        
        if lost:
            if lost_count > FPS * 5:
                run = False
            else:
                continue
        
        if end:
            if end_count > FPS * 5:
                run = False
            else:
                continue

        if len(enemies) == 0:
            level1 += 1
            rounds -= 1
            wave_length += 5
            player.refresh_health()
            #self.health = self.max_health
            # create many enemies
            for i in range(wave_length):
                #random position
                enemy = Enemy(random.randrange(1050, 2500), random.randrange(50, WIDTH - 450), random.choice(["red", "green", "blue"]))
                enemies.append(enemy)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
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
        #enter space to shoot
        if keys[pygame.K_SPACE]:
            player.shoot()
            pewpew.play()
            pewpew.set_volume(0.2)

        for enemy in enemies[:]:
            #make the enemies move
            enemy.move(enemies_velocity)
            enemy.move_magics(-magic_velocity, player)

            #every 2sec enemy will shoot
            if random.randrange(0, 3*60) == 1:
                enemy.shoot()

            #player health decrease after the collision
            if collide(enemy, player):
                player.health -= 10
                enemies.remove(enemy)
            #deducting lives if the enemy off the screen
            elif enemy.x + enemy.get_width() < WIDTH-951:
                lives -= 1
                enemies.remove(enemy)

        
        #check if the magic collide with any of the enemies
        player.move_magics(magic_velocity, enemies)

def main_menu():
    title_font = pygame.font.Font("/Users/pearsupitcha/Documents/python project/PythonProjectHOHOHO/Quinquefive.ttf", 20)
    run = True
    while run:
        win.blit(BG2, (0,0))
        title_label = title_font.render("Click to help Santa get his sleigh back!", 1, (0, 0, 0))
        win.blit(title_label,(WIDTH/2 - title_label.get_width()/2, 350))

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                main()
    pygame.quit()

main_menu()