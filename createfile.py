
import os

filename = input("Enter file name: ")
f = open(filename, 'w')
while True:
    aLine = input("Enter a line ('.' to quit): ")
    if aLine != '.':
        #f.write('%s%s' % (aLine, os.linesep)) - next line
        #f.write('%s' % aLine) - no next line
        f.write('%s\n' % aLine) #for next line
    else:
        break
f.close()