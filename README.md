# Scratch-To-Python
An library that helps primary/high school students progress from Scratch to Python much more easily

## Basic Game Design Command
1. Make new **Game Manager** while setting screen
```python
# Set up screen size 800 x 600
pygame = Pygame(800,600)
```*

2. Game Title
```python
pygame.set_game_title("My Game")
```

3. Add New Sprite
```python
my_sprite = pygame.add_sprite('sprite1.png', 50)
```

4. Add/Set Sprite's Costume 
```python
my_sprite = pygame.switch_costume('sprite2.png')
```

5. Set Background/Backdrop Image <br/>
```python
pygame.change_background_image("background.jpg")
```

6. New Scene <br/>
```python
pygame.new_scene()
```

## Motion
1. Move sprite
