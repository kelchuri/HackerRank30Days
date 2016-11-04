import sys


N = int(raw_input().strip())
if(N%2 != 0):
    print "Weird"
elif (N%2 == 0 and N in [2,3,4,5]):
    print "Not Weird"
elif (N%2 == 0 and N in range(6,21)):
    print "Weird"
elif (N%2 == 0 and N > 20 ):
    print "Not Weird"
