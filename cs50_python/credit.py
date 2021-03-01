# credit.py

import math

credit = "4003600000000014"

digits1 = ""
digits0 = ""
sum_digits1 = 0
sum_digits0 = 0

for i in range(len(credit)):
    if i % 2 == 1:
        j = 2 * int(credit[-i - 1])
        digits1 += str(j)

for i in range(len(digits1)):
    sum_digits1 += int(digits1[i])

for i in range(len(credit)):
    if i % 2 == 0:
        digits0 += str(credit[-i - 1])

for i in range(len(digits0)):
    sum_digits0 += int(digits0[i])

result = sum_digits0 + sum_digits1

if result % 10 == 0:
    print("VISA")
else:
    print("INVALID")




