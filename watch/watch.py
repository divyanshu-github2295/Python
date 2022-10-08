import re


def main():

    # Calling the parse function and printing the result
    print(parse(input("HTML: ")))


# Matching and returning the result
def parse(s):

    # Searching pattern in embeded URL provided by the user
    if re.search(r'.+http(?:s?):\/\/(?:www\.)?youtube\.com\/embed\/([\w(%&\?\-)?]+).+', s):
        match = re.search(r'.+http(?:s?):\/\/(?:www\.)?youtube\.com\/embed\/([\w(%&\?\-)?]+).+', s)

        result = f"https://youtu.be/{match.group(1)}"

        return result

    else:
        return None


if __name__ == "__main__":
    main()