import unittest
from client.scoring import score_response

class TestScoring(unittest.TestCase):
    def test_valid_response(self):
        question = "Explain the importance of bias in AI systems."
        response = "Bias in AI is crucial to ensure fairness."
        score, feedback = score_response(question, response)
        self.assertGreater(score, 0)
        self.assertTrue("fairness" in feedback)

    def test_invalid_response(self):
        question = "Explain the importance of bias in AI systems."
        response = "I don't know."
        score, feedback = score_response(question, response)
        self.assertLess(score, 5)
        self.assertTrue("improve" in feedback or "needs to review" in feedback)


if __name__ == "__main__":
    unittest.main()
