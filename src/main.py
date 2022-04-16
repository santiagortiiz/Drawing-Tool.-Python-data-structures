# Data Structures
from  data_structures import Canvas


if __name__ == '__main__':

    canvas = None

    with open('output.txt', 'w') as output_file:

        with open('input.txt', 'r') as input_file:
            for line in input_file.readlines():

                command = line.replace('\n', '').split(' ')
                command = list(map(lambda i: int(i) if i.isnumeric() else i, command))

                if command[0] == 'C':
                    _, w, h = command
                    canvas = Canvas(w, h)
                    output_file.write(str(canvas))

                elif command[0] == 'L' and canvas is not None:
                    _, x1, y1, x2, y2 = command
                    row1, col1, row2, col2 = y1, x1, y2, x2
                    canvas.create_line(row1, col1, row2, col2)
                    output_file.write(str(canvas))

                elif command[0] == 'R' and canvas is not None:
                    _, x1, y1, x2, y2 = command
                    row1, col1, row2, col2 = y1, x1, y2, x2
                    canvas.create_rectangle(row1, col1, row2, col2)
                    output_file.write(str(canvas))

                elif command[0] == 'B' and canvas is not None:
                    _, x, y, color= command
                    row, col, = y, x
                    canvas.bucket_fill(row, col, color)
                    output_file.write(str(canvas))