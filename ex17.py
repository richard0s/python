from sys import argv
from os.path import exists#exists方法会检查文件是否存在，返回True或False
script, from_file, to_file = argv
tit = "> "
print "%scopying from %s to %s" % (tit, from_file, to_file)
#读取文件
in_file = open(from_file)
indata = in_file.read()
#输出文件信息
print "%sThe input is %d bytes long." % (tit, len(indata))#len()函数会返回字符串的长度
print "%sRead, hit RETURN to conrinue, Ctrl-C to abrt." % tit
raw_input(tit)
#复制文件
out_file = open(to_file,"w")
out_file.write(indata)
print "%sAlright, all done." % tit
#关闭文件
out_file.close()
in_file.close()
