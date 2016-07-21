"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""

import pygame
import random



# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
light_blue = (150,150,255)
colors = [WHITE, light_blue]

pygame.init()

# Set the width and height of the screen [width, height]


size = (700,500)
screen = pygame.display.set_mode(size)
bg = pygame.image.load("tree.jpg")
bg = pygame.transform.scale(bg,size)
screen.blit(bg,(0,0))


pygame.display.set_caption("Snow")


class SnowFlake():
    
	# This class will be used to create the SnowFlake Objects.
	# It takes: 
		# size - an integer that tells us how big we want the snowflake
		# position - a 2 item list that tells us the coordinates of the snowflake (x,y) 
		# wind - a boolean that lets us know if there is any wind or not.  
	def __init__(self, size, position, wind=False): #the third argument is optional-if none entered, will default to false
		self.size = size
		self.position = position
		self.wind = wind
    
	def fall(self, speed):
        
        # Take in a integer that represents the speed at which the snowflake is falling in the y-direction.  
        # A positive integer will have the snowflake falling down the screen. 
        # A negative integer will have the snowflake falling up the screen. 
        
        # If wind = True
            # - the x direction of the snowflake changes
		
		self.position[1] += speed
		if self.wind == True:
			self.position[0] += speed
		
	def draw(self):
		global screen
		global colors
		pygame.draw.circle(screen, random.choice(colors), self.position,self.size)
		#Uses pygame and the global screen variable to draw the snowflake on the screen
        
        

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()



# Speed
speed = 1


#INITIALIZE YOUR SNOWFLAKE HERE! 
deer = pygame.image.load("reindeer.png")
deer = pygame.transform.scale(deer,(50,100))
x=size[0]-50
y=size[1]-100
screen.blit(deer,(x,y))

# Snow List
snow_list = []

for i in range(random.randint(1,600)):
	snowflake = SnowFlake(3,[random.randint(1,size[0]),random.randint(1,size[1])])
	snow_list.append(snowflake)

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
	screen.blit(bg,(0,0))
	if x>-50:
		x-=1
	else: 
		x = size[0]
	screen.blit(deer,(x,y))

    # --- Drawing code should go here
    # Begin SnowFlake
	for snowflake in snow_list:
		snowflake.draw()
	for snowflake in snow_list:
		snowflake.fall(speed)
		if snowflake.position[1] > size[1]:
			snowflake.position[1] = 0
    



    


    # End Snow
    # --- Go ahead and update the screen with what we've drawn.
	pygame.display.flip()

    # --- Limit to 60 frames per second
	clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE
