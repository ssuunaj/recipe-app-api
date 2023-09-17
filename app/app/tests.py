"""Sample Tests"""

from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """Test the calc module"""

    def test_add_numbers(self):
        """Test adding numbers together"""
        result = calc.add(5, 6)

        self.assertEqual(result, 11)

    def test_sub_numbers(self):
        """Test substracting numbers """

        result = calc.substract(10, 15)

        self.assertEqual(result, 5)
