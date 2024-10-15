"""
A failing unit test to ensure CI/CD pipeline is testing before deployment
"""
import unittest


class TestCI_CD(unittest.TestCase):
    """ Test class for CI/CD pipeline """

    def test_fail(self):
        """ Failing test """

        # 1 does not equal 2
        self.assertEqual(1, 2)
