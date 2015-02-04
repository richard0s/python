#使用from sys import argv调用sys模块的argv功能
from sys import argv
script, filename = argv

print "we're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit return."
raw_input("?")
print "Opening the file..."
targen = open(filename,'w')#以写模式打开文件，会将清空原内容
print "Truncating the file. Goodbye!"
#targen.truncate()，truncate()方法表示截断文件
print "Now I'm going to ask you for three lines."
line1 = raw_input("(w)> ")
line2 = raw_input("(w)> ")
line3 = raw_input("(w)> ")
#使用write()方法将字符串写入文件
targen.write(line1 + "\n")
targen.write(line2 + "\n")
targen.write(line3 + "\n")

print "And finally, we close it."
targen.close()#关闭文件