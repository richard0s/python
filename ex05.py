#信息变量
name = 'Richard'
gender = 'Man'
age = 18
height = 175.00 #单位CM
weight = 60.00 #单位KG
#格式化字符串输出
print "Hi, %s" % name #%s表示字符串格式
print "You are an %d year old %s" % (age, gender) #%d表示整数格式
print "Your height is %f CM, equivalent to %f IN." % (height, height * 0.39)#%f表示浮点数格式
print "Your weight is %f KG, equivalent to %f LB." % (weight, weight * 2.20)
