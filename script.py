from math import *

#input des points
x1 = float(input("Coordonnée x du premier point: "))
y1 = float(input("Coordonnée y du premier point: "))
x2 = float(input("Coordonnée x du deuxième point: "))
y2 = float(input("Coordonnée y du deuxième point: "))

#calcul de a, b et c
a = (y2 - y1) / (x2 - x1)**2
b = ((x1 * y2) - (x2 * y1)) / (x1 - x2)**2
c = y1 - (a * x1**2) - (b * x1)

#print du résultat
if b<0:
	if c<0:
		print(f"La fonction du polynôme de degré 2 est: y={a}x^2{b}x{c}")
	elif c>0:
		print(f"La fonction du polynôme de degré 2 est : y={a}x^2{b}x+{c}")
	elif c==0:
		print(f"La fonction du polynôme de degré 2 est : y={a}x^2{b}x")
elif b>0:
	if c<0:
		print(f"La fonction du polynôme de degré 2 est: y={a}x^2+{b}x{c}")
	elif c>0:
		print(f"La fonction du polynôme de degré 2 est : y={a}x^2+{b}x+{c}")
	elif c==0:
		print(f"La fonction du polynôme de degré 2 est : y={a}x^2+{b}x")
elif b==0:
	if c<0:
		print(f"La fonction du polynôme de degré 2 est: y={a}x^2{c}")
	elif c>0:
		print(f"La fonction du polynôme de degré 2 est : y={a}x^2+{c}")
	elif c==0:
		print(f"La fonction du polynôme de degré 2 est : y={a}x^2")
