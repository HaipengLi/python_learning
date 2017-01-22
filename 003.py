"""一个整数，它加上100和加上268后都是一个完全平方数，请问该数是多少？"""
import math
for cnum in range(100000):
	num1=math.sqrt(cnum+100)
	num2=math.sqrt(cnum+268)
	if(num1-int(num1)==0)and(num2-int(num2)==0):
		print(cnum)