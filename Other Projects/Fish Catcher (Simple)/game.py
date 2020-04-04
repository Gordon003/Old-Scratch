import random
from manager import *

# Start pygame
pygame = Pygame(800, 600)
pygame.set_game_title("Fish Catcher Game")
pygame.set_background_image("background1.jpg")

# Fish sprite
fish = pygame.add_sprite('fish.png', 50)
fish.go_to(100, 0)
fish_speed = 5
fishTimer = 0

# Shark sprite
shark = pygame.add_sprite('shark.png', 75)
shark.go_to(-200,-200)
shark_speed = 10

# Game Loop
done = False
while not done:
	
	# Check User input
	pygame.check_event();
	done = pygame.check_quit();

	# Shark going left and right
	if pygame.key_hold("left"):
		shark.change_x(-1 * shark_speed)
	if pygame.key_hold("right"):
		shark.change_x(shark_speed)
	if pygame.key_released("left") or pygame.key_released("right"):
		shark.change_x(0)

	# Shark going up and down
	if pygame.key_hold("up"):
		shark.change_y(shark_speed)
	if pygame.key_hold("down"):
		shark.change_y(-1 * shark_speed)
	if pygame.key_released("up") or pygame.key_released("down"):
		shark.change_y(0)

	# Fish going left and right
	if pygame.key_hold("a"):
		fish.change_x(-1 * fish_speed)
	if pygame.key_hold("d"):
		fish.change_x(fish_speed)
	if pygame.key_released("a") or pygame.key_released("d"):
		fish.change_x(0)

	# Fish going up and down
	if pygame.key_hold("w"):
		fish.change_y(fish_speed)
	if pygame.key_hold("s"):
		fish.change_y(-1 * fish_speed)
	if pygame.key_released("w") or pygame.key_released("s"):
		fish.change_y(0)

	# Shark touching the fish
	if shark.touch(fish):
		shark.say("I got you")
		shark.switch_costume("shark2.png")
	else:
		shark.say("")
		shark.switch_costume("shark.png")


	# Stop on edge
	shark.bounce_on_edge()
	fish.bounce_on_edge()

	# Update All Sprites
	pygame.update_game();

# Quit Game
pygame.quit_game()