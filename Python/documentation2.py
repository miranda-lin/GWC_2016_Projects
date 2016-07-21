import pygame
import random
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (129, 129, 129)
TB = (50,204,203)
LB = (204,255,255)
LP = (255,204,255)
P = (229,204,255)
colors = [TB,LB,LP,P]

def random_color():
	return random.choice(colors)

# initialize the pygame class
pygame.init()

# Set the width and height of the screen [width, height]
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


# Set the title of the window
pygame.display.set_caption("Documentation Hunt")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

class Circle():
	def __init__(self,mouse_position):
		self.mouse_position = list(mouse_position)
		self.size = random.randint(20,80)
		self.color = random_color()
		self.x = random.randint(-5,5)
		self.y = random.randint(-5,5)
		
	def draw(self):
		global screen
		
		pygame.draw.circle(screen,self.color,self.mouse_position,self.size,3)
	
	def move(self): #,x_speed, y_speed
		# self.mouse_position[0] += x_speed
		# self.mouse_position[1] += y_speed
		self.mouse_position[0] += self.x
		self.mouse_position[1] += self.y
		
a=0
circle_list = []
# -------- Main Program Loop -----------
while not done:
	# --- Main event loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

	# --- Game logic should go here
	# if a%30==0:
		# x_speed = random.randint(-10,10)
		# y_speed = random.randint(-10,10)
	# a+=1
	x_speed = 5
	y_speed = 0
	# --- Screen-clearing code goes here

	# Here, we clear the screen to white. Don't put other drawing commands
	# above this, or they will be erased with this command.

	# If you want a background image, replace this clear with blit'ing the
	# background image.
	screen.fill(BLACK)

	# --- Drawing code should go here
	pressed = pygame.mouse.get_pressed()
	pos = pygame.mouse.get_pos()
	
	if pressed[0] == 1:
		#print("Here!")
		circle_list.append(Circle(pos))
	
	for circ in circle_list:
		circ.draw()
		circ.move() #x_speed,y_speed


	# --- Go ahead and update the screen with what we've drawn.
	pygame.display.flip()

	# --- Limit to 60 frames per second
	clock.tick(60)

# Close the window and quit.
pygame.quit()
