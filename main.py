import pygame
import tetrisboard
import random


BLOCK_HEIGHT = 50
BLOCK_WIDTH = 50

#NUM_BLOCKS_IN_ROW = 10
#NUM_BLOCKS_IN_COL = 15

NUM_BLOCKS_IN_ROW = 4
NUM_BLOCKS_IN_COL = 4

WHITE = (255, 255, 255)



def choose_difficulty():
	"""Ask the user for difficulty level of the game and return the matching start speed"""
	print 'Please choose the difficulty level of the game' 
	print 'Press 1 for easy'
	print 'Press 2 for hard'

	difficulty = raw_input()

	while difficulty not in ('1', '2'):
		print 'please type either 1 or 2'
		difficulty = raw_input()

	if difficulty == 1:
		start_speed = 1
	else:
		start_speed = 4 

	return start_speed





def main():

 	start_speed = choose_difficulty()
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
        
	
		tetris.pass_one_time_unit()
		if tetris.is_game_over():
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
		clock.tick(start_speed)
	 
	# Close the window and quit.
	pygame.quit()




if __name__ =='__main__':
	main()
