#判断101-200之间有多少个素数，并输出所有素数。
import math
result=0;
i=101
while(i<=200):
	j=2
	while(j<=int(math.sqrt(i))):
		q=float(i)/j
		if(q-int(q)==0):
			break
		j+=1
	if(j==int(math.sqrt(i))+1):
		print(i)
		result+=1
	i+=1
print(result)