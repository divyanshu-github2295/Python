def main():
    camel= input("Enter something in camelCase: ")
    snake=tosnake(camel)
    print("snake_case:",snake)

#converting camelCase to snake_case

def tosnake(text):
    txt=[text[0]] # list txt
    for c in text[1:]:
        if c.isupper():
            txt.append("_") # add element at last position in list
            txt.append(c)
        else:
            txt.append(c)
    text="".join(txt).lower()
    return text

main()