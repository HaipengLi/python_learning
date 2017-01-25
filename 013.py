"""
打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。
"""
def divide(i):
	L=[]
	while((i)>0):
		L.append((i%10))
		i//=10
	return L
for i in range(100,1000):
	DList=divide(i)
	result=0
	for j in DList:
		result+=pow(j,3)
	if(result==i):
		print(i)