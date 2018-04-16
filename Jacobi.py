print("---Jacobi Method---\n")

def calculateEq(x2, x1, x0, x, degreeOfH):
    return pow(x2 * x * x + x1 * x + x0, degreeOfH)

#inputs
print("G(x) = x was assigned.")
gX = 1
print("Enter the h(x):")
hX1 = float(input("Enter the coefficient of the first degree of the equation(x'1): "))
hX0 = float(input("Enter the constant number of the equation(x^0): "))
degreeOfH = float(input("Enter the degree of h(x): ---(Ex: (h(x) = (2x + 3)^1/2 --> Degree of h(x) = 0.5)\n"))
print()

tmp_x = float(input("Enter the starting value(x0): "))
tolerance = float(input("Tolerance(Epsilon): "))

input("Press any key to find root of the equation via Jacobi Method.")
print("---\n")

resGx = [calculateEq(0, 1, 0, tmp_x, 1)]
resHx = [calculateEq(0, hX1, hX0, tmp_x, degreeOfH)]
print("g(%f): %f\nh(%f): %f\n" % (tmp_x, resGx[-1], tmp_x, resHx[-1]))

while abs(resGx[-1] - resHx[-1]) > tolerance:
    resGx.append(calculateEq(0, 1, 0, resHx[-1], 1))
    resHx.append(calculateEq(0, hX1, hX0, resHx[-1], degreeOfH))
    print("g(%f): %f\nh(%f): %f\n" % (resHx[-2], resGx[-1], resHx[-2], resHx[-1]))

print("x_root :", resHx[-1])
