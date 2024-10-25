# -*- coding: utf-8 -*-
"""Understanding flow control .ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1pZMQMunGudHFSO9xj2UFztPwmDx32jOs

# What is Flow control?

=> Flow control in Python refers to how the program decides what actions to take and in what order. It allows the program to make decisions, repeat tasks, or branch into different paths based on conditions.

Here are the main types of flow control:

1. Conditional Statements (if, elif, else): These let the program make decisions based on conditions.

Example:
"""

x = 10
if x > 5:
    print("x is greater than 5")
else:
    print("x is 5 or less")

"""**Loops** (for, while): These allow the program to repeat actions.

Example:
"""

for i in range(3):
    print(i)  # prints 0, 1, 2

"""**Break and Continue:** Used to control the loop further. break stops the loop, and continue skips to the next iteration.

Example:
"""

for i in range(5):
    if i == 3:
        break  # loop stops at 3
    print(i)