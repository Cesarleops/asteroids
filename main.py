import pygame
from constants import *
from player import Player





def main():

    print("Starting Asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)
    # Initialize the pygame library, it automatically initializes all the modules
    # and returns a tuple with the number of modules initialized and the list of initialized modules 
    initGame = pygame.init()

    clock = pygame.time.Clock()

    dt = 0
    # Creates a display using, recieves a tuple as argument indicating the width and height of the window
    # The display is a surface that will be used to draw the game
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while True:
        screen.fill((0, 0, 0)) 
        player.draw(screen)
        player.update(dt)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
