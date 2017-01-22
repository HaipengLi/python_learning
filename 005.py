#输入三个整数x,y,z，请把这三个数由小到大输出。
#i think the example is too naive, so i change it to "input n integers, and ouput them in ascending order"
N=int(input("total number: "))
array=[int(input())for x in range(N)]

choice=int(input("use hand-written insertionsort (1) or call stdlib sort function (2)?"))
if(choice==1):
	for x in range(N):
		i=x-1
		temp=array[x]
		while(i>=0):
			if(array[i]>temp):
				array[i+1]=array[i]
				i-=1;
			else:
				break
		array[i+1]=temp
	print(array)
elif (choice==2):
	#sorted(array)
	array.sort()
	print(array)
else:
	print("bye-bye")
