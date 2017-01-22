#题目：输入某年某月某日，判断这一天是这一年的第几天？
year=int(input("year:"))
month=int(input("month:"))
day=int(input("day:"))
result=0
array=[31,28,31,30,31,30,31,31,30,31,30,31]
if(year<=0)or(month<=0)or(month>12)or(day<=0)or(day>array[month-1]):
	print("error input")
else:
	if(year%4==0)and(year%100!=0)or(year%400==0):
		result+=1
	for i in range(1,13):
		if(month>i):
			result+=array[i]
		else:
			break
	result+=day
	print(result)
