import mytest


print '----This is func1----'
mytest.world.func1()
print '----This is func2----'
mytest.simple.func2()
print '----This is func3----'
mytest.whatever.func3()

print '----This is myobj using MyClass----'
myobj = mytest.MyClass('nick', 'florida')

myobj.hello()
