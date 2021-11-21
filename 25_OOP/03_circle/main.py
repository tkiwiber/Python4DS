from circle import Circle

print('\n')
print('>' * 18, 'base unit tests:')
c1 = Circle()
c2 = Circle(0, 0, 0.5)
c3 = Circle(1, 0, 0.5)
print(c1.length())
print(c1.square())
print(c1.intersected(c2))
c2.increase(3)
print(c2.length())
print(c1.intersected(c3))
print('\n')
print('>' * 18, 'handle class methods errors:')
try:
    print(c1.increase('t'))
except Exception as err:
    print(err)
try:
    print(c1.increase(-1))
except Exception as err:
    print(err)
try:
    print(c1.intersected('c2'))
except Exception as err:
    print(err)
