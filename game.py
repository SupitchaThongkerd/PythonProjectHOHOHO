import pygame

class Game():
    def __init__(self):
        pygame.init()
        self.running, self.playing = True, False
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        self.DISPLAY_W, self,DISPLAY_H = 480, 270
        self.display = pygame.Surface(self.DISPLAY_W, self.DISPLAY_H)
        self.window = pygame.display.set_mode(self.DISPLAY_W, self.DISPLAY_H)
        self.font_name = "wheaton capitals.otf"
        #self.font_name = pygame.font.get_default_font()
        self.WHITE, self.BLACK = (255, 255, 255), (0, 0, 0)