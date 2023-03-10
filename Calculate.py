#TempConvert
print("Please type the temperature data you want to transform")
In = input()
'''
eval()函数可对括号中的含变量表达式做运算
0  1  2  3  4  5  6  :正向递增序号
"  1  2  3  4  5  "
-7 -6 -5 -4 -3 -2 -1 :反向递减序号
使用[]获取字符串中一个或多个字符
str[0]获取第一个字 str[0:2]获取前两个字 str[0:-1]字符串去掉末位后输出 str[1:]去首位
str[m:n[:k]]m位至n位，k为步长
['F', 'f', '℉'] : 列表类型数据
'''
numdata = eval(In[0:-1])
numdata = float(numdata)
'''
print("{:.2f}".format(value))
:.2f表示填充变量取到小数点后两位
{}表示变量填充位置
'''
if In[-1] in ['F', 'f', '℉']:
    numdata = numdata - 32.0
    numdata = numdata / 180.0
    numdata = numdata * 100.0
    Degree = numdata
    print("Degree Celsius : {:.2f}°C".format(Degree))

elif In[-1] in ['C', 'c', '°C']:
    numdata = numdata / 100.0
    numdata = numdata * 180.0
    numdata = numdata + 32.0
    Fahrenheit = numdata
    print("Fahrenheit scale : {:.2f}℉".format(Fahrenheit))

else:
    print("Syntax Error")
