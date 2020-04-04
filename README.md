# Scratch-To-Python
An library that helps primary/high school students progress from Scratch to Python much more easily

## Basic Game Design Command
- Make new **Game Manager** while setting screen </li>
```python
# Set up screen size 800 x 600
pygame = Pygame(800,600)
```

- Set **Game Title**
```python
pygame.set_game_title("My Game")
```

- Add **New Sprite**
```python
my_sprite = pygame.add_sprite('sprite1.png', 50)
```

- New **Scene** <br/>
```python
pygame.new_scene()
```

## Motion
- Move sprite 10 **steps**
```python
my_sprite.move(10)
```

- Turn **right** 15 degrees
```python
my_sprite.turn_right(15)
```

- Turn **left** 15 degrees
```python
my_sprite.turn_left(15)
```

- **Go To** specfic position
```python
# Random Position
my_sprite.go_to_random_position()

# Go to specific position (200,100)
my_sprite.go_to(200,100)
```

- Set **Direction** to 100
```python
my_sprite.set_direction(100)
```

- Points toward **Mouse**
```python
my_sprite.point_toward_mouse()
```

- Points toward **another Sprite**
```python
my_sprite.point_toward_sprite(another_sprite)
```

- Change **x** by 10
```python
my_sprite.change_x(10)
```

- Set **x** to 100
```python
my_sprite.set_x(100)
```

- Change **y** by 10
```python
my_sprite.change_y(10)
```

- Set **y** to 100
```python
my_sprite.set_y(100)
```

- **If on edge, bounce**
```python
my_sprite.stop_on_edge()
```

- Set **Rotation Style**
```python
my_sprite.set_rotation_style("all-around")
my_sprite.set_rotation_style("left-right")
my_sprite.set_rotation_style("don't rotate")
```

- Get **x** position
```python
X = my_sprite.get_x_position()
```

- Get **y** position
```python
Y = my_sprite.get_y_position()
```

- Get **direction**
```python
direction = my_sprite.get_direction()
```

## Looks
- Say "Hello!"
```python
my_sprite.say("Hello!")
```

- Switch **costume**
```python
my_sprite.switch_costume('costume1.png')
```

- Switch **backdrop**
```python
pygame.set_background_image('background.jpg')
```

- Change **size** by 10
```python
my_sprite.change_size(10)
```

- Set **size** to 100
```python
my_sprite.set_size(100)
```

- Show **sprite**
```python
my_sprite.show()
```

- Hide **sprite**
```python
my_sprite.hide()
```

## Sound
- Start **sound** 'Meow
```python
pygame.play_sound_effect('effect1.mp3')

pygame.play_background_music('music1.mp3')
```

- Stop all **sound**
```
pygame.stop_sound()
```

## Sensing
- Touch **mouse**
```python
# Return True/False
# Hover
on sprite
result = my_sprite.mouse_hovered_on_sprite()
# Click
result = my_sprite.mouve_clicked_on_sprite()
```

- Touch **another sprite**
```python
# Return True/False
result = my_sprite.touch(another_sprite)
```

- **Key 'Space'** hold/pressed/released
```python
# Return True/False
result = pygame.key_hold('Space')
result = pygame.key_pressed('Space')
result = pygame.key_released('Space')
```

- **Mouse down**
```python
result = pygame.check_mouse_clicked(self)
```
