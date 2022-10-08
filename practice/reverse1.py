def reverse_words(text):
    count_space = 0
    for i in text:
        if i.isspace():
            count_space += 1
    text = text.split()
    print(text)
    reverse = []
    for word in text:
        word = list(word)
        word.reverse()
        reverse.append("".join(word))
    return " ".join(reverse)

print(reverse_words("double  spaced  words"))