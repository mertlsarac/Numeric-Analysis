print("---Jacobi Method---\n")

def calculateEq(l, x):
    res = 0
    degree = len(l) - 1
    for i in l:
        res += pow(x, degree) * i
        degree -= 1
    return res

coefficients = [float(input("Enter the coefficient of the %d. degree of the equation(x^%d): " % (i, i))) for i in range(int(input("Enter the max degree: ")), -1, -1)]

print("\nEnter the ranges: ")
a = float(input("a: "))
b = float(input("b: "))
c = (a + b) / 2

tolerance = float(input("Tolerance(Epsilon): "))

print("\n%10s| %10s| %10s| %10s| %10s| %10s|" % ("a", "f(a)", "b", "f(b)", "c", "f(c)"))
print("%10s| %10s| %10s| %10s| %10s| %10s|" % ("---------", "---------", "---------", "---------", "---------", "---------"))

resA = [calculateEq(coefficients, a)]
resB = [calculateEq(coefficients, b)]
resC = [calculateEq(coefficients, c)]

print("%10.8f| %10.8f| %10.8f| %10.8f| %10.8s| %10.8f|" % (a, resA[-1], b, resB[-1], c, resC[-1]))

while abs(resC[-1]) > tolerance:
    if resC[-1] * resB[-1] >= 0:
        b = c
    else:
        a = c
    c = (a + b) / 2
    resA.append(calculateEq(coefficients, a))
    resB.append(calculateEq(coefficients, b))
    resC.append(calculateEq(coefficients, c))
    print("%10.8f| %10.8f| %10.8f| %10.8f| %10.8s| %10.8f|" % (a, resA[-1], b, resB[-1], c, resC[-1]))

print("\nx_root: %f" % c)
