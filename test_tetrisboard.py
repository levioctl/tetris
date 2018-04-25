import unittest
import tetrisboard


class Test(unittest.TestCase):
    def test_create_new_block(self):
        board = tetrisboard.TetrisBoard(4, 4)
        board.pass_one_time_unit()
        blocks = board.get_blocks()
        assert len(blocks) == 1


    def test_new_block_is_on_first_row(self):
        board = tetrisboard.TetrisBoard(4, 4)
        board.pass_one_time_unit()
        blocks = board.get_blocks()
        print blocks[0].y
        assert blocks[0].y == 0


    def test_block_falling(self):
        board = tetrisboard.TetrisBoard(4, 4)
        board.pass_one_time_unit()
        blocks = board.get_blocks()
        initial_row = blocks[0].y
        board.pass_one_time_unit()
        blocks = board.get_blocks()
        assert blocks[0].y == initial_row + 1


if __name__ == "__main__":
    unittest.main()
