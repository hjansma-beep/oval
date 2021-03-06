"""
 Move a sprite in a circle.

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

"""

import pygame
import math
import random

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

size = [570, 563]
screen = pygame.display.set_mode(size)
background_image = pygame.image.load("oval.jpg").convert()

time_elapsed_since_last_action = 0
clock = pygame.time.Clock()
finish_list = []

class Block(pygame.sprite.Sprite):
    """ This class represents the ball that moves in a circle. """

    def __init__(self):
        """ Constructor that create's the ball's image. """
        super().__init__()
        self.image = pygame.image.load("bal.png").convert_alpha()
        self.rect = self.image.get_rect()

        # The "center" the sprite will orbit
        self.center_x = 0
        self.center_y = 0

        self.number = 0

        # Current angle in radians
        self.angle = 0

        # How far away from the center to orbit, in pixels
        self.radius = 0

        # How fast to orbit, in radians per frame
        self.speed = 0

        self.start = False

    def update(self):
        """ Update the ball's position. """
        # Calculate a new x, y
        self.rect.x = self.radius * math.sin(self.angle) + self.center_x
        self.rect.y = self.radius * math.cos(self.angle) + self.center_y

        # Increase the angle in prep for the next round.
        self.angle -= self.speed

    def check_start(self):
        if self.rect.colliderect(start_rect):
            self.start = True

    def check_finish(self):
        if self.rect.colliderect(finish_rect):
            finish_list.append(self.number)
            self.kill()


# Initialize Pygame
pygame.init()

# This is a list of 'sprites.' Each block in the program is
# added to this list. The list is managed by a class called 'Group.'
block_list = pygame.sprite.Group()

# This is a list of every sprite. All blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()

def place_block(gridpos, angle, number):
    # This represents a block
    block = Block()
    speed = random.randrange(1, 9)
    # Set a random center location for the block to orbit
    #naar rechts
    block.center_x = 270
    #omlaag
    block.center_y = 285
    # Random radius from 10 to 200
    block.radius = 195 + gridpos
    # Random start angle from 0 to 2pi
    block.angle = angle
    # radians per frame
    block.speed = speed / 1000

    block.number = number
    # block.speed = 0.01
    # Add the block to the list of objects
    block_list.add(block)
    all_sprites_list.add(block)

place_block(0, 3.2, 1)
place_block(45, 3.2, 2)
place_block(0, 3.35, 3)
place_block(45, 3.35, 4)
place_block(0, 3.5, 5)
place_block(45, 3.5, 6)

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
# clock = pygame.time.Clock()

score = 0

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # dt = clock.tick()
    # time_elapsed_since_last_action += dt
    # print(time_elapsed_since_last_action)

    all_sprites_list.update()
    # print(all_sprites_list)

    # Clear the screen
    screen.fill(WHITE)
    screen.blit(background_image, [0, 0])
    pygame.draw.line(screen, WHITE, (290, 24), (290, 118))
    start_rect = pygame.draw.rect(screen, BLUE, (331, 23, 1, 100))
    finish_rect = pygame.draw.rect(screen, BLUE, (310, 23, 1, 100))
    # screen.blit(background_image, [0, 0])


    for block in block_list:
        block.check_start()
        # print(block.start)

    for block in block_list:
        if block.start == True:
            block.check_finish()
            print(finish_list)

    # Draw all the spites
    all_sprites_list.draw(screen)
    # print(block)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # Limit to 60 frames per second
    clock.tick(60)

pygame.quit()