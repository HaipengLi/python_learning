"""
输出 9*9 乘法口诀表。
"""
for row in range(1,10):
	for col in range(row,10):
		print("%1d * %1d = %2d "%(row,col,row*col),end=" ")
	print("\n")