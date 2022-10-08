numbers = "8 3 -5 42 -1 0 0 -9 4 7 4 -4"
# Method 1
'''numbers = numbers.split()
print(numbers)
num_list = []
for i in numbers:
    num_list.append(int(i))

print(num_list)
num_list.sort()
max = num_list[len(num_list)-1]
min = num_list[0]
num_list.clear()
print(num_list)
num_list.append(str(max))
num_list.append(str(min))

print(" ".join(num_list))'''

# Method 2
nums = sorted(numbers.split(), key=int)
print('{} {}'.format(nums[-1], nums[0]))