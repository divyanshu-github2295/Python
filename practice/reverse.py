
string = "world"
reverse = ""
for i in range(len(string)):
    reverse = reverse + string[len(string)-1-i]

print(reverse)