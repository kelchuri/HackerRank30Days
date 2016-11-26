return_date = raw_input()
rd = int(return_date.split()[0])
rm = int(return_date.split()[1])
ry = int(return_date.split()[2])

expected_date = raw_input()
ed = int(expected_date.split()[0])
em = int(expected_date.split()[1])
ey = int(expected_date.split()[2])

if (ry, rm, rd) <= (ey, em, ed):
    print(0)
elif (ry, rm) == (ey, em):
    print(15 * (rd - ed))
elif ry == ey:
    print(500 * (rm - em))
else:
    print(10000)
