def is_isogram(string):
    string = string.lower()
    count = 0
    for i in range(len(string)):
        for j in range(i+1, len(string)):
            if string[i] == string[j]:
                return False
    return True
    #return len(string) == len(set(string.lower()))

s = "aba"
print(is_isogram(s))
