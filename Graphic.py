print("---Graphical Method---")

def calculateEq(l, x):
    res = 0
    degree = len(l) - 1
    for i in l:
        res += pow(x, degree) * i
        degree -= 1
    return res

#inputs
coefficients = [float(input("Enter the coefficient of the %d. degree of the equation(x^%d): " % (i, i))) for i in range(int(input("Enter the max degree: ")), -1, -1)]
print()
tmp_x = float(input("Enter the starting value(x0): "))
delta_x = float(input("delta_x: "))
tolerance = float(input("Tolerance(Epsilon): "))
l = [0, 0]
k = [tmp_x]
tmp = l[-2]

input("Press any key to find root of the equation via Graphical Method.")
print("---\n")

while abs(tmp) > tolerance or tmp == 0:
    while l[-1] * l[-2] >= 0:
        print("delta_x :", delta_x)
        l.append(calculateEq(coefficients, k[-1]))
        print("Results of the equation :", l[2:])
        print("x value :", k[-len(l) + 2:])
        k.append(k[-1] + delta_x)
        tmp = abs(l[-1] - l[-2])
        print("\n")
    if abs(tmp) > tolerance or tmp == 0:
        print("---")
        delta_x = delta_x / 2
        print("New delta_x :", delta_x)
        l = [0, 0]
        k = k[:-2]
    print("\n")

print("x_root :", k[-3])
