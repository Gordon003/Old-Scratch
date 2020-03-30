import random
from manager import *

# Start pygame
my_pygame = Pygame(800, 600)
my_pygame.setGameTitle("Apple Catcher Game")
my_pygame.changeBackgroundImage("background.jpg")

# Variable
score = 0

# Basket
basket = my_pygame.addSprite('basket.png', 15)
basket.goTo(0,-150)

# Apple
apple = my_pygame.addSprite('apple.png', 5)
apple.goTo(random.randint(-300,300),300)

# Start Game
my_pygame.startGame()

done = False
while not done:
	# Check User input
	my_pygame.checkEvent()
	done = my_pygame.checkQuit()

	# Move Basket
	# Shark going left and right
	if my_pygame.keyHold(pygame.K_LEFT):
		basket.changeX(-5)
	if my_pygame.keyHold(pygame.K_RIGHT):
		basket.changeX(5)
	if my_pygame.keyReleased(pygame.K_LEFT) or my_pygame.keyReleased(pygame.K_RIGHT):
		basket.changeX(0)

	# Apple Drop
	apple.changeY(-5)

	if basket.touch(apple):
		score += 1
		apple.goTo(random.randint(-300,300),300)

	# Reset apple if drop
	if apple.getY() < -200:
		apple.goTo(random.randint(-300,300),300)

	# Write Score
	my_pygame.writeText("Score: " + str(score), 20, 320, 250)

	# Update All Sprites
	my_pygame.updateGame()

# Quit Game
my_pygame.quitGame()