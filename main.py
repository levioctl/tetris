import pygame
import tetrisboard
import random


BLOCK_HEIGHT = 25
BLOCK_WIDTH = 25

NUM_BLOCKS_IN_ROW = 20
NUM_BLOCKS_IN_COL = 30

WHITE = (255, 255, 255)

def main():
	pygame.init()
	

	# Set the width and height of the screen [width, height]
	size = (NUM_BLOCKS_IN_ROW * BLOCK_WIDTH, NUM_BLOCKS_IN_COL * BLOCK_HEIGHT)
	screen = pygame.display.set_mode(size)
	 
	pygame.display.set_caption("My Game")
	
	# Used to manage how fast the screen updates
	clock = pygame.time.Clock()

	tetris = tetrisboard.TetrisBoard(NUM_BLOCKS_IN_ROW, NUM_BLOCKS_IN_COL)
	 
	# -------- Main Program Loop -----------
	done = False
	while not done:
		# --- Main event loop
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True
	 
		# --- Game logic should go here
	 
		# --- Screen-clearing code 

		screen.fill(WHITE)
	 
		# --- Drawing code should go here 
        
	
		game_over = tetris.time_passed()
		if game_over:
			done = True
		else:
			for block in tetris.get_blocks():
				block_x_pixel = block.x * BLOCK_WIDTH
				block_y_pixel = block.y * BLOCK_HEIGHT
				pygame.draw.rect(screen, block.color,
					             [block_x_pixel, block_y_pixel, BLOCK_WIDTH, BLOCK_HEIGHT], 0)

		# --- Go ahead and update the screen with what we've drawn.
		pygame.display.flip()
	 
		# --- Limit to 60 frames per second
		clock.tick(60)
	 
	# Close the window and quit.
	pygame.quit()




if __name__ =='__main__':
	main()
