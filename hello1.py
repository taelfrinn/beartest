#!/usr/bin/env python
'''beartest'''

lineno = 0

for j in range(0, 10):
    print "Line %d:" % lineno
    print "Hello, %d" % (j)
    lineno += 1
    print "%d squared = %d" % (j*j)

print "program complete"
