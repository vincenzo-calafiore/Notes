a = 12
b = 3

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a // b) #integer division rounded down minus infinity
print(a % b) #modulo: the reminder after integer division

print()

i=1
print(i)
i=2
print(i)
i=3
print(i)

print()

for i in range(1, a // b):
    print(i)
    
print()

print(a + b / 3 - 4 * 12)
print(a + (b/3) - (4*12))
print((((a+b)/3)-4)*12)
print(((a+b)/3-4)*12)

print()

c= a+b
d = c/3
e = d - 4
print(e*12)

# Operators Presedence Acronyms
#   PEMDAS = Parentheses , Exponents, Multiplication, Division, Addition, Subtractions
#   BEDMAS = Brackets, Exponents, Division, Multiplication, Addition, Subtractions
#   BODMAS = Brackets, Order, Division, Multiplication, Addition, Subtractions
#   BIDMAS = Brackets, Index, Division, Multiplication, Addition, Subtractions

print()

print(a / (b * a) / b)