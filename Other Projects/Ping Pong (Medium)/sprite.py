from colour import *
import pygame
import math
import random

class Sprite(pygame.sprite.Sprite):
	def __init__(self, game_Manager, image_link, scale, screen_width, screen_height):

		self.game_Manager = game_Manager

		self.image = pygame.image.load("images/" + image_link)
		original_width, original_height = self.image.get_size()
		self.image = pygame.transform.scale(self.image, (int(scale * original_width / 100), int(scale *original_height / 100)))
		self.image_link_list = [image_link]
		self.image_list = [self.image]
		self.scale = scale

		self.height = int(scale * original_height / 100)
		self.width = int(scale * original_width / 100)
		self.direction = 0

		self.x = screen_width/2 - original_width/2
		self.y = screen_height/2 - original_height/2
		self.rect = self.image.get_rect()
		self.rect.x = self.x
		self.rect.y = self.y
		self.rotation = 0

		self.x_change = 0
		self.y_change = 0

		self.screen_width = screen_width
		self.screen_height = screen_height

		self.rotation_style = 'all-around' 
		self.pivot = [original_width/2, original_height/2]

		self.waiting = False

		self.visible = True

		self.last = pygame.time.get_ticks()
		self.cooldown = 0

		self.text = ""
		self.SpeechBubble = SpeechBubble(self)

	# If on edge, bounce
	def bounce_on_edge(self):

		# Bounce on right edge - DONE
		if self.x + self.width > self.screen_width:
			self.set_direction(-1 * self.direction)
			self.x = self.screen_width - self.width
		# Bounce on left edge - DONE
		elif self.x < 0:
			self.set_direction(-1 * self.direction)
			self.x = 0

		# Bounce on bottom edge
		if self.y + self.height > self.screen_height:
			if self.direction == 180: self.set_direction(0)
			elif self.direction > 0: self.set_direction(180 - self.direction)
			elif self.direction < 0: self.set_direction(-1 * (180 + self.direction))
			self.y = self.screen_height - self.height
		# Bounce on top edge - DONE
		elif self.y < 0:
			if self.direction == 0: self.set_direction(180)
			elif self.direction < 0: self.set_direction(-1 * (180 + self.direction))
			elif self.direction > 0: self.set_direction(180 - self.direction)
			self.y = 0

	# Change X
	def change_x(self, amount):
		self.x_change = amount

	# Change Y
	def change_y(self, amount):
		self.y_change = -1 * amount

	# Change size
	def change_size(self, amount):
		self.scale += amount

	# Get Direction
	# ISSUE - not adjusted to scratch degree
	def get_direction(self):
		return self.direction

	# Get Size
	def get_size(self):
		return self.scale

	# Get X
	def get_x(self):
		return int(self.x - self.screen_width/2 + self.width/2)

	# Get Y
	def get_y(self):
		return int(self.screen_height/2 - self.height/2 - self.y)

	# Go to specific position
	def go_to(self, x, y):
		self.x = self.screen_width/2 - self.width/2 + x
		self.y = self.screen_height/2 - self.height/2 - y

	# Go to random position
	def go_to_random_position(self):
		self.x = random.randint(int(self.width/2), int(self.screen_width-(self.width/2)))
		self.y = random.randint(int(self.height/2), int(self.screen_height-(self.height/2)))

	# Hide sprite
	def hide(self):
		self.visible = False

	# Move sprite
	def move(self, amount):
		self.x += amount * math.cos(math.radians(self.rotation))
		self.y -= amount * math.sin(math.radians(self.rotation))

	# Check if Mouse clicked on Sprite
	def mouse_clicked_on_sprite(self):

		for event in self.game_Manager.events_list:
			if event.type == pygame.MOUSEBUTTONDOWN:
				pos = pygame.mouse.get_pos()
				if self.rect.collidepoint(pygame.mouse.get_pos()):
					return True

		return False

	# Check if Mouse hovered on Sprite
	def mouse_hovered_on_sprite(self):
		if self.rect.collidepoint(pygame.mouse.get_pos()): return True
		return False

	# Point toward Mouse
	def point_toward_mouse(self):
		mouse_x, mouse_y = pygame.mouse.get_pos()
		rel_x, rel_y = mouse_x - self.x, mouse_y - self.y
		self.rotation = (180 / math.pi) * -math.atan2(rel_y, rel_x)

	# Point toward Sprite
	def point_toward_sprite(self, otherSprite):
		diff_x = otherSprite.x - self.x
		diff_y = self.y - otherSprite.y
		self.rotation = math.degrees(math.atan2(diff_y,diff_x))

	# Say
	def say(self, text):
		self.text = text

	# Set Direction
	def set_direction(self, angle):
		self.rotation = 90 - angle
		self.direction = angle

	# Set Rotation
	def set_rotation_style(self, rotation_style):
		self.rotation_style = rotation_style

	# Set size
	def set_size(self, scale):
		self.scale = scale
		self.height = int(scale * height / 100)
		self.width = int(scale * width / 100)
		self.switchCostume(self.image_list)

	# Set X position
	def set_x(self, amount):
		self.x = self.screen_width/2 - self.width/2 + amount

	# Set Y position
	def set_y(self, amount):
		self.y = self.screen_height/2 - self.height/2 - amount

	# Show sprite
	def show(self):
		self.visible = True

	# Switch Costume
	def switch_costume(self, imageLink):
		if imageLink not in self.image_link_list:
			self.image = pygame.image.load("images/" + imageLink)
			self.image = pygame.transform.scale(self.image, (self.width, self.height))
			self.image_list.append(self.image)
			self.image_link_list.append(imageLink)
		else:
			self.image = self.image_list[self.image_link_list.index(imageLink)]

	# Touch Other Sprite
	def touch(self, other_sprite):
		return pygame.sprite.collide_rect(self, other_sprite)

	# Turn Left
	def turn_left(self,angle):
		self.rotation += angle

	# Turn Right
	def turn_right(self,angle):
		self.rotation -= angle

	# Update Movement
	def update_movement(self):

		now = pygame.time.get_ticks()
		if not self.waiting or (self.waiting and now - self.last >= self.cooldown):
			self.x += self.x_change
			self.y += self.y_change
			self.rect.x = self.x
			self.rect.y = self.y
			self.last = now
			self.waiting = False

		self.SpeechBubble.update_movement()

	# Wait
	def wait(self, seconds):
		if not self.waiting:
			self.last = pygame.time.get_ticks()
			self.cooldown = seconds * 1000
			self.waiting = True

# SPEECH BUBBLE
class SpeechBubble(pygame.sprite.Sprite):
	def __init__(self, parentSprite):
		global screen_height, screen_width

		self.image = pygame.image.load('images/speech.png')
		self.image = pygame.transform.scale(self.image, (150, 150))

		self.font = pygame.font.Font('freesansbold.ttf', 25)

		self.parentSprite = parentSprite

		self.width = 150
		self.height = 150

	def render_text(self):
		global white, green, blue, black

		self.textFont = self.font.render(self.parentSprite.text, True, black, white)
		self.textRect = self.textFont.get_rect() 
		self.textRect.center = (self.x + 80, self.y + 65)

	def update_movement(self):
		self.x = self.parentSprite.x + self.parentSprite.width
		self.y = self.parentSprite.y - self.height