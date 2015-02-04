import sys
file_name = sys.argv[1]
def print_all(add):
	print add.read()
#移动指针到文件的起始位置
def re(fo):
	fo.seek(0)
#打印行号
def line(line_nu, file):
	print line_nu, file.readline(),#readline()表示读取文件的\n
fileob = open(file_name)
print_all(fileob)
print "\n"
re(fileob)
line_n = 1
line(line_n, fileob)
line_n += line_n #+=等同于a=a+a
line(line_n, fileob)
line_n = line_n + 1
line(line_n, fileob)
