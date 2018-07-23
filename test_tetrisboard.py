import mock
import unittest
import tetrisboard


def fake_random_choice(elements):
    return 0


class Test(unittest.TestCase):
    def test_create_new_block(self):
        board = tetrisboard.TetrisBoard(4, 4)
        board.pass_one_time_unit()
        blocks = board.get_blocks()
        assert len(blocks) == 1


    def test_new_block_is_on_first_row(self):
        board = tetrisboard.TetrisBoard(4, 4)
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


    def test_is_game_over_when_game_is_not_over(self):
        board = tetrisboard.TetrisBoard(4, 4)
        for i in range(4):
            board.pass_one_time_unit()
        assert not board.is_game_over() 

    @mock.patch("tetrisboard.random.choice", fake_random_choice)
    def test_is_game_over_when_game_is_over(self):
        board = tetrisboard.TetrisBoard(2, 2)
        color = (100,100,100)
        
        board.pass_one_time_unit()
        board.pass_one_time_unit()
        assert not board.is_game_over()
        board.pass_one_time_unit()
        assert board.is_game_over()


if __name__ == "__main__":
    unittest.main()
