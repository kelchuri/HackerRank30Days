import sys


n = int(raw_input().strip())

if n >=2 and n<=20:
    for i in range(1,11):
        print str(n) + " x " + str(i) + " = " + str(n*i)
