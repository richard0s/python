#----------------------
#程序名：ex21.py
#功能：用QQ号计算年龄
#作者：Richard
#更新时间：2015-02-04
#----------------------

#调用sys模块
import sys
#异常处理
try:
	name = sys.argv[1]
except IndexError:#处理IndexError异常
	print u"""请输入参数:
\tex21.py <Your_Name>
	""".encode("gbk"),
	exit()
#定义函数
def add(x, y):
	print "ADD: %d + %d" %(x, y)
	add = x + y
	return add#使用return返回值
def sub(x, y):
	print "SUB: %d - %d" %(x, y)
	sub = x - y
	return sub
def mul(x, y):
	print "MUL: %d * %d" %(x, y)
	mul = x * y
	return mul
def mod(x, y):
	print "MOD: %d %% %d" %(x, y)
	mod = x % y
	return mod
qqfn = int(raw_input(u"请输入你QQ号码的第一位数字>> ".encode("gbk")))#使用int()转换为整数，
first = mul(add(mul(qqfn, 5), 8), 20)
birthday = int(raw_input(u"如果你的生日过了，请输入1848，否则输入1847>>  ".encode("gbk")))
second = add(first, birthday)
year = int(raw_input(u"请输入你的出生年份>> ".encode("gbk")))
third = sub(second, year)
fourth = mul(qqfn, 100)
fiveth = add(mod(third, fourth), 7)
print u"\n你好, %s.\n\t在 2015 年，你有 %d 岁了".encode("gbk") % (name, fiveth)