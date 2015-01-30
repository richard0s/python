print "How old are you?",#print最后加,逗号表示不会换行
age = raw_input() #raw_input()获取用户输入
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "so, you're %r old, %r tall and %r heavy." % (
	age, height, weight)