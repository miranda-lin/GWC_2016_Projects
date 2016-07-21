import pygame
import random
from city2 import Scroller
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
pygame.display.set_caption("Runner Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

class RunnerSprite(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("totoro.png")
		self.rect = self.image.get_rect()
		self.image = pygame.transform.scale(self.image,(60,60))
	def draw(self,pos):
		global screen
		screen.blit(self.image,pos)
	def update(self,x,y):
		self.rect = pygame.rect.move(x,y)

FRONT_SCROLLER_COLOR = (0,0,30)
MIDDLE_SCROLLER_COLOR = (30,30,100)
BACK_SCROLLER_COLOR = (50,50,150)
BACKGROUND_COLOR = (17, 9, 89)

runner = RunnerSprite()
all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(runner)
runner.draw((SCREEN_WIDTH-100,100))

back_scroller = Scroller(screen,SCREEN_WIDTH, 100, SCREEN_HEIGHT-100, BACK_SCROLLER_COLOR, 1)
middle_scroller = Scroller(screen,SCREEN_WIDTH, 300, SCREEN_HEIGHT-70, MIDDLE_SCROLLER_COLOR, 2)
front_scroller = Scroller(screen,SCREEN_WIDTH, 500, SCREEN_HEIGHT-20, FRONT_SCROLLER_COLOR, 3)
back_scroller.add_buildings(0)
middle_scroller.add_buildings(0)
front_scroller.add_buildings(0)
a=0

# -------- Main Program Loop -----------
while not done:
	# --- Main event loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

	# --- Game logic should go here
	if a%(SCREEN_WIDTH)==0:
		back_scroller.add_buildings(-SCREEN_WIDTH)
	if a%(int(SCREEN_WIDTH/2))==0:
		middle_scroller.add_buildings(-SCREEN_WIDTH)
	if a%(int(SCREEN_WIDTH/3))==0:
		front_scroller.add_buildings(-SCREEN_WIDTH)
	a+=1
	# --- Screen-clearing code goes here

	# Here, we clear the screen to white. Don't put other drawing commands
	# above this, or they will be erased with this command.

	# If you want a background image, replace this clear with blit'ing the
	# background image.
	screen.fill(BLACK)

	# --- Drawing code should go here
	back_scroller.draw_buildings()
	back_scroller.move_buildings()
	middle_scroller.draw_buildings()
	middle_scroller.move_buildings()
	front_scroller.draw_buildings()
	front_scroller.move_buildings()
	x = pygame.mouse.get_pos()[0]
	y = pygame.mouse.get_pos()[1]
	runner.draw((x-30,y-30))
	runner.update(x,y)
	# --- Go ahead and update the screen with what we've drawn.
	pygame.display.flip()

	# --- Limit to 60 frames per second
	clock.tick(60)

# Close the window and quit.
pygame.quit()
