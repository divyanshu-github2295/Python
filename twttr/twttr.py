def main():
    tweet=input("Input: ")
    tweet=rmvowel(tweet)
    print("Output:",tweet)

#removing vowel from input

def rmvowel(text):
    txt=[]                  # Empty List

    vowel=["a","e","i","o","u","A","E","I","O","U"]
    for c in text:
        if c not in vowel:
            txt.append(c)

    text="".join(txt)
    return text

main()
