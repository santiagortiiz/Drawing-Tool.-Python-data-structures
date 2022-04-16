# Data Structures
from .grid import Grid

# Errors
from .exceptions import OnlyStraightLinesAllowed


class Canvas:

    def __init__(self, width, height, fill_value=' ', mark='x'):
        self.background = fill_value
        self.mark = mark

        self.height = height
        self.width = width

        self.borders = 2
        self.canvas = Grid(height+self.borders, width+self.borders, fill_value)
        self.__draw_borders()

    def __str__(self):
        return str(self.canvas)

    def __setitem__(self, row, col, value):
        self.canvas.__setitem__(row, col, value)

    def __getitem__(self, row, col):
        return self.canvas.__getitem__(row, col)

    def __draw_borders(self):
        ''' Draws the borders of the Canvas with horizontal and vertical lines '''
        last_row = self.height + 1
        last_col = self.width + 1

        # Draw horizontal lines
        horizontal_edge = '-'
        self.__draw_horizontal_line(0, 0, 0, last_col, horizontal_edge)
        self.__draw_horizontal_line(last_row, 0, last_row, last_col, horizontal_edge)

        # Draw vertical lines
        vertical_edge = '|'
        self.__draw_vertical_line(1, 0, self.height, 0, vertical_edge)
        self.__draw_vertical_line(1, last_col, self.height, last_col, vertical_edge)

    def __draw_horizontal_line(self, row1, col1, row2, col2, value):
        ''' Iterate over the columns setting the specified value '''
        for col in range(col1, col2+1):
            self.canvas.__setitem__(row1, col, value)

    def __draw_vertical_line(self, row1, col1, row2, col2, value):
        ''' Iterate over the rows setting the specified value '''
        for row in range(row1, row2+1):
            self.canvas.__setitem__(row, col1, value)

    def create_line(self, row1, col1, row2, col2, value=None):
        '''
        Should create a new line from (row1,col1) to (row2,col2).
        Currently only horizontal or vertical lines are supported.
        '''
        value = value or self.mark

        # Horizontal condition
        if row1==row2:

            # Validates vertical limits
            if self.height >= row1 > 0:

                # Sorting the columns to allow drawing in two directions
                if col1 > col2:
                    col2, col1 = col1, col2

                # If the col1 is less than or equal to 0, is setted to the minimum value
                if col1 <= 0:
                    col1 = 1

                # Set col2 to the canvas width if it exceeds horizontal limits
                if col2 > self.width:
                    col2 = self.width

                self.__draw_horizontal_line(row1, col1, row2, col2, value)

        # Vertical condition
        elif col1==col2:

            # Validates horizontal limits
            if self.width >= col1 > 0:

                # Sorting the rows to allow drawing in two directions
                if row1 > row2:
                    row2, row1 = row1, row2

                # If the row1 is less than or equal to 0, is setted to the minimum value
                if row1 <= 0:
                    row1 = 1

                # Set row2 to the canvas width if it exceeds vertical limits
                if row2 > self.height:
                    row2 = self.height

                self.__draw_vertical_line(row1, col1, row2, col2, value)

        else:
            raise OnlyStraightLinesAllowed

    def create_rectangle(self, row1, col1, row2, col2, value=None):
        '''
        Should create a new rectangle, whose upper left corner is (row1,col1)
        and lower right corner is (row2,col2).
        '''
        value = value or self.mark

        # Draw horizontal lines
        self.create_line(row1, col1, row1, col2, value)
        self.create_line(row2, col1, row2, col2, value)

        # Draw vertical lines
        self.create_line(row1, col1, row2, col1, value)
        self.create_line(row1, col2, row2, col2, value)

    def bucket_fill(self, row, col, color):
        '''
        Should fill the entire area connected to (row, col) with the specified "colour".
        The behaviour of this is the same as that of the "bucket fill" tool in paint programs.
        '''

        # Return if current position is already filled
        current = self.canvas.__getitem__(row, col)
        if current == self.mark:
            return
        # Set the current position to the new value if it is free
        elif current == self.background:
            self.canvas.__setitem__(row, col, color)
        else:
            return

        if row + 1 <= self.height:
            self.bucket_fill(row+1, col, color)
        if row - 1 > 0:
            self.bucket_fill(row-1, col, color)

        if col + 1 <= self.width:
            self.bucket_fill(row, col+1, color)
        if col - 1 > 0:
            self.bucket_fill(row, col-1, color)