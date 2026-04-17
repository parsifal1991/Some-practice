import math

radius = float(input(" Give me the radius of the circle: "))

circumference = 2 * math.pi * radius

area = math.pi * pow(radius,2)

print(f" the circumference:{round(circumference,2)}cm ")

print(f" The area:{round(area,2)}cm^2")