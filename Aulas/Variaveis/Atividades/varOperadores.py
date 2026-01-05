# Questão 1
x = int(input())
y = int(input())
z = int(input())

resultado1 = (x < y and y > z) or (x + y == z and not (z == x * 3))

print(resultado1)

# Questão 2
a = int(input())
b = int(input())
c = int(input())
d = int(input())

resultado2 = ((a * b) + (c / d)) - (a ** b)

print(resultado2)
