eval()函数可对括号中的含变量表达式做运算
0  1  2  3  4  5  6  :正向递增序号
"  1  2  3  4  5  "
-7 -6 -5 -4 -3 -2 -1 :反向递减序号
使用[]获取字符串中一个或多个字符
str[0]获取第一个字 str[0:2]获取前两个字 str[0:-1]字符串去掉末位后输出 str[1:]去首位
['F', 'f', '℉'] : 列表类型数据

print("{:.2f}".format(value))
:.2f表示填充变量取到小数点后两位
{}表示变量填充位置

转义字符\可以转义很多字符，比如\n表示换行，\t表示制表符，字符\本身也要转义，所以\\表示的字符就是\
如果字符串里面有很多字符都需要转义，就需要加很多\，为了简化，Python还允许用r''表示''内部的字符串默认不转义
如果字符串内部有很多换行，用\n写在一行里不好阅读，为了简化，Python允许用''''''的格式表示多行内容
def(a, *b)a表示第一变量，*b表示后面全部变量

常见的占位符有：
占位符	替换内容
%d	    整数
%f	    浮点数
%s	    字符串
%x	    十六进制整数

'Hi, %s, you have $%d.' % ('Michael', 1000000)
'Hi, Michael, you have $1000000.'

有些时候，字符串里面的%是一个普通字符怎么办？这个时候就需要转义，用%%来表示一个%

另一种格式化字符串的方法是使用字符串的format()方法，它会用传入的参数依次替换字符串内的占位符{0}、{1}

'Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125)
'Hello, 小明, 成绩提升了 17.1%'

最后一种格式化字符串的方法是使用以f开头的字符串，称之为f-string，它和普通字符串不同之处在于，字符串如果包含{xxx}，就会以对应的变量替换：

r = 2.5
s = 3.14 * r ** 2
print(f'The area of a circle with radius {r} is {s:.2f}')
The area of a circle with radius 2.5 is 19.62

上述代码中，{r}被变量r的值替换，{s:.2f}被变量s的值替换，并且:后面的.2f指定了格式化参数（即保留两位小数），因此，{s:.2f}的替换结果是19.62

可以使用 Turtle.setup(width, height, startx, starty) 函数来设置启动Turtle绘图窗口的位置和大小，以下是参数解释：
width：Turtle 绘图窗口的宽度。
height：Turtle 绘图窗口的宽度
startx：Turtle 绘图窗口距显示器左侧的距离
starty：Turtle 绘图窗口距显示器顶部的距离
turtle.goto(x, y)：指定 x 和 y 的值，海龟将会到达坐标为（x, y）的位置。
turtle.forward(distance)：控制海龟前进 distance 个单位像素的距离。forwad 可以简写为 fd，
即 turtle.forward(distance) 和 turtle.fd(distance) 的效果是一样的。
turtle.backward(distance)：控制海龟后退 distance 个单位像素的距离。backward可以简写为 ，
即 turtle.backward(distance) 和 turtle.bk(distance) 的效果是一样的。
turtle.circle(r,angle)：以海龟当前位置，左侧的某一个点为圆心，半径为 r 的距离，
画一个角度值为angle 的弧形。如果没有指定 angle 的值，则默认为360度，也就是画一个圆。r 和 angle 的值可以为负数，意为反方向。注意，顺时针旋转的角度度数值为负数，逆时针的为正数。
turtle建立了一个空间坐标体系，那么在空间坐标中，海龟行进的方向也有一个角度，同样分为绝对角度和海龟角度。
对于绝对角度来讲，绝对坐标的x正轴表示0度或360度，y正轴表示90度或-270度，x负轴表示180度或-180度，y负轴表示270度或-90度。
相关的函数有：
turtle.seth(angle)：设置 angel 的值用于改变海龟行进方向，只改变方向不行进。
turtle.left(angle)：让海龟向左改变 angle 个角度
turtle.right(angle)：让海龟向右改变 angle 个角度
Turtle常用函数
5.1 画笔控制函数
turtle.penup() 或者 turtle.pu() 或者 turtle.up()：抬笔，移动时不绘图
turtle.pendown() 或者 turtle.pd() 或者 turtle.down()：落笔，移动时绘图
turtle.pensize(width)：设置画笔尺寸
turtle.width(width)：画笔宽度
turtle.pencolor(*args)：如果不给参数，则返回当前画笔颜色，给出参数则是设定画笔颜色。设置颜色有三种方式的参数，pencolor(colorstring)、pencolor((r,g,b))和pencolor(r,g,b)
5.2 运动控制函数
turtle.forward(distance) 或者 turtle.fd(distance)：前进distance像素
turtle.backward(distance) 或者 turtle.bk(distance) 或者 turtle.back(distance)：后退distance像素
turtle.circle(r,angle)：以画笔（海龟）左侧为圆心，半径为r像素，画angle度的圆形。注意：海龟方向同时发生angle度变化
turtle.goto(x,y)、setpos(x,y)、setposition(x,y)：由当前坐标前往指定坐标，这里使用绝对坐标，但画笔方向不会改变
5.3 方向控制函数
turtle.setheading(angle) 或者 turtle.seth(angle)：以绝对角度改变方向
turtle.left(angle) 或者 turtle.lt(angle)：以海龟角度向左改变方向
turtle.right(angle) 或者 turtle.rt(angle)：以海龟角度向右改变方向


Python列表函数&方法

Python包含以下函数:
序号	函数
1	cmp(list1, list2)
比较两个列表的元素
2	len(list)
列表元素个数
3	max(list)
返回列表元素最大值
4	min(list)
返回列表元素最小值
5	list(seq)
将元组转换为列表

Python包含以下方法:
序号	方法
1	list.append(obj)
在列表末尾添加新的对象
2	list.count(obj)
统计某个元素在列表中出现的次数
3	list.extend(seq)
在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
4	list.index(obj)
从列表中找出某个值第一个匹配项的索引位置
5	list.insert(index, obj)
将对象插入列表
6	list.pop([index=-1])
移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
7	list.remove(obj)
移除列表中某个值的第一个匹配项
8	list.reverse()
反向列表中元素
9	list.sort(cmp=None, key=None, reverse=False)
对原列表进行排序

s = input("")  # 输入一个字符串
ls = []
for c in s:
    ls.append(str(ord(str(c))))
print(','.join(ls))
Python join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。
set

set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。

要创建一个set，需要提供一个list作为输入集合：

>>> s = set([1, 2, 3])
>>> s
{1, 2, 3}

注意，传入的参数[1, 2, 3]是一个list，而显示的{1, 2, 3}只是告诉你这个set内部有1，2，3这3个元素，显示的顺序也不表示set是有序的。。

重复元素在set中自动被过滤：

>>> s = set([1, 1, 2, 2, 3, 3])
>>> s
{1, 2, 3}

通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果：

>>> s.add(4)
>>> s
{1, 2, 3, 4}
>>> s.add(4)
>>> s
{1, 2, 3, 4}

通过remove(key)方法可以删除元素：

>>> s.remove(4)
>>> s
{1, 2, 3}

set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作：

>>> s1 = set([1, 2, 3])
>>> s2 = set([2, 3, 4])
>>> s1 & s2
{2, 3}
>>> s1 | s2
{1, 2, 3, 4}

set和dict的唯一区别仅在于没有存储对应的value，但是，set的原理和dict一样，所以，同样不可以放入可变对象，因为无法判断两个可变对象是否相等，也就无法保证set内部“不会有重复元素”。试试把list放入set，看看是否会报错。