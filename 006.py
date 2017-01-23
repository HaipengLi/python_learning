"""
Fibonacci sequence
"""
def Fibonacci(n):
	if(n==0):
		return 0
	if(n==1)or(n==2):
		return 1
	else:
		return Fibonacci(n-1)+Fibonacci(n-2)
	

array=[0,1]
N=int(input("N:"))
choice=int(input("interation (1) or recursion (2) ?"))
if(choice==1):
	if(N==0):
		print("[0]")
	elif(N==1):
		print(array)
	else:
		for i in range(N-2):
			temp=array[i]+array[i+1]
			array.append(temp)
		print(array)
elif(choice==2):
	print(Fibonacci(N))
else:
	print("byebye")