#将参数存储在args中
#使用def 变量名(参数名)定义函数
def print_two(*args):
	arg1, arg2 = args#分解args
	print "arg1: %r, arg2: %r," % (arg1, arg2)
#带2个参数的函数
def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)
#带1个参数的函数
def print_one(arg1):
	print "arg1: %r" % arg1
#不带参数的函数
def print_none():
	print "I got nothin."
#使用函数
print_two("Richard","Max")
print_two_again("Richard","MAX")
print_one("Richard")
print_none()