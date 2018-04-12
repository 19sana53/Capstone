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
		self.y_speed = 5
		self.strength = 7 
		self.score 
		self.state = "running" 
		self.frame = 0 
			
	def tick(self):
		self.move()

	def move(self):
		self.fd(self.speed)

		if self.xcor() > game.SCREEN_WIDTH / 2:
			self.goto(-game.SCREEN_WIDTH / 2, self.ycor())

		if self.xcor() < -game.SCREEN_WIDTH /2 :
			self.goto(game.SCREEN_WIDTH / 2, self.ycor())

		if self.ycor() > game.SCREEN_HEIGHT / 2:
			self.goto(self.xcor(), -game.SCREEN_HEIGHT / 2)

		if self.ycor() < -game.SCREEN_HEIGHT / 2:
			self.goto(self.xcor(), game.SCREEN_HEIGHT / 2)
            
	def jump(self):
		if self.state == "running": 
			self.y_acceleration += self.strength
			self.sety(0)
			self.state = "jumping"
			
		def tick(self): 
			self.setx(self.xcor())
			if self.ycor() < - 100: 
				self.y_acceleration = 0 
				self.y_speed = 0 
				self.sety(-100)
				self.state = "running"
			
			self.y_acceleration += game.gravity 
			self.y_speed += self.y_acceleration 
			self.sety(self.ycor() + self.y_speed)
		
	def turn_left(self):
		self.lt(30)

	def turn_right(self):
		self.rt(30)

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
		
# Create Functions
#functions should be outside the classes

# Initial Game setup
game = spgl.Game(800, 600, "black", "SPGL Minimum Code Example by /u/wynand1004 AKA @TokyoEdTech", 0)
game.coins = 10
game.gravity = -1

# Create Sprites / player
player = Player("triangle", "white", -350, 0)
rock = Rock("circle", "red", -300, 0)
Block = Block("square", "blue", -190, 0)

# Create Labels
score_label = spgl.Label("Score : {}  Lives : {} ".format(game.coins, player.lives), "white", -380, 280)

# Set Keyboard Bindings
game.set_keyboard_binding(spgl.KEY_SPACE, player.jump)
game.set_keyboard_binding(spgl.KEY_LEFT, player.turn_left)
game.set_keyboard_binding(spgl.KEY_RIGHT, player.turn_right)

while True:
    # Call the game tick method
	game.tick()
    
	if game.is_collision(player, rock): 
		player.score -= 5 
	else:
		player.score += 5
    

    	
    
    	
    
    
    
