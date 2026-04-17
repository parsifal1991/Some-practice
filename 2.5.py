
import math

r = float(input())

terület = round(math.pi,5) * pow(r,2)
kerület = 2 * round(math.pi,5) * r

print(f"{kerület}\n{terület}")