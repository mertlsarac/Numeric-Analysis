print("---Trapez Method---\n")

def calculateEq(l, x):
    res = 0
    degree = len(l) - 1
    for i in l:
        res += pow(x, degree) * i
        degree -= 1
    return res

def findH(l, u, n):
    return (u - l) / n	

coefficients = [float(input("Enter the coefficient of the %d. degree of the equation(x^%d): " % (i, i))) for i in range(int(input("Enter the max degree of the equation: ")), -1, -1)]
print()

l = float(input("Enter the lower value of the integral range: "))
u = float(input("Enter the upper value of the integral range: "))
n = int(input("N: "))

h = findH(l, u, n)
print(h)
x = []
y = []

x.append(l)
y.append(calculateEq(coefficients, x[-1]))

print("\n%10s| %10s|" % ("x", "f(x)"))
print("%10s| %10s|" % ("---------", "---------"))
print("%10.8f| %10.8f|" % (x[-1], y[-1]))
while x[-1] != u:
    x.append(h + x[-1])
    y.append(calculateEq(coefficients, x[-1]))
    print("%10.8f| %10.8f|" % (x[-1], y[-1]))

s = 0
for i in range(1, len(y) - 1):
    s += y[i]
s += (y[0] + y[-1]) / 2
s *= h

print("\n\nS: {}".format(s))
