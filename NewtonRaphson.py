print("---Newton-Raphson Method---\n")

def calculateEq(l, x):
    res = 0
    degree = len(l) - 1
    for i in l:
        res += pow(x, degree) * i
        degree -= 1
    return res

def newtonRaphson(l, k, x):
    return x - (calculateEq(l, x) / calculateEq(k, x))

coefficients = [float(input("Enter the coefficient of the %d. degree of the equation(x^%d): " % (i, i))) for i in range(int(input("Enter the max degree: ")), -1, -1)]
print()
derCoefficients = [float(input("Enter the coefficient of the %d. degree of the derivation of the equations(x^%d): " % (i, i))) for i in range(int(input("Enter the max degree of derivation of the equation: ")), -1, -1)]

tmp_x = float(input("\nEnter the starting value(x0): "))
tolerance = float(input("Tolerance(Epsilon): "))

resK = [tmp_x]
resL = [newtonRaphson(coefficients, derCoefficients, tmp_x)]

print("\n%10s| %10s" % ("Xk", "Xk + 1"))
print("%10s| %10s|" % ("---------", "---------"))

print("%10.5f| %10.5f|" % (resK[-1], resL[-1]))

while abs(resK[-1] - resL[-1]) > tolerance:
    resK.append(resL[-1])
    resL.append(newtonRaphson(coefficients, derCoefficients, resK[-1]))
    print("%10.5f| %10.5f|" % (resK[-1], resL[-1]))

print("\nx_root: %f" % resL[-1])
