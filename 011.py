# (too naive, and i improve its difficulty) a rabbit bears a baby every month from the third month on。  but rabbits will die at the six month
def RabbitNum(n):
	if(n<=0):
		return 0
	if(n==1)or(n==2):
		return 1
	else:
		return (RabbitNum(n-1)+RabbitNum(n-2)-2*RabbitNum(n-5)+2*RabbitNum(n-6))
N=int(input("Month:"))
print(RabbitNum(N))
