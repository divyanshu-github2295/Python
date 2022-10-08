def main():
    greet=converts(input())                  # user input
    print(greet)

# For convertion of Emoticons to Emojis
def converts(text):
    text=text.replace(":)","🙂")
    text=text.replace(":(","🙁")
    return text


main()


