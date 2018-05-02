print("---Secant Method---\n")

def calculateEq(l, x):
    res = 0
    degree = len(l) - 1
    for i in l:
        res += pow(x, degree) * i
        degree -= 1
    return res

def secant(l, x0, xk):
    y0 = calculateEq(l, x0)
    yk = calculateEq(l, xk)
    return x0 - (xk - x0) / (yk - y0) * y0

coefficients = [float(input("Enter the coefficient of the %d. degree of the equation(x^%d): " % (i, i))) for i in range(int(input("Enter the max degree: ")), -1, -1)]

print("\nEnter the ranges: ")
a = float(input("a: "))
b = float(input("b: "))
c = (a + b) / 2

tolerance = float(input("Tolerance(Epsilon): "))

print("\n%10s| %10s| %10s| %10s| %10s| %10s|" % ("x0", "yo", "x1", "y1", "x2", "y2"))
print("%10s| %10s| %10s| %10s| %10s| %10s|" % ("---------", "---------", "---------", "---------", "---------", "---------"))

x0 = a
x1 = b
x2 = secant(coefficients, a, b)

y0 = calculateEq(coefficients, x0)
y1 = calculateEq(coefficients, x1)
y2 = calculateEq(coefficients, x2)

print("%10.6f| %10.6f| %10.6f| %10.6f| %10.6f| %10.6f|" % (x0, y0, x1, y1, x2, y2))

while abs(y2) > tolerance:
    if y2 * y0 > 0:
        x0 = x2
    else:
        x1 = x2
    y0 = calculateEq(coefficients, x0)
    y1 = calculateEq(coefficients, x1)
    x2 = secant(coefficients, x0, x1)
    y2 = calculateEq(coefficients, x2)
    print("%10.6f| %10.6f| %10.6f| %10.6f| %10.6f| %10.6f|" % (x0, y0, x1, y1, x2, y2))

print("\nx_root: %f" % y2)
