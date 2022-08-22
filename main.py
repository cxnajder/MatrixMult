
def mnozenieMacierzy(A, B):
    C = [[0 for j in range(len(B[0]))] for i in range(len(A))] #stworzenie macierzy C wypełnionej zerami o wymiarach wiersz A na kolumny B
    for i in range(len(C)):
        for j in range(len(C[0])):
            for k in range(len(B)):
                C[i][j]+=A[i][k]*B[k][j]
    return C

print("="*60)
print("=", "Wellcome to MatrixMult".center(56), "=")
print("="*60)
print("=", "Type 4 parameters to describe matrixes".center(56), "=")
print("=", "[ A: Arg(1)xArg(2)  B: Arg(3)xArg(4) ]".center(56), "=")
print("="*60)
arg = []

i = 1
a=0
while i <= 4:
    print("Podaj Arg", i, ":", sep="", end="")
    try:
        a=int(input())
        assert a > 0
        arg.append(a)
        i += 1
    except ValueError:
        print("Try to insert a valid argument")
    except AssertionError:
        print("The argument can't be lower then 1")

print("[ A: ", arg[0], "x", arg[1], "  B: ", arg[2], "x", arg[3], " ]", sep="")

if arg[1] == arg[2]:
    A = []
    print("Matrix A:")
    for j in range(arg[0]): #pobranie wartości do macierzy A -- arg[0] to liczba wierszy
        row = []
        print("\tRow ", j + 1, ":", sep="")
        for k in range(arg[1]): #arg[1] to liczba kolumn
            row.append(int(input("\t\t")))
        A.append(row)
    print("Matrix B:")
    B = []
    for j in range(arg[2]): #pobranie wartości do macierzy A -- arg[2] - liczba wierszy
        row = []
        print("\tRow ", j + 1, ":", sep="")
        for k in range(arg[3]): # arg[3] - liczba kolumn
            row.append(int(input("\t\t")))
        B.append(row)
    print("A=", end="")
    for row in A: #narysowanie macierzy A
        print('\t', row, sep="")
    print()
    print("B=", end="")
    for row in B: #narysowanie macierzy B
        print('\t', row, sep="")
    print()
    C = mnozenieMacierzy(A, B)
    print("A x B = C")
    print()
    print("C=", end="")
    for row in C:
        print('\t', row, sep="")
else: 
    print("Cant multiply matrix becouse Arg(2) =/= Arg(3)!")
 