import unittest


class TestStringMethod(unittest.TestCase):

    def test_hoge(self):
        self.assertEqual('foo'.upper(), 'FOO')

if __name__ == '__main__':
    unittest.main()