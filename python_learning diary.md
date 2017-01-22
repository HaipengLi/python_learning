## python 3.6 configuration in VS Code

- establish a new folder, and open it in vs code as python's work folder

- open menu "file->preference->user setting", and find the item named "python.pythonPath". copy it to right window and change it as your python path. mine is "C:/Python36/python.exe"  Note that "/" symbol

- install python extension (omit)

- open launch.json, ![img](http://img.blog.csdn.net/20161208135620414)

- new a .py file in this folder, press F5 to debug. choose "Python" environment.

- ok?!
## 001 using loop: two kinds of loops
### `for x in ...:`
- 依次把list或tuple中的每个元素迭代出来

```python
names = ['Michael', 'Bob', 'Tracy']
for name in names:
print(name)
```
- `range()` generate a sequence, and `list()` convert it to a list

```python
>>> range(5)
range(0,5)
>>> list(range(5))
[0,1,2,3,4]
```

something other about `range()`:      

- `range(0,10,3)` generate 0,3,6,9 four numbers

###  `while`

```python
m_sum=0
n=100
while n>0:
	m_sum=m_sum+n
	n=n-1
print(m_sum)
```

## 002 condition sentences

`if...elif...else...`

```python
age=3
if (age>3):#parantheses can be omitted
	print(1)
elif age==3:
	print(0)
else:
	print(-1)
```

## 003 import math

`import math`

then we can use some useful math funtion

- `math.sqrt()`

- to judge whether a number is a perfect square number

```python
  import math
  cnum=int(intput('enter a number: '))
  cnum=math.sqrt(cnum)
  if(cnum-int(cnum)==0):
      print("yes")
  else :
      print("no")
```

## 004 list generator

- background: input N integers and output them in ascending order

### using `array.appand()`

```python
N=int(input("total number:"))
array=[]
for i in range(N):
	array.append(int(input()))
for i in range(N):
	print(array[i])
```

### using `array=[x*x for x in range(10)]`

a very handy way do generate a list:

```python
array=[int(input()) for x in range(int(input()))]
```

we can reach the same goal.

```python
>>> [x*x for x in range(10)]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

## 005 call build-in sort function

```python
"""
输入三个整数x,y,z，请把这三个数由小到大输出。
i think the example is too naive, so i change it to "input n integers, and ouput them in ascending order"
"""
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
	sorted(array)
	print(array)
else:
	print("bye-bye")
```

Note that `sorted(array)` can be replaced as `array.sort()`

