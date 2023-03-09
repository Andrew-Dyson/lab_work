import unittest

from src.high_scores import latest, personal_best, personal_top_three, high_to_low

# Tests adapted from `problem-specifications//canonical-data.json` @ v4.0.0


class HighScoresTest(unittest.TestCase):
    def setUp(self):
        self.scores = [13, 400, 25, 346, 10000]
    # Tests

    # Test latest score (the last thing in the list)
    def test_latest_score(self):
        self.assertEqual(10000, latest(self.scores))
    # Test personal best (the highest score in the list)
    def test_personal_best(self):
        self.assertEqual(10000, personal_best(self.scores))
    # Test top three from list of scores
    def test_top_three(self):
        self.assertEqual([10000, 400, 346], personal_top_three(self.scores))
        
    # Test ordered from highest to lowest
    def test_ordered_from_highest_to_lowest(self):
        self.scores = [10, 12, 11]
        self.assertEqual([12, 11, 10], high_to_low(self.scores))
    # Test top three when there is a tie
    def test_top_three_scores_when_tie_exists(self):
        self.scores = [10, 10, 10, 10, 2, 6]
        self.scores = personal_top_three(self.scores)
        self.assertEqual([10, 10, 10], self.scores)
    # Test top three when there are less than three
    def test_top_three_if_less_than_three_scores(self):
        self.scores = [10, 6]
        self.scores = personal_top_three(self.scores)
        self.assertEqual([10, 6], self.scores)        
    # Test top three when there is only one
    def test_top_three_if_only_one_scores(self):
        self.scores = [10]
        self.scores = personal_top_three(self.scores)
        self.assertEqual([10], self.scores)     
