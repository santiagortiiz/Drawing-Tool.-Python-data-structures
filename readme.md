# Drawing Tool

In a nutshell, the program reads the
input.txt , executes a set of commands from the file, step by step, and produces output.txt

At this time, the functionality of the program is quite limited but this might change in the future.
At the moment, the program should support the following set of commands:


| Command | Name | Description |
| ----------- | ----------- | ----------- |
| C w h | Create Canvas | Should create a new canvas of width w and height h. |
| L x1 y1 x2 y2 | Create Line | Should create a new line from (x1,y1) to (x2,y2). Currently only horizontal or vertical lines are supported. Horizontal and vertical lines will be drawn using the 'x' character. |
| R x1 y1 x2 y2 | Create Rectangle | Should create a new rectangle, whose upper left corner is (x1,y1) and lower right corner is (x2,y2). Horizontal and vertical lines will be drawn using the 'x' character. |
| B x y c | Bucket Fill | Should fill the entire area connected to (x,y) with "colour" c. The behaviour of this is the same as that of the "bucket fill" tool in paint programs. |

Note: You can draw only draw if a canvas has been created.


# Example
Look at ***input.txt*** and ***output.txt***


# Windows setup
Create virtual environment
- py -m venv .venv
- pip install -r requirements.txt

# Testing
Run tests:
- coverage run -m unittest discover -s src/tests/ -v

Show coverage:
- coverage report -m

| Name | Stmts | Miss | Cover | Missing |
| ----------- | ----------- | ----------- | ----------- | ----------- |
| src\__init__.py                     |    0 | 0 | 100% |     |
| src\data_structures\__init__.py     |    3 | 0 | 100% |     |
| src\data_structures\array.py        |   15 | 0 | 100% |     |
| src\data_structures\canvas.py       |   74 | 0 | 100% |     |
| src\data_structures\exceptions.py   |    2 | 0 | 100% |     |
| src\data_structures\grid.py         |   21 | 0 | 100% |     |
| src\tests\test_array.py             |   22 | 0 | 100% |     |
| src\tests\test_canvas.py            |  177 | 0 | 100% |     |
| src\tests\test_grid.py              |   24 | 0 | 100% |     |
TOTAL    | 338   |  0  |   100%

# Run
py src/main.py