import random
from manager import *

# Start pygame
pygame = Pygame(800, 600)
pygame.set_game_title("Apple Catcher Game")
pygame.set_background_image("background.jpg")

# Variable
score = 0

# Basket
basket = pygame.add_sprite('basket.png', 15)
basket.go_to(0,-150)

# Apple
apple = pygame.add_sprite('apple.png', 5)
apple.go_to(random.randint(-300,300),300)

# Start Game
pygame.start_game()

done = False
while not done:
	# Check User input
	pygame.check_event()
	done = pygame.check_quit()

	# Move Basket
	# Shark going left and right
	if pygame.key_hold("left"):
		basket.change_x(-5)
	if pygame.key_hold("right"):
		basket.change_x(5)
	if pygame.key_released("left") or pygame.key_released("right"):
		basket.change_x(0)

	# Apple Drop
	apple.change_y(-5)

	if basket.touch(apple):
		score += 1
		apple.go_to(random.randint(-300,300),300)

	# Reset apple if drop
	if apple.get_y() < -200:
		apple.go_to(random.randint(-300,300),300)

	# Write Score
	pygame.write_text("Score: " + str(score), 20, 320, 250)

	# Update All Sprites
	pygame.update_game()

# Quit Game
pygame.quit_game()