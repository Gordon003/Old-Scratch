import random
from manager import *

# Start pygame
# Set Screen Size 800 x 600
my_pygame = Pygame(800, 600)
my_pygame.setGameTitle("Tank Shooter Game")
my_pygame.changeBackgroundImage("background.jpg")


# Add Sprite & Variable
tank = my_pygame.addSprite('tank.png', 20)
tank.goTo(0,-200)

bullet = my_pygame.addSprite('bullet.png', 5)
bullet.hide()
bulletShot = False
bulletSpeed = 10

alien = my_pygame.addSprite('alien.png', 15)
alien.setY(250)
alien.setX(random.randint(-300,300))
alien.show()
alienSpeed = 3

# Start Game
my_pygame.startGame()

gameOver = False

score = 0

# Main Game Loop
done = False
while not done:
	# Check User input
	my_pygame.checkEvent()
	done = my_pygame.checkQuit()

	# Programming

	if alien.touch(tank):
		gameOver = True

	if gameOver == True:
		my_pygame.writeText("Game Over!", 100, 0, 0)

	# Point Tank
	if gameOver == False:
		tank.pointTowardMouse()

		# Shoot
		if my_pygame.checkMouseClicked() and bulletShot == False:
			bulletShot = True
			bullet.goTo(tank.getX(), tank.getY())
			bullet.setDirection(tank.getDirection())
			bullet.show()

		# Move Bullet
		if bulletShot == True:
			bullet.move(bulletSpeed)

			# Bullet touch the edge
			if bullet.getY() > 300 or abs(bullet.getX()) > 400:
				bullet.hide()
				bulletShot = False

			# Bullet touch the alien
			if bullet.touch(alien) and bulletShot == True:
				score = score + 1
				alien.goTo(random.randint(-300,300), 250)
				bullet.hide()
				bulletShot = False
				alienSpeed = alienSpeed + 0.5

		# Move Alien
		alien.pointTowardSprite(tank)
		alien.move(alienSpeed)

	# Write Score
	my_pygame.writeText("Score: " + str(score), 20, 320, 250)

	# Update All Sprites
	my_pygame.updateGame()

# Quit Game
my_pygame.quitGame()