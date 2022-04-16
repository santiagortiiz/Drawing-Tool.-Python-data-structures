''' coverage run -m unittest discover -s src/tests/ -v'''
# Testing
import unittest

# Modules
from src.data_structures import Canvas

# Exceptions
from src.data_structures.exceptions import OnlyStraightLinesAllowed


class CanvasTestCase(unittest.TestCase):

    def setUp(self):
        self.width = 3
        self.height = 3
        self.canvas = Canvas(self.width, self.height)

    def test_string_method(self):
        ''' Test the string method could print the Canvas '''
        canvas = Canvas(2, 2, 'X')
        self.assertEqual(str(canvas), '----\n|XX|\n|XX|\n----\n')

    def test_borders(self):
        ''' Validates the borders of the canvas are drawn correctly '''
        last_row = self.height + 1
        last_col = self.width + 1
        horizontal_edge = '-'
        vertical_edge = '|'

        for row in range(1, self.height):
            value = self.canvas.__getitem__(row, 0)
            self.assertEqual(value, vertical_edge)

            value = self.canvas.__getitem__(row, last_col)
            self.assertEqual(value, vertical_edge)

        for col in range(0, self.width+1):
            value = self.canvas.__getitem__(0, col)
            self.assertEqual(value, horizontal_edge)

            value = self.canvas.__getitem__(last_row, col)
            self.assertEqual(value, horizontal_edge)

    def test_get_and_set_item(self):
        ''' Test the set and get methods '''
        row, col = 1, 1
        new_item = 'x'
        self.canvas.__setitem__(row, col, new_item)
        self.assertEqual(self.canvas.__getitem__(row, col), new_item)

        # Test set and get out of the canvas
        offset = 2
        with self.assertRaises(IndexError):
            self.canvas.__setitem__(self.height+offset, self.width+offset, new_item)
        with self.assertRaises(IndexError):
            self.canvas.__getitem__(self.height+offset, self.width+offset)

    def test_creating_horizontal_line(self):
        ''' Drawing horizontal line in the first row '''
        first_row = 1
        row1, col1 = first_row, 1
        row2, col2 = first_row, self.width
        mark = 'x'
        self.canvas.create_line(row1, col1, row2, col2, mark)

        for col in range(col1, col2):
            value = self.canvas.__getitem__(first_row, col)
            self.assertEqual(value, mark)

    def test_creating_vertical_line(self):
        ''' Drawing vertical line in the first column '''
        first_col = 1
        first_row, last_row = 1, self.height

        row1, col1 = first_row, first_col
        row2, col2 = last_row, first_col
        mark = 'x'
        self.canvas.create_line(row1, col1, row2, col2, mark)

        for row in range(first_row, last_row):
            value = self.canvas.__getitem__(row, first_col)
            self.assertEqual(value, mark)

    def test_creating_horizontal_lines_longer_than_the_width_of_canvas(self):
        '''
        Validates that the lines longer than the
        width of the canvas does not touch the edges.
        '''
        # Drawing horizontal line in the first row
        first_row = 1
        left_edge = 0
        right_edge = self.width + 1

        row1, col1 = first_row, left_edge
        row2, col2 = first_row, right_edge
        mark = 'x'
        self.canvas.create_line(row1, col1, row2, col2, mark)

        for col in range(left_edge + 1, right_edge - 1):
            value = self.canvas.__getitem__(first_row, col)
            self.assertEqual(value, mark)

        # Validates that the drawn line does not touch the edges
        left_edge_value = self.canvas.__getitem__(first_row, left_edge)
        self.assertNotEqual(left_edge_value, mark)

        right_edge_value = self.canvas.__getitem__(first_row, right_edge)
        self.assertNotEqual(right_edge_value, mark)

    def test_creating_vertical_lines_longer_than_the_height_of_canvas(self):
        '''
        Validates that the lines longer than the
        height of the canvas does not touch the edges.
        '''
        first_col = 1
        lower_edge = 0
        upper_edge = self.height + 1

        row1, col1 = lower_edge, first_col
        row2, col2 = upper_edge, first_col
        mark = 'x'
        self.canvas.create_line(row1, col1, row2, col2, mark)

        # Validates the mark has been set in the points within the canvas
        for row in range(lower_edge + 1, upper_edge - 1):
            value = self.canvas.__getitem__(row, first_col)
            self.assertEqual(value, mark)

        # Validates that the drawn line does not touch the edges
        left_edge_value = self.canvas.__getitem__(lower_edge, first_col)
        self.assertNotEqual(left_edge_value, mark)

        right_edge_value = self.canvas.__getitem__(upper_edge, first_col)
        self.assertNotEqual(right_edge_value, mark)

    def test_drawing_horizontal_lines_with_points_out_of_the_canvas(self):
        '''
        Only points inside the canvas are marked to draw lines with
        specified points out of the canvas.
        '''
        # Horizontal line in the first row with columns out of the canvas
        first_row = 1
        left_edge = 0
        right_edge = self.width + 1

        row1, col1 = first_row, left_edge - 10
        row2, col2 = first_row, right_edge + 10
        mark = 'x'
        self.canvas.create_line(row1, col1, row2, col2, mark)

        for col in range(left_edge + 1, right_edge - 1):
            value = self.canvas.__getitem__(first_row, col)
            self.assertEqual(value, mark)

        # Validates that the drawn line does not touch the edges
        left_edge_value = self.canvas.__getitem__(first_row, left_edge)
        self.assertNotEqual(left_edge_value, mark)

        right_edge_value = self.canvas.__getitem__(first_row, right_edge)
        self.assertNotEqual(right_edge_value, mark)

    def test_drawing_vertical_lines_with_points_out_of_the_canvas(self):
        '''
        Validates that the lines longer than the
        height of the canvas does not touch the edges.
        '''
        first_col = 1
        lower_edge = 0
        upper_edge = self.height + 1

        row1, col1 = lower_edge - 10, first_col
        row2, col2 = upper_edge + 10, first_col
        mark = 'x'
        self.canvas.create_line(row1, col1, row2, col2, mark)

        # Validates the mark has been set in the points within the canvas
        for row in range(lower_edge + 1, upper_edge - 1):
            value = self.canvas.__getitem__(row, first_col)
            self.assertEqual(value, mark)

        # Validates that the drawn line does not touch the edges
        left_edge_value = self.canvas.__getitem__(lower_edge, first_col)
        self.assertNotEqual(left_edge_value, mark)

        right_edge_value = self.canvas.__getitem__(upper_edge, first_col)
        self.assertNotEqual(right_edge_value, mark)

    def test_drawing_lines_from_right_to_left(self):
        ''' Tests that horizonal lines can be drawn in any direction '''
        # Drawing horizontal line in the first row
        first_row = 1
        first_col = 1
        row1, col1 = first_row, self.width
        row2, col2 = first_row, first_col
        mark = 'x'
        self.canvas.create_line(row1, col1, row2, col2, mark)

        # Validates the mark has been set in the points of the line
        for col in range(col2, col1):
            value = self.canvas.__getitem__(first_row, col)
            self.assertEqual(value, mark)

    def test_drawing_lines_from_bottom_to_top(self):
        ''' Tests that vertical lines can be drawn in any direction '''
        # Drawing vertical line in the first col
        first_row = 1
        first_col = 1
        row1, col1 = self.height, first_col
        row2, col2 = first_row, first_col
        mark = 'x'
        self.canvas.create_line(row1, col1, row2, col2, mark)

        # Validates the mark has been set in the points of the line
        for row in range(row2, row1):
            value = self.canvas.__getitem__(row, first_col)
            self.assertEqual(value, mark)

    def test_drawing_curves(self):
        ''' Validates that the canvas does not allow curves '''
        # Testing horizontal line
        first_row = 1
        second_row = first_row + 1

        row1, col1 = first_row, 1
        row2, col2 = second_row, self.width
        mark = 'x'

        with self.assertRaises(OnlyStraightLinesAllowed):
            self.canvas.create_line(row1, col1, row2, col2, mark)

    def test_creating_rectangle_within_the_canvas(self):
        '''
        Tests the creation of a hollow rectangle within the canvas.

        Note: It is not necessary to test the creation of a rectangle from the outside
        because its primitive function is the creation of lines and it has already been tested.
        '''
        row1, col1 = 1, 1
        row2, col2 = self.height, self.width
        mark = 'x'
        self.canvas.create_rectangle(row1, col1, row2, col2, mark)

        # Left edge
        for row in range(row1, row2):
            value = self.canvas.__getitem__(row, col1)
            self.assertEqual(value, mark)

        # Right edge
        for row in range(row1, row2):
            value = self.canvas.__getitem__(row, col2)
            self.assertEqual(value, mark)

        # Upper edge
        for col in range(col1, col2):
            value = self.canvas.__getitem__(row1, col)
            self.assertEqual(value, mark)

        # Lower edge
        for col in range(col1, col2):
            value = self.canvas.__getitem__(row2, col)
            self.assertEqual(value, mark)

        # Check that there are no marks inside the rectangle
        value = self.canvas.__getitem__(row1 + 1, col1 + 1)
        self.assertNotEqual(value, mark)

    def test_bucket_fill(self):
        ''' Test the points that must (and not) be filled when calling bucket_fill function '''
        w, h = 20, 4
        canvas = Canvas(w, h, ' ')
        canvas.create_line(2, 1, 2, 6)
        canvas.create_line(3, 6, 4, 6)
        canvas.create_rectangle(1, 16, 3, 20)

        color = 'o'
        canvas.bucket_fill(3, 10, color)

        self.assertEqual(canvas.__getitem__(1, 1), color)
        self.assertEqual(canvas.__getitem__(4, 20), color)
        self.assertEqual(canvas.__getitem__(3, 10), color)

        self.assertNotEqual(canvas.__getitem__(2, 1), color)
        self.assertNotEqual(canvas.__getitem__(3, 1), color)
        self.assertNotEqual(canvas.__getitem__(1, 19), color)
        self.assertNotEqual(canvas.__getitem__(2, 19), color)