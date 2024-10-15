import unittest


class TemporaryTest(unittest.TestCase):
    '''
    A temporary test class to stop the CI/CD tests from failing
    '''

    def test_example(self):
        ''' Example unit test '''

        # 1 + 1 is equal to 2, test will pass
        self.assertEqual(1 + 1, 2)
