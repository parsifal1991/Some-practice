import math

h = 1.5
atmero = int(input("Adja meg a medence meretet (diameter):"))
r = atmero / 2

V = math.pi * pow(r, 2) * h
V_kerekitett = math.ceil(V)  # Mindig felfelé kerekít

print(f" A medence vizterfogata {V_kerekitett} kobmeter.")