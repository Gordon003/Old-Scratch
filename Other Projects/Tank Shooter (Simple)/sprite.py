from colour import *
import pygame
import math
import random

class Sprite(pygame.sprite.Sprite):
	def __init__(self, game_Manager, image_link, scale, screen_width, screen_height):

		self.game_Manager = game_Manager

		self.image = pygame.image.load("images/" + image_link)
		width, height = self.image.get_size()
		self.image = pygame.transform.scale(self.image, (int(scale * width / 100), int(scale *height / 100)))
		self.image_link_list = [image_link]
		self.image_list = [self.image]
		self.scale = scale

		self.x = screen_width/2 - width/2
		self.y = screen_height/2 - height/2
		self.rect = self.image.get_rect()
		self.rect.x = self.x
		self.rect.y = self.y
		self.rotation = 0

		self.x_change = 0
		self.y_change = 0

		self.height = int(scale * height / 100)
		self.width = int(scale * width / 100)
		self.direction = 0

		self.screen_width = screen_width
		self.screen_height = screen_height

		self.rotation_style = 'all-around' 
		self.pivot = [width/2, height/2]

		self.waiting = False

		self.visible = True

		self.last = pygame.time.get_ticks()
		self.cooldown = 0

		self.text = ""
		self.speechBubble = SpeechBubble(self)

	def changeX(self, amount):
		self.x_change = amount

	def changeY(self, amount):
		self.y_change = -1 * amount

	def changeSize(self, amount):
		self.scale += amount

	def getDirection(self):
		return self.rotation + 90

	def getSize(self):
		return self.scale

	def getX(self):
		return int(self.x - self.screen_width/2 + self.width/2)

	def getY(self):
		return int(self.screen_height/2 - self.height/2 - self.y)

	def goTo(self, x, y):
		self.x = self.screen_width/2 - self.width/2 + x
		self.y = self.screen_height/2 - self.height/2 - y

	def goToRandomPosition(self):
		self.x = random.randint(int(self.width/2), int(self.screen_width-(self.width/2)))
		self.y = random.randint(int(self.height/2), int(self.screen_height-(self.height/2)))

	def hide(self):
		self.visible = False

	def move(self, amount):
		self.x += amount * math.cos(math.radians(self.rotation))
		self.y -= amount * math.sin(math.radians(self.rotation))

	def mouseClickedOnSprite(self):

		for event in self.game_Manager.events_list:
			if event.type == pygame.MOUSEBUTTONDOWN:
				pos = pygame.mouse.get_pos()
				if self.rect.collidepoint(pygame.mouse.get_pos()):
					return True

		return False

	def mouseHoveredOnSprite(self):
		if self.rect.collidepoint(pygame.mouse.get_pos()): return True
		return False

	def pointTowardMouse(self):
		mouse_x, mouse_y = pygame.mouse.get_pos()
		rel_x, rel_y = mouse_x - self.x, mouse_y - self.y
		self.rotation = (180 / math.pi) * -math.atan2(rel_y, rel_x)

	def pointTowardSprite(self, otherSprite):
		diff_x = otherSprite.x - self.x
		diff_y = self.y - otherSprite.y
		self.rotation = math.degrees(math.atan2(diff_y,diff_x))


	def say(self, text):
		self.text = text

	def setDirection(self, angle):
		self.rotation = angle - 90

	def setRotation(self, angle):
		self.rotation = angle - 90

	def setRotationStyle(self, rotation_style):
		self.rotation_style = rotation_style

	def setSize(self, scale):
		self.scale = scale
		self.height = int(scale * height / 100)
		self.width = int(scale * width / 100)
		self.switchCostume(self.image_list)

	def setX(self, amount):
		self.x = self.screen_width/2 - self.width/2 + amount

	def setY(self, amount):
		self.y = self.screen_height/2 - self.height/2 - amount

	def show(self):
		self.visible = True

	def stopOnEdge(self):

		if self.x + self.width > self.screen_width:
			self.x = self.screen_width - self.width
		elif self.x < 0:
			self.x = 0

		if self.y + self.height > self.screen_height:
			self.y = self.screen_height - self.height
		elif self.y < 0:
			self.y = 0

	def switchCostume(self, imageLink):
		if imageLink not in self.image_link_list:
			self.image = pygame.image.load("images/" + imageLink)
			self.image = pygame.transform.scale(self.image, (self.width, self.height))
			self.image_list.append(self.image)
			self.image_link_list.append(imageLink)
		else:
			self.image = self.image_list[self.image_link_list.index(imageLink)]

	def touch(self, otherSprite):
		return pygame.sprite.collide_rect(self, otherSprite)

	def turnLeft(self,angle):
		self.rotation += angle

	def turnRight(self,angle):
		self.rotation -= angle

	def updateMovement(self):

		now = pygame.time.get_ticks()
		if not self.waiting or (self.waiting and now - self.last >= self.cooldown):
			self.x += self.x_change
			self.y += self.y_change
			self.rect.x = self.x
			self.rect.y = self.y
			self.last = now
			self.waiting = False

		self.speechBubble.updateMovement()

	def wait(self, seconds):
		if not self.waiting:
			self.last = pygame.time.get_ticks()
			self.cooldown = seconds * 1000
			self.waiting = True


class SpeechBubble(pygame.sprite.Sprite):
	def __init__(self, parentSprite):
		global screen_height, screen_width

		self.image = pygame.image.load('images/speech.png')
		self.image = pygame.transform.scale(self.image, (150, 150))

		self.font = pygame.font.Font('freesansbold.ttf', 25)

		self.parentSprite = parentSprite

		self.width = 150
		self.height = 150

	def renderText(self):
		global white, green, blue, black

		self.textFont = self.font.render(self.parentSprite.text, True, black, white)
		self.textRect = self.textFont.get_rect() 
		self.textRect.center = (self.x + 80, self.y + 65)

	def updateMovement(self):
		self.x = self.parentSprite.x + self.parentSprite.width
		self.y = self.parentSprite.y - self.height