#使用import调用python的sys模块.
#argv是参数变量
from sys import argv 
scrint, first, second, third = argv#将参数变量解包到变量中，scrint的值是文件名
print "the script is called:", scrint
print "your first variable is:", first
print "your second variable is:", second
print "your third variable is:", third