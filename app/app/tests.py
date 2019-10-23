from django.test import TestCase
from app.addition import add_numbers
from app.addition import subtract_numbers


class Addition_tests(TestCase):
    def test_add_numbers(self):
        """test the result of addition of two numbers"""
        self.assertEqual(add_numbers(2, 3), 5)

    def test_substract_numbers(self):
        """test the result of substraction of two numbers"""
        self.assertEqual(subtract_numbers(5, 3), 2)
