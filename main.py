import pygame
import tetrisboard
import random

def main():
	"""
	 Pygame base template for opening a window
	 
	 Sample Python/Pygame Programs
	 Simpson College Computer Science
	 http://programarcadegames.com/
	 http://simpson.edu/computer-science/
	 
	 Explanation video: http://youtu.be/vRB_983kUMc
	"""

	 
	# Define some colors
	BLACK = (0, 0, 0)
	WHITE = (255, 255, 255)
	GREEN = (0, 255, 0)
	RED = (255, 0, 0)
	 
	pygame.init()
	 
	# Set the width and height of the screen [width, height]
	size = (400, 800)
	screen = pygame.display.set_mode(size)
	 
	pygame.display.set_caption("My Game")
	 
	# Loop until the user clicks the close button.
	done = False
	 
	# Used to manage how fast the screen updates
	clock = pygame.time.Clock()

	tetris = tetrisboard.TetrisBoard()
	 
	# -------- Main Program Loop -----------
	x = 0
	y = 0
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


		screen.fill(WHITE)
	 
		# --- Drawing code should go here 
        
		#if x%30 == 0:
		#	y = x/30
		#pygame.draw.rect(screen, BLACK, [0, y*50, 50, 50], 2)
		#
		#x+= 1
		game_over = tetris.time_passed()
		if game_over:
			done = True
		else:
			for block in tetris.get_blocks():
				pygame.draw.rect(screen, block.color,
					             [block.x, block.y, tetrisboard.BLOCK_WIDTH, tetrisboard.BLOCK_HEIGHT], 0)

		# --- Go ahead and update the screen with what we've drawn.
		pygame.display.flip()
	 
		# --- Limit to 60 frames per second
		clock.tick(60)
	 
	# Close the window and quit.
	pygame.quit()




if __name__ =='__main__':
	main()
