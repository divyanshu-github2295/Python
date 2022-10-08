number = int(input("Enter a number? "))
for i in range(2, number):
    count = 0
    for j in range(2, i+1):
        if i % j == 0:
            count += 1
        else:
            pass

    if count == 1:
        print(i, end = " ")
        continue
print()

