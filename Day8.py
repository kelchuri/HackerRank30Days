import sys

# Read input and assemble Phone Book
n = int(input())
phoneBook = {}
for i in range(n):
    contact = input().split(' ')
    phoneBook[contact[0]] = contact[1]


lines = sys.stdin.readlines()
for i in lines:
    query = i.strip()
    if query in phoneBook:
        print(query + '=' + str(phoneBook[query]))
    else:
        print('Not found')