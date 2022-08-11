print("==============================")
print("=== Wellcome to MatrixMult ===")
print("==============================")
print("Type 4 parameters to describe matrixes")
print("[ A: Arg(1)xArg(2)  B: Arg(3)xArg(4) ]")
print("=================================+====")
arg=[]

i=1
while(i <=4):
	print("Podaj Arg", i, ":", sep="", end="")
	arg.append(int(input()))
	if arg[-1]<=0:
		arg.pop()
		print("\tInvalid arg!")
		continue
	i+=1

print("[ A: ", arg[0], "x", arg[1], "  B: ", arg[2], "x", arg[3], " ]", sep="")

A=[]
print("Matrix A:")
for j in range(arg[0]):
	row=[]
	print("\tRow ", j+1,":" , sep="")
	for k in range(arg[1]):
		row.append(input("\t\t"))
	A.append(row)
print("Matrix B:")
B=[]
for j in range(arg[2]):
	row=[]
	print("\tRow ", j+1,":" , sep="")
	for k in range(arg[3]):
		row.append(input("\t\t"))
	B.append(row)
print(A)
print(B)
