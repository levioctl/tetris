"""Tetris logic"""

import random 

class Block():
	"""docstring for Rec"""
	def __init__(self, x, y, color):
		self.x = x
		self.y = y
		self.color = color


class TetrisBoard:

	def __init__(self, num_blocks_in_row, num_blocks_in_col):
		self.static_blocks = []
		self._falling_block = None 
		self._num_blocks_in_row = num_blocks_in_row
		self._num_blocks_in_col = num_blocks_in_col 

	def pass_one_time_unit(self):
		"""Retrun True if game is over. Else return False."""
		if self._falling_block is None:

			self._falling_block = self._generate_block()
			game_over = self._falling_block is None
			if game_over:
				return True
			self._remove_full_rows()
		else:
			block_can_keep_falling = self._move_falling_block()
			if not block_can_keep_falling:
				self.static_blocks.append(self._falling_block)
				self._falling_block = None

		
		return False

	def get_blocks(self):
		"""return None if game is over , else returns the blocks on the board"""
		if self._falling_block is None:
			return self.static_blocks 		
		return self.static_blocks + [self._falling_block]

	def _get_blocks_in_row(self, row):
		return [block for block in self.static_blocks if block.y == row]

	def _generate_block(self):
		x_values_of_top_row = [block_index for block_index in xrange(self._num_blocks_in_row)]
		x_values_of_top_row_with_blocks = [block.x for block in self.static_blocks if block.y == 0]
		available_for_new_block = [x for x in x_values_of_top_row if not x in x_values_of_top_row_with_blocks]
		if available_for_new_block:
			x = random.choice(available_for_new_block)
			green = random.randint(0,255)
			red = random.randint(0,255)
			blue = random.randint(0,255)
			color = (red, green, blue)
			return Block(x, 0, color)
		# Game over
		return None



	def does_block_intersect_with_another_block(self, block):
		overlapping = [other_block for other_block in self.static_blocks if
		               other_block.x == block.x and other_block.y == block.y]
		return any(overlapping)


	def _move_falling_block(self):
		
		are_there_block_under_this_block = any([block for block in self.static_blocks if 
								self._falling_block.x == block.x and self._falling_block.y + 1 == block.y])

		has_block_reached_the_floor =  self._falling_block.y == self._num_blocks_in_col - 1


		block_cant_keep_falling = are_there_block_under_this_block or has_block_reached_the_floor 
		
		if  block_cant_keep_falling:
			return False
		else:
			self._falling_block.y += 1
			return True 

	def _remove_full_rows(self):
		full_rows = [row for row in xrange(self._num_blocks_in_col)
		             if len(self._get_blocks_in_row(row)) == self._num_blocks_in_row]
		for row in full_rows:
			row_blocks = self._get_blocks_in_row(row)
			self.static_blocks = [block for block in self.static_blocks if block not in row_blocks]
			higher_blocks = [block for block in self.static_blocks if block.y < row]
			for block in higher_blocks:
				block.y += 1