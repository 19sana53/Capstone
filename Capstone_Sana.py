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
        self.speed = 3
        self.score = 0
        player.score = 20 
        player.lives = 3 
        
    def __init__(self): 
		turtle.Turtle.__init__(self)
		self.penup()
		self.hideturtle()
		self.speed(0) 
		self.color("white") 
		self.goto(-290, 310)
		self.score = 0 
 
 	def tick(self):
 		self.move()

	def move(self): 
		self.forward(self.speed)
	
		if self.xcor() > 290 or self.xcor() < -290: 
			self.left(60)
		if self.ycor() > 290 or self.ycor() < -290: 
			self.right(60)
			
	def jump(self):
		pass
		#acceleration, gravity, speed

    def turn_left(self):
        self.lt(30)

    def turn_right(self):
        self.rt(30)

    def accelerate(self):
        self.speed += 1

class Rock(spgl.Sprite):
	def __init__(self, shape, color, rock, x, y):
    	spgl.Sprite.__init__(self, shape, color, x, y)
    	self.rock = rock  	
    	
class Coines(spgl.Sprite):
	def __init__(self, shape, color, rock, coins, x, y):
    	spgl.Sprite.__init__(self, shape, color, x, y)
    	self.coins = coins
	
# Create Functions

# Initial Game setup
game = spgl.Game(800, 600, "black", "SPGL Minimum Code Example by /u/wynand1004 AKA @TokyoEdTech")

# Create Sprites / player
player = Player("triangle", "white", -400, 0)
rock = Rock("circle", "red", -400, 0)

# Create Labels
score_label = spgl.Label("""
Score : {}
Lives: {} """.format(game.Coins), "white", -380, 280)

# Create Buttons (none)

# Set Keyboard Bindings
game.set_keyboard_binding(spgl.KEY_UP, player.jump)
game.set_keyboard_binding(spgl.KEY_LEFT, player.turn_left)
game.set_keyboard_binding(spgl.KEY_RIGHT, player.turn_right)
game.set_keyboard_binding(spgl.KEY_LEFT, player.accelerate)

while True:
	wn.update()
	player.move()
		
    # Call the game tick method
    game.tick()
    
    
    
