import unittest
from game import Coin, flip_coin, bet, play_betting_bame

class TestGame(unittest.TestCase):
    def test_coin(self):
        self.assertIn(flip_coin(), [Coin.HEADS.value, Coin.TAILS.value])
    
    def test_bet(self):
        amount = 500
        self.assertIn(bet(amount), [0,amount*2])
    
    def test_game(self):
        
        mock_aborted_game = {
            "attempts": 0,
            "successful_attempts": 0,
            "unsuccessful_attempts": 0,
            "win_average": 0,
            "loss_average": 0,
            "max_cash": 0
        }

        no_initial_cash_result = play_betting_bame(0, 100)
        not_enough_initial_cash_result = play_betting_bame(50, 100)
        standard_result = play_betting_bame(100, 100)

        standard_attempts = standard_result["attempts"]

        self.assertDictEqual(not_enough_initial_cash_result, mock_aborted_game)
        self.assertDictEqual(no_initial_cash_result, mock_aborted_game)
        self.assertGreaterEqual(standard_attempts, 1)

if __name__ == '__main__':
    unittest.main()