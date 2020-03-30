import random
from manager import *

# Start pygame
my_pygame = Pygame(800, 600)
my_pygame.setGameTitle("Fish Catcher Game")
my_pygame.changeBackgroundImage("background1.jpg")

# Fish sprite
fish = my_pygame.addSprite('fish.png', 50)
fish.goTo(100, 0)
fishSpeed = 5
fishTimer = 0

# Shark sprite
shark = my_pygame.addSprite('shark.png', 75)
shark.goTo(-200,-200)
sharkSpeed = 10

done = False
while not done:
	# Check User input
	my_pygame.checkEvent();
	done = my_pygame.checkQuit();

	# Shark going left and right
	if my_pygame.keyHold(pygame.K_LEFT):
		shark.changeX(-1 * sharkSpeed)
	if my_pygame.keyHold(pygame.K_RIGHT):
		shark.changeX(sharkSpeed)
	if my_pygame.keyReleased(pygame.K_LEFT) or my_pygame.keyReleased(pygame.K_RIGHT):
		shark.changeX(0)

	# Shark going up and down
	if my_pygame.keyHold(pygame.K_UP):
		shark.changeY(sharkSpeed)
	if my_pygame.keyHold(pygame.K_DOWN):
		shark.changeY(-1 * sharkSpeed)
	if my_pygame.keyReleased(pygame.K_UP) or my_pygame.keyReleased(pygame.K_DOWN):
		shark.changeY(0)

	# Shark touching the fish
	if shark.touch(fish):
		shark.say("I got you")
		shark.switchCostume('shark2.png')
	else:
		shark.say("")
		shark.switchCostume('shark.png')


	# Stop on edge
	shark.stopOnEdge()
	fish.stopOnEdge()

	# Update All Sprites
	my_pygame.updateGame();

# Quit Game
my_pygame.quitGame()