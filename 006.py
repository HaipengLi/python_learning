"""
Fibonacci sequence
"""
array=[0,1]
N=int(input("N:"))
if(N==0):
	print("[0]")
elif(N==1):
	print(array)
else:
	for i in range(N-2):
		temp=array[i]+array[i+1]
		array.append(temp)
	print(array)