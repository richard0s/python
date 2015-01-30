#使用from ... import调用sys模块
from sys import argv#使用argv参数变量
script, user_name = argv#将argv参数变量解包到script变量和user_name变量中
prompt = "> "

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
lives = raw_input(prompt)
print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
alright, so you said %r about liing me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (lives, lives, computer)