import random
from manager import *

# Start pygame
pygame = Pygame(800, 600)
pygame.set_game_title("Apple Catcher Game")
pygame.set_background_image("background.jpg")

# Variable & Sprite

# Start Game
pygame.start_game()

done = False
while not done:
	# Check User input
	pygame.check_event()
	done = pygame.check_quit()

	# Program Logic

	# Update All Sprites
	pygame.update_game()

# Quit Game
pygame.quit_game()