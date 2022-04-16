''' coverage run -m unittest discover -s src/tests/ -v'''
# Testing
import unittest

# Modules
from src.data_structures import Grid


class GridTestCase(unittest.TestCase):

    def setUp(self):
        self.rows = 2
        self.cols = 2
        self.grid = Grid(self.rows, self.cols, '-')
        self.new_item = 'X'

    def test_grid_shape(self):
        '''
        Test that the Grid instance has a height equal to the number of specified rows,
        and a width equal to the number of specified columns.
        '''
        rows = 5
        cols = 9
        fill_value = '-'
        grid = Grid(rows, cols, fill_value)

        self.assertEqual(grid.get_height(), rows)
        self.assertEqual(grid.get_width(), cols)

    def test_get_and_set_item(self):
        ''' Test the set and get methods '''
        row, col = 1, 1
        self.grid.__setitem__(row, col, self.new_item)
        self.assertEqual(self.grid.__getitem__(row, col), self.new_item)

        with self.assertRaises(IndexError):
            self.grid.__setitem__(self.rows+1, self.cols+1, self.new_item)

    def test_string_method(self):
        ''' Test the string method could print array items '''
        grid = Grid(2, 2, '-')
        self.assertEqual(str(grid), '--\n--\n')