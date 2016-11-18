import sys


n = int(raw_input().strip())
ones = '{0:b}'.format(n).split('0')
max = 0
for each in ones:
    if(len(each) > max):
        max = len(each)
print max