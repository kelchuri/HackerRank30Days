
n = int(raw_input().strip())
inputStrings = []
if n>=1 and n<=10:
    for i in range(n):
        str = raw_input()
        if len(str)>=2 and len(str) <=10000:
            inputStrings.append(str)
    for str in inputStrings:
        odd = ""
        even = ""
        for index in range(len(str)):
            if index%2 == 0:
                even+=str[index]
            else:
                odd+=str[index]
        print even + " " + odd
