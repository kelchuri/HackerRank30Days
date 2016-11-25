import math

nos = []
def check_prime(num):
    if num == 1:
        return "Not prime"
    sq = int(math.sqrt(num))
    for x in range(2, sq+1):
        if num % x == 0:
            return "Not prime"
    return "Prime"

number = int(raw_input())
for i in range(number):
    no = int(raw_input())

    nos.append(check_prime(no))
for each in nos:
    print each