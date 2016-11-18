

S = raw_input().strip()
try:
    r = int(S)
    print S
except Exception:
    print "Bad String"