#将100赋值给cars变量
cars = 100
#将4.0赋值给apace_in_a_car变量,4还是4.0无影响，因为与其他计算没有产生浮点数
space_in_a_car = 4.0
#将30赋值给drivers变量
drivers = 30
#将90的值赋值给passengers变量
passengers = 90
#将变量cars - 变量drivers的值赋值给cars_not_driven变量,100 - 30
cars_not_driven = cars - drivers
#将变量drivers的值赋值给cars_driven,30
cars_driven = drivers
#将变量cars_driven * space_in_a_car变量的值赋值给carpool_capacity,30 * 4.0
carpool_capacity = cars_driven * space_in_a_car
#将变量passengers / 变量cars_driven 的值赋值给average_passengers_per_car,90 / (100 - 30) 
average_passengers_per_car = passengers / cars_driven
#输出cars的值,100
print "Thers are", cars, "cars available."
#输出drivers的值,30
print "There are only", drivers, "drivers available"
#输出cars_not_drivers的值,100 - 30
print "There will be", cars_not_driven, "empty cars today"
#输出carpool_capacity的值,(100 - 30) * 4.0
print "We can transport", carpool_capacity, "people today"
#输出passengers的值,90
print "We have", passengers, "to carpool today"
#输出average_passengers_per_car的值,90 / (100 - 3)
print "We need to put about", average_passengers_per_car, "in each car"