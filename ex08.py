#格式化字符串
formatter = "%r %r %r %r"
#将常量列表对应到变量formatter的格式化字符打印
print formatter % (1, 2, 3, 4)
print formatter % ("noe", "two", "three", "four")
print formatter % (True, False, False, True)
#将变量列表对应到变量formatter的格式化字符打印
print formatter % (formatter, formatter, formatter, formatter)
#使用缩进编写多行代码

print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But is didn't sing.",#输出""为双引号，因为didn's包括'单引号所以不能用''单引号输出.
	"so i said goodnight."
)
	

