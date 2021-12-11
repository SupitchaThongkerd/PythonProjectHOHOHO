import pygame

class Menu():
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        self.run_display = True
        self.cursor_rect = pygame.rect(0, 0, 20, 20)
        self.offset = -100

    def draw_cursor(self):
        self.game.draw_text("*", 15, self.cursor_rect.x, self.cursor_rect.y)
    
    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.uppdate()
        self.game.reset_keys()


class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Start"
        self.startx, self.starty = self.mid_w, self.mid_h + 30
        self.controlsx, self.controlsy = self.mid_w, self.mid_h + 50
        self.creditsx, self.creditsy = self.mid_w, self.mid_h + 70
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text("HOHOHO GIVE MY SLEIGH BACK!", 20, self.game.DISPLAY_W/2, self.game.DISPLAY_H/2-20)
            self.game.draw_text("Start Game", 20, self.startx, self.starty)
            self.game.draw_text("Controls", 20, self.controlsx, self.controlsy)
            self.game.draw_text("Credits", 20, self.creditsx, self.creditsy)
            self.draw_cursor()
            self.blit_screen()
    
    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == "Start":
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.state = "Controls"
            elif self.state == "Controls":
                self.cursor_rect.midtop = (self.controlsx + self.offset, self.controlsy)
                self.state = "Credits"
            elif self.state == "Credits":
                self.cursor_rect.midtop = (self.controlsx + self.offset, self.controlsy)
                self.state = "Start"

#when return from the last one to the top
        elif self.game.UP_KEY:
            if self.state == "Start":
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = "Credits"
            elif self.state == "Controls":
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = "Start"
            elif self.state == "Credits":
                self.cursor_rect.midtop = (self.controlsx + self.offset, self.controlsy)
                self.state = "Controls"

    def check_input(self):
        #check if he player move any cursor
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == "Start":
                self.game.playing = True
            elif self.state == "Controls":
                pass
            elif self.state == "Credits":
                pass
            #main menu stop diaplaying / it will tell the display menu function to stop
            self.run_display = False
