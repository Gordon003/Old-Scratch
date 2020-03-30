import pygame
from colour import *
from sprite import *

class Pygame(object):
	def __init__(self, width, height):
		pygame.init()
		self.width = width
		self.height = height
		self.screen = pygame.display.set_mode((self.width, self.height))
		self.clock = pygame.time.Clock()

		self.current_background_image = ''
		self.background_images_list = []
		self.background_images_links_list = []

		self.sprite_objects = []
		self.text_objects = []
		self.text_rect_objects = []

		self.key_pressed_list = []
		self.events_list = []

		self.screen_height = height
		self.screen_width = width

	def addSprite(self, image_link, scale):
		new_sprite = Sprite(self, image_link, scale, self.screen_width, self.screen_height)
		self.sprite_objects.append(new_sprite)
		self.sprite_objects.append(new_sprite.speechBubble)
		return new_sprite

	def blitRotate(self, surf, image, pos, originPos, angle):

		# calcaulate the axis aligned bounding box of the rotated image
		w, h       = image.get_size()
		box        = [pygame.math.Vector2(p) for p in [(0, 0), (w, 0), (w, -h), (0, -h)]]
		box_rotate = [p.rotate(angle) for p in box]
		min_box    = (min(box_rotate, key=lambda p: p[0])[0], min(box_rotate, key=lambda p: p[1])[1])
		max_box    = (max(box_rotate, key=lambda p: p[0])[0], max(box_rotate, key=lambda p: p[1])[1])

		# calculate the translation of the pivot 
		pivot        = pygame.math.Vector2(originPos[0], -originPos[1])
		pivot_rotate = pivot.rotate(angle)
		pivot_move   = pivot_rotate - pivot

		# calculate the upper left origin of the rotated image
		origin = (pos[0] - originPos[0] + min_box[0] - pivot_move[0] + w/2, pos[1] - originPos[1] - max_box[1] + pivot_move[1] + h/2)

		# get a rotated image
		rotated_image = pygame.transform.rotate(image, angle)

		# rotate and blit the image
		surf.blit(rotated_image, origin)
		#pygame.draw.circle(self.screen, (0, 255, 0), [int(pos[0] + w/2),int(pos[1] + h/2)], 7, 0)

	def changeBackgroundImage(self, link):
		if link not in self.background_images_links_list:
			self.current_background_image = pygame.image.load("images/" + link).convert()
			self.current_background_image = pygame.transform.scale(self.current_background_image, (self.width, self.height))
			self.background_images_links_list.append(link)
			self.background_images_list.append(self.current_background_image)
		else:
			self.current_background_image = self.background_images_list[self.background_images_links_list.index(link)]

	def checkEvent(self):
		self.events_list = pygame.event.get()
		self.key_pressed_list = pygame.key.get_pressed()

	def checkQuit(self):
		for event in self.events_list:	
			if event.type == pygame.QUIT:
				return True
		return False

	def getMousePosition(self):
		pos = pygame.mouse.get_pos()
		fin = [pos[0] - int(self.width/2), pos[1] - int(self.height/2)]
		return fin

	def getTime(self):
		return pygame.time.get_ticks()

	def keyHold(self, key):
		if self.key_pressed_list[key]:
			return True

		return False

	def keyPressed(self, key):
		for event in self.events_list:
			if event.type == pygame.KEYDOWN and event.key == key:
				return True
		return False

	def keyReleased(self, key):
		for event in self.events_list:
			if event.type == pygame.KEYUP and event.key == key:
				return True
		return False

	def checkMouseClicked(self):
		for event in self.events_list:
			if event.type == pygame.MOUSEBUTTONDOWN:
				return True
		return False

	def checkMouseHold(self):
		if pygame.mouse.get_pressed()[0]:
			return True
		return False

	def newScene(self):
		for sprite in self.sprite_objects:
			sprite = None
		self.sprite_objects = []

	def playBackgroundMusic(self, link):
		pygame.mixer.music.load(link)
		pygame.mixer.music.play(-1)

	def playSoundEffect(self, link):
		pygame.mixer.music.load(link)
		pygame.mixer.music.play(0)

	def quitGame(self):
		pygame.quit()
		quit()

	def startGame(self):

		self.screen.fill((0,0,0))

		if len(self.background_images_list) != 0:
			self.screen.blit(self.current_background_image, [0, 0])

		for sprite in self.sprite_objects:
			if not isinstance(sprite, SpeechBubble):
				sprite.updateMovement()
				if sprite.rotation_style == 'all-around':
					w, h = sprite.image.get_size()
					self.blitRotate(self.screen, sprite.image, [sprite.x, sprite.y], (w//2, h//2), sprite.rotation)
				elif sprite.rotation_style == 'left-right':
					if sprite.rotation >= -90 and sprite.rotation <= 90:
						self.screen.blit(sprite.image, [sprite.x - (sprite.width/2), sprite.y - (sprite.height/2)])
					else:
						self.screen.blit(pygame.transform.flip(sprite.image, True, False),[sprite.x - (sprite.width/2), sprite.y - (sprite.height/2)])
				else:
					self.screen.blit(sprite.image, [sprite.x - (sprite.width/2), sprite.y - (sprite.height/2)])

		count = 0
		for sprite in self.text_objects:
			text_rect = self.text_rect_objects[count]
			self.screen.blit(sprite, text_rect)
			count += 1

	def setGameTitle(self, text):
		pygame.display.set_caption(text)

	def stopSound(self):
		pygame.mixer.music.stop()

	def updateGame(self):

		self.screen.fill((0,0,0))

		if len(self.background_images_list) != 0:
			self.screen.blit(self.current_background_image, [0, 0])

		for sprite in self.sprite_objects:
			sprite.updateMovement()
			if isinstance(sprite, SpeechBubble):
				if sprite.parentSprite.text != "":
					sprite.renderText()
					self.screen.blit(sprite.image, [sprite.x, sprite.y])
					self.screen.blit(sprite.textFont, sprite.textRect)
			elif sprite.visible == True:
					if sprite.rotation_style == 'all-around':
						w, h = sprite.image.get_size()
						self.blitRotate(self.screen, sprite.image, [sprite.x, sprite.y], (w//2, h//2), sprite.rotation)
					elif sprite.rotation_style == 'left-right':
						if sprite.rotation >= -90 and sprite.rotation <= 90:
							self.screen.blit(sprite.image, [sprite.x - (sprite.width/2), sprite.y - (sprite.height/2)])
						else:
							self.screen.blit(pygame.transform.flip(sprite.image, True, False),[sprite.x - (sprite.width/2), sprite.y - (sprite.height/2)])
					else:
						self.screen.blit(sprite.image, [sprite.x - (sprite.width/2), sprite.y - (sprite.height/2)])

		count = 0
		for sprite in self.text_objects:
			text_rect = self.text_rect_objects[count]
			self.screen.blit(sprite, text_rect)
			count += 1


		self.text_objects = []
		self.text_rect_objects = []

		pygame.display.update()
		self.clock.tick(60)

	def writeText(self, text, font_size, x, y):
		font = pygame.font.Font('freesansbold.ttf', font_size)
		text = font.render(text, True, black) 
		textRect = text.get_rect()
		new_x = self.screen_width/2 + x
		new_y = self.screen_height/2 - y
		textRect.center = (new_x,new_y)
		self.text_objects.append(text)
		self.text_rect_objects.append(textRect)
