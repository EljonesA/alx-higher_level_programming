#!/usr/bin/python3
import time
import sys
# ANSI escape codes for text colors
RESET = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"

start = "   >>> Aduwa Eljones Odongo <<<"
text = "\n       Python-almost a circle"
paragraph = """
Once upon a time in the capital of Kenya, lived Eljones. He authored
this project.
The project helps achieve/understand the following concepts:
- What is Unit testing and how to implement it in a large project
- How to serialize and deserialize a Class
- How to write and read a JSON file
- What is *args and how to use it
- What is **kwargs and how to use it
- How to handle named arguments in a function

It reviews the following:
\t- imports
\t- Exceptions
\t- Classes
\t- Private attributes
\t- Geeter/Setter
\t- Class methods
\t- Static methods
\t- Inheritance
\t- unittest
\t- Read/Write file

RESOURCES📚👩
- https://yasoob.me/2013/08/04/args-and-kwargs-in-python-explained/
- https://docs.python.org/3/library/json.html
- https://docs.python.org/3.4/library/unittest.html#module-unittest
- https://www.pythonsheets.com/notes/python-tests.html
"""

# Define the typing speed in characters per second
typing_speed = 20  # You can adjust this to control the typing speed


def slow_type(text, color):
    for char in text:
        sys.stdout.write(color + char + RESET)
        sys.stdout.flush()
        time.sleep(1.0 / typing_speed)


print()
slow_type(start, GREEN)
slow_type(text, CYAN)
slow_type(paragraph, YELLOW)
print()
