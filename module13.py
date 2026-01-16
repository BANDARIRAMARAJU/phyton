""" Working with random module:
This module defines several functions to generate random numbers.
We can use these functions while developing games,in cryptography and to generate
random numbers on fly for authentication.
1. random() function:
This function always generate some float value between 0 and 1 ( not inclusive)
0<x<1"""


from random import *
for i in range(10):
    print(random())