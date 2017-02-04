"""
输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
"""
myString=str(input("Input a string: "))
NumOfLetters=0
NumOfSpaces=0
NumOfDigits=0
NumOfOthers=0
for myChar in myString:
    print(myChar)
    if(myChar.isalpha()):
        NumOfLetters+=1
    elif(myChar.isdigit()):
        NumOfDigits+=1
    elif(myChar==' '):
        NumOfSpaces+=1
    else:
        NumOfOthers+=1
print('NumOfLetters: %d\nNumOfDigits: %d\nNumOfSpaces: %d\nNumOfOthers: %d'%(NumOfLetters,NumOfDigits,NumOfSpaces,NumOfOthers))
