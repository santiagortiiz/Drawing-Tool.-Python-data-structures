''' coverage run -m unittest discover -s src/tests/ -v'''
# Testing
import unittest

# Modules
from src.data_structures import Array


class ArrayTestCase(unittest.TestCase):

    def setUp(self):
        self.capacity = 3
        self.array = Array(self.capacity, '-')
        self.new_item = 'X'

    def test_array_capacity(self):
        ''' Test that an array is created with the specified capacity '''
        array = Array(self.capacity)
        self.assertEqual(len(array), self.capacity)

        with self.assertRaises(IndexError):
            self.array[self.capacity + 1]

    def test_get_and_set_item(self):
        ''' Test the set and get methods '''
        self.array[1] = self.new_item
        self.assertEqual(self.array[1], self.new_item)

    def test_string_method(self):
        ''' Test the string method could print array items '''
        fill_value = 'o'
        array = Array(1, fill_value)
        self.assertEqual(str(array), "['o']")

    def test_iter_method(self):
        '''
        Test that the iter method of the array,
        returns an object of "list_iterator" type.
        '''
        from _collections_abc import list_iterator
        self.assertIsInstance(self.array.__iter__(), list_iterator)






