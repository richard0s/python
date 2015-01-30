x = "There are %d types of people"% 10
binary = "binary"
do_not = "don't"#字符串内包含'单引号字符所以不能用"双引号
y = "Those who know %s and those who %s."% (binary, do_not)

print x
print y

print "I said: %s"% x
print "I also said: %s"% y
hilarious = False #布尔值
joke_evaluation = "Isn`t that joke so funny?! %r" #%r表示原数据格式
print joke_evaluation% hilarious #将变量hilarious的值赋值给变量joke_evaluation的格式化字符
w = "This is the left side of..."
e = "a string with a right side."
print w + e #多个字符串变量使用+加号可以将字符串连接起来