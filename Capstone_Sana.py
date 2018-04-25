# SPGL Minimal Code by /u/wynand1004 AKA @TokyoEdTech
# Requires SPGL Version 0.8 or Above
# SPGL Documentation on Github: https://wynand1004.github.io/SPGL
# Use this as the starting point for your own games

# Import SPGL
import spgl

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
		self.score 
		self.state = "running" 
		self.frame = 0 
		
	def tick(self): 	
		if self.state == "jumping":	
			self.sety(self.ycor() + self.y_speed)
			self.y_acceleration += game.gravity 
			self.y_speed += self.y_acceleration 
					
		self.setx(self.xcor() + self.x_speed)
		
		for block in blocks:
			if game.is_collision(self, block):
				self.y_acceleration = 0 
				self.y_speed = 0 
				self.sety(block.ycor() + block.height +1)
				self.state = "running"	
		
		if game.is_collision(self, pipe):
			self.y_acceleration = 0 
			self.y_speed = 0 
			self.sety(pipe.ycor() + pipe.height + 5)
			self.state = "running"


	def jump(self):
		if self.state == "running": 
			self.y_acceleration += self.strength
			self.state = "jumping"
			self.sety(self.ycor() + 5)
			game.play_sound("jump.wav")
			
	def turn_left(self):
		self.x_speed = -3 

	def turn_right(self):
		self.x_speed = 3 

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

# Create Functions

# Initial Game setup
game = spgl.Game(800, 600, "black", "Sana Kureshi - SKYDIVER MARIO", 0)
game.coins = 10
game.gravity = -0.3
game.play_sound("theme_song.wav -v 0.6", 10) 

# Create Sprites / player
player = Player("triangle", "white", 300, -250)
player.set_image("mario.gif", 25, 30)

donkeykong = Donkeykong("circle", "red", 255, 255)
donkeykong.set_image("donkeykong.gif", 50, 60) 

peach = Peach("circle", "red", 310, 250)
peach.set_image("peach.gif", 50, 70) 

pipe = Pipe("triangle", "blue", 300, -250)
pipe.set_image("pipe.gif", 80, 80)

#ROCKS
rock = Rock("circle", "red", 110, -55)
rock.set_image("rock.gif", 25, 25)

rock = Rock("circle", "red", 155, -100)
rock.set_image("rock.gif", 25, 25)
	
#BLOCKS
blocks = []
blocks.append(Block("brick2.gif", "blue", 150 , -100))
blocks.append(Block("brick3.gif", "red", 210, 50))
blocks.append(Block("brick2.gif", "red", -200, -150))
blocks.append(Block("brick3.gif", "red",  -180, 200))
blocks.append(Block("brick2.gif", "red",  -230, 30)) 
blocks.append(Block("brick2.gif", "red",  260, 200))
 
for block in blocks:
	block.set_bounding_box(75, 25)

#COINS
coins = []
coins.append(Coin("coins.gif", "blue", -150, 250))
coins.append(Coin("coins.gif", "blue", 200 , 95))
coins.append(Coin("coins.gif", "blue",  -240, 75))
coins.append(Coin("coins.gif", "blue", -180 , 250))

for coin in coins: 
	coin.set_bounding_box (30, 20)
	
 
# Create Labels
score_label = spgl.Label("Score : {}".format(game.coins), "white", -380, 280)
game.set_background("background.gif")

# Set Keyboard Bindings
game.set_keyboard_binding(spgl.KEY_SPACE, player.jump)
game.set_keyboard_binding(spgl.KEY_LEFT, player.turn_left)
game.set_keyboard_binding(spgl.KEY_RIGHT, player.turn_right)

while True:
    # Call the game tick method
	game.tick()
     
	if game.is_collision(player, rock): 
		player.score -= 5
		score_label.update("Score: {}".format(player.score))
		player.goto(300, -250)
	else:
		player.score += 0
		
	if game.is_collision(player, coin):  
		player.score += 10
		score_label.update("Score: {}".format(player.score))
		player.goto()
	else: 
		player.score += 0 
		
	if game.is_collision(player, donkeykong): 
		player.score += 10
		score_label.update("Score: {}".format(player.score))
	else: 
		player.score += 0
		
	print(player.state, player.y_acceleration, player.y_speed)
    	
    
    
    
