import pygame
from colour import *
from sprite import *

class Pygame(object):

	# Constructor Function
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

		self.keyboard_dict = {
			'up'	: pygame.K_UP,
			'right'	: pygame.K_RIGHT,
			'down'	: pygame.K_DOWN,
			'left'	: pygame.K_LEFT,
			'a'		: pygame.K_a,
			'b'		: pygame.K_b,
			'c'		: pygame.K_c,
			'd'		: pygame.K_d,
			'e'		: pygame.K_e,
			'f'		: pygame.K_f,
			'g'		: pygame.K_g,
			'h'		: pygame.K_h,
			'i'		: pygame.K_i,
			'j'		: pygame.K_j,
			'k'		: pygame.K_k,
			'l'		: pygame.K_l,
			'm'		: pygame.K_m,
			'n'		: pygame.K_n,
			'o'		: pygame.K_o,
			'p'		: pygame.K_p,
			'q'		: pygame.K_q,
			'r'		: pygame.K_r,
			's'		: pygame.K_s,
			't'		: pygame.K_t,
			'u'		: pygame.K_u,
			'v'		: pygame.K_v,
			'w'		: pygame.K_w,
			'x'		: pygame.K_x,
			'y'		: pygame.K_y,
			'z'		: pygame.K_z,
		}

	# Add New Sprite Images
	def add_sprite(self, image_link, scale):
		new_sprite = Sprite(self, image_link, scale, self.screen_width, self.screen_height)
		self.sprite_objects.append(new_sprite)
		self.sprite_objects.append(new_sprite.SpeechBubble)
		return new_sprite

	# Rotate Image [WAS FROM STACK OVERFLOW]
	def blit_rotate(self, surf, image, pos, origin_pos, angle):

		# calcaulate the axis aligned bounding box of the rotated image
		w, h       = image.get_size()
		box        = [pygame.math.Vector2(p) for p in [(0, 0), (w, 0), (w, -h), (0, -h)]]
		box_rotate = [p.rotate(angle) for p in box]
		min_box    = (min(box_rotate, key=lambda p: p[0])[0], min(box_rotate, key=lambda p: p[1])[1])
		max_box    = (max(box_rotate, key=lambda p: p[0])[0], max(box_rotate, key=lambda p: p[1])[1])

		# calculate the translation of the pivot 
		pivot        = pygame.math.Vector2(origin_pos[0], -origin_pos[1])
		pivot_rotate = pivot.rotate(angle)
		pivot_move   = pivot_rotate - pivot

		# calculate the upper left origin of the rotated image
		origin = (pos[0] - origin_pos[0] + min_box[0] - pivot_move[0] + w/2, pos[1] - origin_pos[1] - max_box[1] + pivot_move[1] + h/2)

		# get a rotated image
		rotated_image = pygame.transform.rotate(image, angle)

		# rotate and blit the image
		surf.blit(rotated_image, origin)

	# Check for all user input
	def check_event(self):
		self.events_list = pygame.event.get()
		self.key_pressed_list = pygame.key.get_pressed()

	# Check if user has quit
	def check_quit(self):
		for event in self.events_list:	
			if event.type == pygame.QUIT: return True
		return False

	# Get Mouse X Position
	def get_mouse_x_position(self):
		pos = pygame.mouse.get_pos()
		return pos[0] - int(self.width/2)

	# Get Mouse Y Position
	def get_mouse_y_position(self):
		pos = pygame.mouse.get_pos()
		return pos[1] - int(self.height/2)

	# Get Time
	def get_time(self):
		return pygame.time.get_ticks()

	# Check if Certain Key is Hold
	def key_hold(self, key):
		hit = self.keyboard_dict[key]
		if self.key_pressed_list[hit]: return True
		return False

	# Check if Certain Key is Pressed
	def key_pressed(self, key):
		hit = self.keyboard_dict[key]
		for event in self.events_list:
			if event.type == pygame.KEYDOWN and event.key == hit: return True
		return False

	# Check if Certain Key is Released
	def key_released(self, key):
		hit = self.keyboard_dict[key]
		for event in self.events_list:
			if event.type == pygame.KEYUP and event.key == hit: return True
		return False

	# Check if Mouse has Clicked
	def check_mouse_clicked(self):
		for event in self.events_list:
			if event.type == pygame.MOUSEBUTTONDOWN: return True
		return False

	# Check if Mouse Click has been Holded
	def check_mouse_hold(self):
		if pygame.mouse.get_pressed()[0]: return True
		return False

	# Reset to New Scene
	def new_scene(self):
		for sprite in self.sprite_objects: sprite = None
		self.sprite_objects = []

	# Play Background Music
	def play_background_music(self, link):
		pygame.mixer.music.load("sounds/" + link)
		pygame.mixer.music.play(-1)

	# Play Sound Effect
	def play_sound_effect(self, link):
		pygame.mixer.music.load("sounds/" + link)
		pygame.mixer.music.play(0)

	# Quit game
	def quit_game(self):
		pygame.quit()
		quit()

	# Set Background Image
	def set_background_image(self, link):
		# If not in list, convert the image
		if link not in self.background_images_links_list:
			self.current_background_image = pygame.image.load("images/" + link).convert()
			self.current_background_image = pygame.transform.scale(self.current_background_image, (self.width, self.height))
			self.background_images_links_list.append(link)
			self.background_images_list.append(self.current_background_image)
		# If in list, just get the converted image from list
		else:
			self.current_background_image = self.background_images_list[self.background_images_links_list.index(link)]

	# Start Game
	def start_game(self):

		# blank background
		self.screen.fill((0,0,0))

		# Show current background if has one
		if len(self.background_images_list) != 0: self.screen.blit(self.current_background_image, [0, 0])

		# Set up each sprite
		for sprite in self.sprite_objects:
			if not isinstance(sprite, SpeechBubble):
				sprite.update_movement()
				if sprite.rotation_style == 'all-around':
					w, h = sprite.image.get_size()
					self.blit_rotate(self.screen, sprite.image, [sprite.x, sprite.y], (w//2, h//2), sprite.rotation)
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

	# Set Game Title
	def set_game_title(self, text):
		pygame.display.set_caption(text)

	# Stop Sound
	def stop_sound(self):
		pygame.mixer.music.stop()

	# Update Game
	def update_game(self):

		# Background
		self.screen.fill((0,0,0))
		if len(self.background_images_list) != 0: self.screen.blit(self.current_background_image, [0, 0])

		# Update sprite image position
		for sprite in self.sprite_objects:
			sprite.update_movement()
			if isinstance(sprite, SpeechBubble):
				if sprite.parentSprite.text != "":
					sprite.render_text()
					self.screen.blit(sprite.image, [sprite.x, sprite.y])
					self.screen.blit(sprite.textFont, sprite.textRect)
			elif sprite.visible == True:
					if sprite.rotation_style == 'all-around':
						w, h = sprite.image.get_size()
						self.blit_rotate(self.screen, sprite.image, [sprite.x, sprite.y], (w//2, h//2), sprite.rotation)
					elif sprite.rotation_style == 'left-right':
						if sprite.rotation >= -90 and sprite.rotation <= 90:
							self.screen.blit(sprite.image, [sprite.x - (sprite.width/2), sprite.y - (sprite.height/2)])
						else:
							self.screen.blit(pygame.transform.flip(sprite.image, True, False),[sprite.x - (sprite.width/2), sprite.y - (sprite.height/2)])
					else:
						self.screen.blit(sprite.image, [sprite.x - (sprite.width/2), sprite.y - (sprite.height/2)])

		
		# Text Object
		count = 0
		for sprite in self.text_objects:
			text_rect = self.text_rect_objects[count]
			self.screen.blit(sprite, text_rect)
			count += 1

		# Remove all text objects for new
		self.text_objects = []
		self.text_rect_objects = []

		# Tick
		pygame.display.update()
		self.clock.tick(60)

	# Write Text
	def write_text(self, text, font_size, x, y):
		font = pygame.font.Font('freesansbold.ttf', font_size)
		text = font.render(text, True, black) 
		textRect = text.get_rect()
		new_x = self.screen_width/2 + x
		new_y = self.screen_height/2 - y
		textRect.center = (new_x,new_y)
		self.text_objects.append(text)
		self.text_rect_objects.append(textRect)
