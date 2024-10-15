"""Temporary uniting testing module that the deployment workflow can find."""
import unittest


class TemporaryTest(unittest.TestCase):
    """Temporary uniting class that the deployment workflow can find."""

    def test_example(self):

        # 1 + 1 is equal to 2, test will pass
        self.assertEqual(1 + 1, 2)
