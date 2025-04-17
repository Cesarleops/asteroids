import pygame
from constants import *

def main():

    print("Starting Asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)
    # Initialize the pygame library, it automatically initializes all the modules
    # and returns a tuple with the number of modules initialized and the list of initialized modules 
    initGame = pygame.init()

    # Creates a display using, recieves a tuple as argument indicating the width and height of the window
    # The display is a surface that will be used to draw the game
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        screen.fill((0, 0, 0)) 
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

if __name__ == "__main__":
    main()
