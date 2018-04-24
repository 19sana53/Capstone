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
		self.setx(self.xcor())
		
		if game.is_collision(self, pipe):
			self.y_acceleration = 0 
			self.y_speed = 0 
			self.sety(pipe.ycor() + pipe.height + 1)
			self.state = "running"
			
		elif game.is_collision(self, block):
			self.y_acceleration = 0 
			self.y_speed = 0 
			self.sety(block.ycor() + block.height +1)
			self.state = "running"	
	
		else:
			self.sety(self.ycor() + self.y_speed)
			self.y_acceleration += game.gravity 
			self.y_speed += self.y_acceleration 
			
		self.x_speed += self.x_acceleration 
		if self.x_speed > 3:
			self.x_speed = 3
			
		if self.x_speed < -3:
			self.x_speed = -3
		self.setx(self.xcor() + self.x_speed)
            
	def jump(self):
		if self.state == "running": 
			self.y_acceleration += self.strength
			self.state = "jumping"
			self.sety(self.ycor() + 5)
			
	def turn_left(self):
		self.x_acceleration -= 1 
		if self.x_acceleration < -3:
			self.x_acceleration = -3

	def turn_right(self):
		self.x_acceleration += 1 
		if self.x_acceleration > 3:
			self.x_acceleration = 1

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
		
# Create Functions

# Initial Game setup
game = spgl.Game(800, 600, "black", "Sana Kureshi - SUICIDAL MARIO", 1)
game.coins = 10
game.gravity = -0.3

# Create Sprites / player
player = Player("triangle", "white", 300, -250)
player.set_image("mario.gif", 50, 60)

pipe = Pipe("triangle", "blue", 300, -250)
pipe.set_image("pipe.gif", 80, 80)

rock = Rock("circle", "red", 110, -55)
rock.set_image("rock.gif", 25, 25)

#BLOCKS
block = Block("square", "blue", 150 , -100)
block.set_image("brick2.gif", 150, 50)

block = Block("triangle", "red", 210, 50)
block.set_image("brick3.gif", 150, 50) 

block = Block("triangle", "red", -200, -150)
block.set_image("brick2.gif", 150, 50) 

block = Block("triangle", "red", -180, 200)
block.set_image("brick3.gif", 150, 50) 

#COINS
coin = Coin("circle", "red", -200, 150) 
coin.set_image("coins.gif", 30, 20) 

coin = Coin("circle", "blue", 200 , 95) 
coin.set_image("coins.gif", 30, 20) 

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
	
	#coin should disappear once hit 
	if game.is_collision(player, coin):  
		player.score += 10
		score_label.update("Score: {}".format(player.score))
		player.goto()
	else: 
		player.score += 0 
		
	print(player.state)
    	
    
    
    
