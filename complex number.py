import cmath
comp = complex(input())
a = comp.real
b = comp.imag
print(abs(complex(a, b)))
print(cmath.phase(complex(a, b)))