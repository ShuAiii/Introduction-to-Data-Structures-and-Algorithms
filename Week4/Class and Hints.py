import math

def areachoice():
    choice = input("choose a shape(square,triangle,circle): ")
    if choice == "square":
        side = input("Enter side: ")
        side = float(side)
        area = squarearea(side)
    elif choice == "triangle":
        base = input("enter base: ")
        base = float(base)
        height = input("enter height:")
        height = float(height)
        area = areatriangle(base,height)
    else:
        radius = input("enter radius: ")
        radius = float(radius)
        area = circlearea(radius)   
    return area

def squarearea(side):
    area = side * side
    return area

def areatriangle(base, height):
    area = 0.5 * base * height
    return area

def circlearea(radius):
    area = math.pi * radius**2
    return area

""" HINTS """

# Q1

def choice():
    input choose area or perimeter
    call area() or perimeter()
    
    SQUARE
    
def area():
    
def perimeter():
    

# Q2
def choice():
    input choose +, - , * or /
    take in x and y
    call plus(x,y), minus(x,y), multiply(x,y) or divide(x,y)
    
    return answer
    
def plus(x,y):
    
def minus(x,y):

def multiply(x,y):
    
def divide(x,y):

# Q 3
    
def volumechoice():
    choice = input("choose (cube, cone, cylinder or sphere): ")
    if choice == "cube":
        side = input("???")
        volume = cube(?)

    elif choice == "cone":
        base = input("????")
        volume = cone(?)
        
    elif choice == "cylinder":
        ????
        ?????
    else:
        radius = input("???")
        volume = sphere(?)
    return ????

def cube(?):
    volume = ??
    return volume

??????