#!/usr/bin/python3
import unittest
import pep8


class TestConsole(unittest.TestCase):
    """Test cases for the console

    Args:
        unittest ([type]): [description]
    """

    def test_pep8(self):
        """pep8
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    if __name__ == '__main__':
        unittest.main()
