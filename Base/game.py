'''
	YOUR GAME FILE
'''

import random
from manager import *

# Start pygame
# Set Screen Size 800 x 600
my_pygame = Pygame(800, 600)


# Add Sprite & Variable

# Start Game
my_pygame.startGame()

# Main Game Loop
done = False
while not done:
	# Check User input
	my_pygame.checkEvent()
	done = my_pygame.checkQuit()

	# Program Logic

	# Update All Sprites
	my_pygame.updateGame()

# Quit Game
my_pygame.quitGame()