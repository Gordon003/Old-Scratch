import random
import time
from colour import *
from manager import *

# Start pygame
pygame = Pygame(800, 600)
pygame.set_game_title("Ping Pong Game")
pygame.set_background_image("background.jpg")

player_speed = 10

red = pygame.add_sprite("red.png", 70)
red.go_to(-300,0)
red_score = 0

blue = pygame.add_sprite("blue.png", 70)
blue.go_to(300,0)
blue_score = 0

ball = pygame.add_sprite("ball.png", 40)
ball.set_direction(-60)
ball.set_direction(random.randint(-180,180))
default_speed = 4
ball_speed = default_speed

# Start Game
pygame.start_game()

done = False
while not done:
	# Check User input
	pygame.check_event()
	done = pygame.check_quit()

	# Red Movement
	if pygame.key_hold("w") and red.get_y() < 300:
		red.change_y(player_speed)
	elif pygame.key_hold("s") and red.get_y() > -300:
		red.change_y(-1 * player_speed)
	elif pygame.key_released("w") or pygame.key_released("s") or (abs(red.get_y()) > 300):
		red.change_y(0)

	# Blue Movement
	if pygame.key_hold("up") and blue.get_y() < 300:
		blue.change_y(player_speed)
	elif pygame.key_hold("down") and blue.get_y() > -300:
		blue.change_y(-1 * player_speed)
	elif pygame.key_released("up") or pygame.key_released("down") or (abs(blue.get_y()) > 300):
		blue.change_y(0)

	# Ball hit side
	if abs(ball.get_x()) >= 380:
		if ball.get_x() >= 0: blue_score += 1
		else: red_score += 1
		time.sleep(1)
		ball.go_to(0,0)
		ball.set_direction(random.randint(-180,180))
		blue.set_y(0)
		red.set_y(0)
		ball_speed = default_speed

	# Ball touch blue or red pad
	if ball.touch(blue) or ball.touch(red):
		ball.move(-2 * ball_speed)
		ball_speed += 1
		ball.set_direction(-1 * ball.get_direction())
	# Ball hit edge
	else:
		ball.move(ball_speed)
		ball.bounce_on_edge()

	# Write score
	pygame.write_text("Red: " + str(red_score), 30, WHITE, -300, 250)
	pygame.write_text("Blue: " + str(blue_score), 30, WHITE, 300, 250)

	# Update All Sprites
	pygame.update_game()

# Quit Game
pygame.quit_game()