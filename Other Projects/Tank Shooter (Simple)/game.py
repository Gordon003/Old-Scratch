import random
from manager import *

# Start pygame
pygame = Pygame(800, 600)
pygame.set_game_title("Tank Shooter Game")
pygame.set_background_image("background.jpg")


# Add Sprite & Variable
tank = pygame.add_sprite('tank.png', 20)
tank.go_to(0,-200)

bullet = pygame.add_sprite('bullet.png', 5)
bullet.hide()
bullet_shot = False
bullet_speed = 10

alien = pygame.add_sprite('alien.png', 15)
alien.set_y(250)
alien.set_x(random.randint(-300,300))
alien.show()
alien_speed = 3

# Start Game
pygame.start_game()

game_over = False
score = 0

# Main Game Loop
done = False
while not done:
	# Check User input
	pygame.check_event()
	done = pygame.check_quit()

	# Game Over
	if alien.touch(tank):
		game_over = True
	if game_over:
		pygame.write_text("Game Over!", 100, 0, 0)

	# Point Tank
	if game_over == False:
		tank.point_toward_mouse()

		# Shoot
		if pygame.check_mouse_clicked() and bullet_shot == False:
			bullet_shot = True
			bullet.go_to(tank.get_x(), tank.get_y())
			bullet.set_direction(tank.get_direction())
			bullet.show()

		# Move Bullet
		if bullet_shot == True:
			bullet.move(bullet_speed)

			# Bullet touch the edge
			if bullet.get_y() > 300 or abs(bullet.get_x()) > 400:
				bullet.hide()
				bullet_shot = False

			# Bullet touch the alien
			if bullet.touch(alien) and bullet_shot == True:
				score = score + 1
				alien.go_to(random.randint(-300,300), 250)
				bullet.hide()
				bullet_shot = False
				alien_speed = alien_speed + 0.5

		# Move Alien
		alien.point_toward_sprite(tank)
		alien.move(alien_speed)

	# Write Score
	pygame.write_text("Score: " + str(score), 20, 320, 250)

	# Update All Sprites
	pygame.update_game()

# Quit Game
pygame.quitGame()