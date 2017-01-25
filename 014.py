"""
题目：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。
"""
import math
import time
def FindNextPrime(p):
	np=p+1
	while(1):
		i=2
		while(i<=int(math.sqrt(np))):
			q=np/i
			if(q-int(q)==0):
				break
			i+=1
		if(i==int(math.sqrt(np))+1):
			#prime
			break
		else:
			np+=1
	return np
Number=int(input("Number: "))
print("%d="%Number,end="")
p=2
if(Number<=0):
	print("error")
elif(Number==1):
	print("1")
else:
	while(Number!=p):
		while(Number/p==Number//p)and(Number!=p):
			print("%d*"%p,end="")
			Number/=p
		if(Number!=p):
			p=FindNextPrime(p)
	print(p)	
