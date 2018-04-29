# SPGL Minimal Code by /u/wynand1004 AKA @TokyoEdTech
# Requires SPGL Version 0.8 or Above
# SPGL Documentation on Github: https://wynand1004.github.io/SPGL
# Use this as the starting point for your own games

# Import SPGL
import spgl
import os 

# Create Classes
class Player(spgl.Sprite):
	def __init__(self, shape, color, x, y):
		spgl.Sprite.__init__(self, shape, color, x, y)
		self.penup()
		self.score = 0
		self.lives = 3 
		self.color("white") 
		self.shape("triangle")
		self.speed = 1
		self.y_acceleration = 0 
		self.x_acceleration = 0 
		self.y_speed = 4
		self.x_speed = 0
		self.strength = 3
		self.score = 10
		self.state = "running" 
		self.frame = 0 
		
	def tick(self): 	
		self.sety(self.ycor() + self.y_speed)
		self.y_acceleration += game.gravity 
		self.y_speed += self.y_acceleration 
					
		self.setx(self.xcor() + self.x_speed)
		
		for block in blocks:
			if game.is_collision(self, block) and self.ycor() > block.ycor():
				print("BLOCK COLLISION")
				self.y_acceleration = 0 
				self.y_speed = 0 
				self.sety(block.ycor() + block.height)
				self.state = "running"
		
		for rock in rocks: 
			if game.is_collision(self, rock):
				print("ROCK COLLISION")
				self.y_acceleration = 0 
				self.y_speed = 0 
				self.sety(rock.ycor() + rock.height)
				self.state = "running"
				self.score -= 20
				player.goto(300, -250)
				score_label.update("SCORE: {}".format(player.score))
				
		for coin in coins: 
			if game.is_collision(self, coin):
				print("COIN COLLISION")
				self.y_acceleration = 0 
				self.y_speed = 0 
				coin.destroy()
				self.state = "running"
				game.play_sound("coin.wav -v 0.1")
				self.score += 30
				score_label.update("SCORE: {}".format(self.score)) 
		
		if game.is_collision(self, pipe):
			print("PIPE COLLISION")
			self.y_acceleration = 0 
			self.y_speed = 0 
			self.sety(pipe.ycor() + pipe.height)
			self.state = "running"

		# Off screen
		if self.ycor() < -300:
			self.goto(300, -250)
			self.y_acceleration = 0
			self.y_speed = 0
			self.x_speed = 0

	def jump(self):
		if self.state == "running": 
			self.y_acceleration += self.strength
			self.state = "jumping"
			self.sety(self.ycor() + 5)
			game.play_sound("jump.wav -v 0.2")
			
	def turn_left(self):
		self.x_speed = -5 

	def turn_right(self):
		self.x_speed = 5
	
	def end_game(self):
		game.exit()
	
class Rock(spgl.Sprite):
	def __init__(self, shape, color, x, y):
		spgl.Sprite.__init__(self, shape, color, x, y)
    	
class Coin(spgl.Sprite):
	def __init__(self, shape, color, x, y):
		spgl.Sprite.__init__(self, shape, color, x, y)
		
class Block(spgl.Sprite):
	def __init__(self, shape, color, x, y):
		spgl.Sprite.__init__(self, shape, color, x, y) 
		self.speed = 1

class Pipe(spgl.Sprite): 
	def __init__(self, shape, color, x, y):
		spgl.Sprite.__init__(self, shape, color, x, y) 
		self.speed = 1
		
class Donkeykong(spgl.Sprite): 
	def __init__(self, shape, color, x, y):
		spgl.Sprite.__init__(self, shape, color, x, y) 
		
class Peach(spgl.Sprite): 
	def __init__(self, shape, color, x, y):
		spgl.Sprite.__init__(self, shape, color, x, y) 	
		
# Initial Game setup
game = spgl.Game(800, 600, "black", "Sana Kureshi - SUPER MARIO BROS.", 7)
game.coins = 10
game.gravity = -0.3
game.play_sound("background_sound.wav -v 0.6", 57) 

# Create Sprites / player
player = Player("triangle", "white", 300, -250)
player.set_image("mario.gif", 50, 60)

donkeykong = Donkeykong("circle", "red", 310, 250)
donkeykong.set_image("donkeykong.gif", 50, 60) 

peach = Peach("circle", "red", 255, 255)
peach.set_image("peach.gif", 50, 70) 

pipe = Pipe("triangle", "blue", 300, -250)
pipe.set_image("pipe.gif", 80, 80)

#ROCKS
rocks = []
rocks.append(Rock("rock.gif", "red", 140, -110))
rocks.append(Rock("rock.gif", "red", 250, 90))
rocks.append(Rock("rock.gif", "red", -210, 240))
rocks.append(Rock("rock.gif", "red", -210, 75))

for rock in rocks: 
	rock.set_bounding_box(25, 25)
	
#BLOCKS
blocks = []
blocks.append(Block("brick2.gif", "blue", 150 , -150))
blocks.append(Block("brick3.gif", "red", 210, 50))
blocks.append(Block("brick2.gif", "red", -200, -150))
blocks.append(Block("brick3.gif", "red",  -180, 200))
blocks.append(Block("brick2.gif", "red",  -230, 30)) 
blocks.append(Block("brick2.gif", "red",  260, 200))
blocks.append(Block("brick2.gif", "red",  0, 0))
 
for block in blocks:
	block.set_bounding_box(150, 50)

#COINS
coins = []
coins.append(Coin("coins.gif", "blue", -150, 250))
coins.append(Coin("coins.gif", "blue", 200 , 95))
coins.append(Coin("coins.gif", "blue",  -240, 75))
coins.append(Coin("coins.gif", "blue", -180 , 250))
coins.append(Coin("coins.gif", "blue", 40, 45))

for coin in coins: 
	coin.set_bounding_box (30, 20)

# Create Labels
score_label = spgl.Label("SCORE : {}".format(game.coins), "white", -360, 260, font_size = 20)
game.set_background("background.gif")

# Set Keyboard Bindings
game.set_keyboard_binding(spgl.KEY_SPACE, player.jump)
game.set_keyboard_binding(spgl.KEY_LEFT, player.turn_left)
game.set_keyboard_binding(spgl.KEY_RIGHT, player.turn_right)
game.set_keyboard_binding(game.exit, "q")

while True:
	os.system("clear") 
	
    # Call the game tick method
	game.tick()
	
	if game.is_collision(player, peach): 
		player.score += 50
		score_label.update("SCORE: {}".format(player.score))
		print("MISSION COMPLETE! PEACH IS SAFE WITH MARIO :))") 
		game.exit()
	else: 
		player.score += 0
	
	print(player.state, player.xcor(), player.ycor(), player.y_acceleration, player.y_speed)