#使用from sys import 调用sys模块的argv参数函数功能
from sys import argv
script, file_name = argv#将argv解包到file_name函数
txt = open(file_name)#使用open()打开文件
print "Her's your file %r:" %file_name
print txt.read()#read函数读取打开文件内容
print "Type the filename again:"
file_again = raw_input("$ ")#提示输入新增文件名
txt_again = open(file_again)#打开新增文件
print txt_again.read()#读内容