# a = matrix, b = matrix, c = row_1, d = row_2
def swapRows(a, b, c, d):
    n = len(a)
    for i in range(n):
        a[c][i], a[d][i] = a[d][i], a[c][i]
        b[c][i], b[d][i] = b[d][i], b[c][i]

# i = column index
def notNullColumns(a, b, i):
    j = 0
    while a[i][i] == 0 and j < len(a):
        if a[j][i] != 0:
            swapRows(a, b, i, j)
        j += 1

print("---Inverse of the Matrix---\n")

print("The matrix you want to reverse must have the same number of rows as the columns.")
print("(number of rows = number of columns = n)")

n = int(input("N: "))

a = [[float(input("M[{}][{}]: ".format(j + 1, i + 1))) for i in range(n)] for j in range(n)]
# a = [[1, 7, 9], [0, 1, 0], [0, 0, 1]]
b = [[0 for i in range(n)] for j in range(n)]
for i in range(n):
    b[i][i] = 1

i = 0
flag = 1
while i < n and flag == 1:
    flag = notNullColumns(a, b, i)

i = 0
while i < n and a[i][i] != 0 :
    i += 1
flag = 1
if i != n:
    print("The matrix can not be reversed.")
    flag = 0

if flag == 1:
    for i in range(n):
        for j in range(n):
            if i != j:
                x = a[j][i] / a[i][i]
                for k in range(n):
                    a[j][k] = a[j][k] - a[i][k] * x
                    b[j][k] = b[j][k] - b[i][k] * x
    for i in range(n):
        x = a[i][i]
        for j in range(n):
            a[i][j] /= x
            b[i][j] /= x
    for i in range(n):
        for j in range(n):
            print(b[i][j], end='    ')
        print()

