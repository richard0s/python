def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man thar's enough for a party!"
	print "Get a blanket.\n"
	
print "Number:"
cheese_and_crackers(10, 20)#可以使用数字表示参数

cheese = 30
crackers = 40
print "variables:"
cheese_and_crackers(cheese, crackers)#可以使用函数表示参数
print "expression:"
cheese_and_crackers(cheese + crackers, crackers - cheese)#可以使用表达式表示函数