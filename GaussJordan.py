# a = matrix, b = matrix, c = row_1, d = row_2
def swapRows(a, b, c, d):
    n = len(a)
    for i in range(n):
        a[c][i], a[d][i] = a[d][i], a[c][i]
    b[c], b[d] = b[d], b[c]

# i = column index
def notNullColumns(a, b, i):
    j = 0
    if a[i][i] == 0:
        while a[i][i] == 0 and j < len(a):
            if a[j][i] != 0 and a[i][j] != 0:
                swapRows(a, b, i, j)
            j += 1

print("---Gauss jordan---\n")

print("Enter the number of unknown variables.")
n = int(input("N: "))

print("Enter the matrix of coefficients .")

a = [[float(input("M[{}][{}]: ".format(j + 1, i + 1))) for i in range(n)] for j in range(n)]

print("Enter the result matrix.")

b = [float(input("C[{}]: ".format(i))) for i in range(n)]

for i in range(n):
    notNullColumns(a, b, i)

i = 0
while i < n and a[i][i] != 0 :
    i += 1

if i == n:
    for i in range(n):
        for j in range(n):
            if i != j:
                x = a[j][i] / a[i][i]
                for k in range(n):
                    a[j][k] = a[j][k] - a[i][k] * x
                b[j] = b[j] - b[i] * x
    for i in range(n):
        x = a[i][i]
        for j in range(n):
            a[i][j] /= x
        b[i] /= x
    for i in range(n):
        print("x{} = {}".format(i + 1, b[i]))

