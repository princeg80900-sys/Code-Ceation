from shapegr import *
shape = int(input("""Please choose the shape you want to calculate area
              1. Circle
              2. Square
              3. Rectangle
              4. Triangle 
              Put you choice here: """))

print(f"The area of the {shape} is: {calculate_area(shape)}")
