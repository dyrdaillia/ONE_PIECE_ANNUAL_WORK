import pygame, sys
from settings import *
from level import Level
from button import Button
from pyvidplayer import Video

pygame.init()
SCREEN = pygame.display.set_mode((WIDTH, HEIGTH))
BG = pygame.image.load("image1.png")
BG2 = pygame.image.load("image3.jpg")

class Game:
    def __init__(self):

            pygame.init()
            self.screen = pygame.display.set_mode((WIDTH,HEIGTH))
            pygame.display.set_caption('One Piece')
            programIcon = pygame.image.load('onepiece.png')
            pygame.display.set_icon(programIcon)
            self.clock = pygame.time.Clock()


    def intro(self):
        vid = Video("video3.mp4")
        vid.set_size((1280, 720))
        while True:
            vid.draw(SCREEN,(0,0))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    vid.close()
                    self.run()

    def get_font(self,size):
        return pygame.font.Font("one piece font.ttf", size)

    def credits(self):
        while True:
            CREDITS_MOUSE_POS = pygame.mouse.get_pos()

            SCREEN.blit(BG2, (0, 0))

            CREDITS_TEXT = self.get_font(45).render("Thanks for playing", True, "Black")
            CREDITS_RECT = CREDITS_TEXT.get_rect(center=(640, 260))
            SCREEN.blit(CREDITS_TEXT, CREDITS_RECT)

            CREDITS_BACK = Button(image=None, pos=(640, 460),
                                  text_input="BACK", font=self.get_font(75), base_color="Black", hovering_color="Green")

            CREDITS_BACK.changeColor(CREDITS_MOUSE_POS)
            CREDITS_BACK.update(SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if CREDITS_BACK.checkForInput(CREDITS_MOUSE_POS):
                        self.main_menu()

            pygame.display.update()

    def main_menu(self):
        while True:
            SCREEN.blit(BG, (0, 0))

            MENU_MOUSE_POS = pygame.mouse.get_pos()

            MENU_TEXT = self.get_font(100).render("ONE PIECE", True, "White")
            MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

            PLAY_BUTTON = Button(image=pygame.image.load("Rect2.png"), pos=(640, 250),
                                 text_input="PLAY", font=self.get_font(50), base_color="#d7fcd4", hovering_color="White")
            OPTIONS_BUTTON = Button(image=pygame.image.load("Rect2.png"), pos=(640, 400),
                                    text_input="CREDITS", font=self.get_font(50), base_color="#d7fcd4",
                                    hovering_color="White")
            QUIT_BUTTON = Button(image=pygame.image.load("Rect2.png"), pos=(640, 550),
                                 text_input="QUIT", font=self.get_font(50), base_color="#d7fcd4", hovering_color="White")

            SCREEN.blit(MENU_TEXT, MENU_RECT)

            for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.intro()
                    if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.options()
                    if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                        pygame.quit()
                        sys.exit()

            pygame.display.update()

    def run(self):
        self.level = Level()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_m:
                        self.level.toggle_menu()


            self.screen.fill('#01d6fc')
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == '__main__':
    game = Game()
    game.main_menu()