import math
n = 25
if n >= 0:
    square_root = math.sqrt(n)
    if square_root ** 2 == n:
        print("True")
    else:
        print("False")
else:
    print("False")