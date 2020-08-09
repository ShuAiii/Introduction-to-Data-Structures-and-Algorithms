#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 12:16:57 2020

@author: Kevin
"""

# TEXT in this colour are comments! No effect on the code!


X = 5.0 # number , float (number, stores a certain amount of digits 0.934829)
Y = 2.0 # number

Z = 'Jason'  # String ( Think of it as a string of letters, must be put in qoutes!)


"""
Variable Types!
"""

TypeX = type(X) # checking the variable type of the variable X!
TypeY = type(Y)
TypeZ = type(Z) # str is short for String


"""
Print things!
"""

print("X is equal to: ", X)

"""
Inpunt things!
"""

R = input("Enter a number: ") # storing an input number in varible R
# Input will take numbers, and convert to String!

"""
Casting! Convert variable types
"""

CastX = str(X)  # converting X to a String
BackX = float(CastX) # converting CastX back to a float