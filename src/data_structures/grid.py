# Data Structures
from .array import Array


class Grid():

    def __init__(self, rows, columns, fill_value=None):
        # Defines the rows of the array
        self.data = Array(rows)

        # Defines the columns of the array and set their default values
        for row in range(rows):
            self.data[row] = Array(columns, fill_value=fill_value)

    def get_height(self):
        return len(self.data)

    def get_width(self):
        return len(self.data[0])

    def __setitem__(self, row, column, value):
        self.data[row][column] = value

    def __getitem__(self, row, column):
        return self.data[row][column]

    def __str__(self):
        string = ""

        for row in range(self.get_height()):
            for col in range(self.get_width()):
                string += str(self.data[row][col])

            string += "\n"

        return str(string)