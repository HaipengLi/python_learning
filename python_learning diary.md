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
> Note that x== (the last element in list) rather than (the last +1 )

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

## 006 define a function

`def function name(parameter list):`

---

define a function to calculate absolute value

```python
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
```

---

define a function to calculate Fibonacci sequence

```python
def Fibonacci(n):
	if(n==0):
		return 0
	if(n==1)or(n==2):
		return 1
	else:
		return Fibonacci(n-1)+Fibonacci(n-2)
```

## 007 something more about `print()`

### print a empty line

`print()` is ok

### print several empty line

`print("\n")` print 2 empty line

### print without a  new line

`print(something, end="")` is ok

### print with format

---

example: print 9*9 multiplication table

```python
for row in range(1,10):
	for col in range(row,10):
		print("%1d * %1d = %2d "%(row,col,row*col),end=" ")
	print("\n")
```

---

format: `print(sth,"%3.1f & %6.2f "%(a,b),sth)`

%3.1f: width is 3, round to the nearest tenth

## `008 import time`
### `time.sleep(1)`
```python
import time
time.sleep(1)#delay one second
```
### some other thing about time

![time module](./time_module.jpg)

```python
>>> time.time()#Timestamp
1485148323.7097616
>>> time.localtime(time.time())#struct_time
time.struct_time(tm_year=2017, tm_mon=1, tm_mday=23, tm_hour=13, tm_min=12, tm_sec=51, tm_wday=0, tm_yday=23, tm_isdst=0)
>>> time.asctime()# string: %a %b %d %H:%M:$S %Y
'Mon Jan 23 13:13:12 2017'
```

## `009 dict`

### basic operation: define, find

```python
>>> Score={'Leo':100,'Bob':70}
>>> Score
{'Leo': 100, 'Bob': 70}
>>> Score['Leo']
100
>>> Score['Hah'] #bad way
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'Hah'
    
>>> 'Leo' in Score #good way
True
>>> 'Hah' in Score
False
```

###  add

```python
>>> Score['Harry']=80
>>> Score
{'Leo': 100, 'Bob': 70, 'Harry': 80}
>>> Score[100]=2
>>> Score
{'Leo': 100, 'Bob': 70, 'Harry': 80, 100: 2}
```

### remove

```python
>>> Score.pop(100)
'Leo'
>>> Score
{'Leo': 100, 'Bob': 70, 'Harry': 80}
```

### use `dict` in loop

```python
# wrong way
>>> for key,value in Score:
...     print(Score[key])
...
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: too many values to unpack (expected 2)
```

```python
# right way
>>> for key,value in dict.items(Score):
...     print(Score[key])
...
100
70
80
```

```python
# right way
>>> for key in Score:
...     print(key,": ",Score[key])
...
Leo :  100
Bob :  70
Harry :  80
```

## 010 

