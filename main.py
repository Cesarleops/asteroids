import pygame
from constants import *
from player import Player





def main():

    print("Starting Asteroids!")

    # Initialize the pygame library, it automatically initializes all the modules
    # and returns a tuple with the number of modules initialized and the list of initialized modules 
    initGame = pygame.init()

    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()

    drawable = pygame.sprite.Group()


    Player.containers = (updatable, drawable)

    dt = 0
    # Creates a display using, recieves a tuple as argument indicating the width and height of the window
    # The display is a surface that will be used to draw the game
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #Create an instance of the player 
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    #Start game loop, it must check player input, update the world(process physics and animations)
    #draw the updated world to the screen
    while True:


        # Fill the screen with a color, black in this case
        screen.fill((0, 0, 0)) 

        #We can manually call each method of an object, but that can make the code very cluttered
        #For example, we could have many players and have 10 lines calling the update, pygame
        # offers the group class that can manage multiple groups, think of a group as a venn diagram
        # if an object belongs to a group it means it has a specific method that can be called
        # e.g If player belongs to the drawable group, it can call the draw() method.

        # player.draw(screen)
        # player.update(dt)

        # It's possible to call a method of an object in a group by iterating each item of the group
        # or calling the method directly on the group which calls it on every item at the same time.

        #Draw the player in the screen
        updatable.update(dt)

        for member in drawable:
            member.draw(screen)

     

        #Update the screen
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
