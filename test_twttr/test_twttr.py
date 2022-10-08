from twttr import shorten


def main():

    # Calling test_vowel function
    test_vowel()

    # Calling test_digits function
    test_digits()

    # Calling test_punctuation function
    test_punctuation()


# Test whether program proper removing vowel or not
def test_vowel():
    assert shorten("HitchhIker") == "Htchhkr"
    assert shorten("gAlaxy") == "glxy"
    assert shorten("twitter") == "twttr"
    assert shorten("bzx") == "bzx"


#  Test whether program omitting digits
def test_digits():
    assert shorten("4512Hw") == "4512Hw"
    assert shorten("124x7") == "124x7"


# Test whether program omitting punctuations
def test_punctuation():
    assert shorten("{ca},gf.") == "{c},gf."
    assert shorten("(io)?right!") == "()?rght!"


if __name__ == "__main__":
    main()