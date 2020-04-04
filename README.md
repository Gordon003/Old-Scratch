# Scratch-To-Python
An library that helps primary/high school students progress from Scratch to Python much more easily

## Basic Game Design Command
1. Make new **Game Manager** while setting screen
```python
# Set up screen size 800 x 600
pygame = Pygame(800,600)
```

2. Set **Game Title**
```python
pygame.set_game_title("My Game")
```

3. Add **New Sprite** <br/>
Warning: the images must be in the images folder
```python
my_sprite = pygame.add_sprite('sprite1.png', 50)
```

## Motion
1. Move sprite
