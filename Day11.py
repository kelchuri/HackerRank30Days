#!/bin/python

maximum = -63
arr = []
for arr_i in xrange(6):
   arr_temp = map(int,raw_input().strip().split(' '))
   if all((item >= -9 and item <= 9) for item in arr_temp):
        arr.append(arr_temp)

for i in range(4):
    for j in range(4):
        maximum = max(arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j]
                      + arr[i+2][j+1] + arr[i+2][j+2], maximum)

print maximum


