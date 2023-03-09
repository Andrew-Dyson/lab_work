import unittest

from src.high_scores import latest, personal_best, personal_top_three

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

    # Test top three when there is a tie

    # Test top three when there are less than three

    # Test top three when there is only one
    
