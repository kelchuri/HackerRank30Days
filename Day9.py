
def fact(n):
    if n<=1:
        return n
    else:
        return n * fact(n-1)

num = int(raw_input())
print fact(num)
