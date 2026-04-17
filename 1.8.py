import math 

a = 15
b = 20
c = 30
kerület = a+b+c
s = (a+b+c)/2
terület = math.sqrt(s * (s-a) * (s-b) * (s-c)) 

print(terület)
print(kerület)