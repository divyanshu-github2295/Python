import sys
from PIL import Image, ImageOps


def main():

    # Calling check_command_line function
    check_command_line()

    # Calling Tshirt function for image procesing
    Tshirt()


# checking command-line argument
def check_command_line():

    extension = (".jpg", ".jpeg", ".png")

    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    elif sys.argv[1].endswith(extension) and sys.argv[2].endswith(extension):

        _, ext1 = sys.argv[1].split(".")
        _, ext2 = sys.argv[2].split(".")

        if ext1 != ext2:
            sys.exit("Input and output have different extensions")
    else:
        sys.exit("Invalid input")


# Processing the images
def Tshirt():

    try:

        # Opening the Images
        img = Image.open(sys.argv[1])
        shirt = Image.open("shirt.png")

        # Crop and resize the image
        img = ImageOps.fit(img, size=(600, 600))

        '''Paste image in shirt object in img object
            first shirt represent image to overlay and second shirt indicating which pixels to update in img object'''
        img.paste(shirt, shirt)

        # Saving Processed image
        img.save(sys.argv[2])

    except FileNotFoundError:
        sys.exit("Input does not exist")


if __name__ == "__main__":
    main()
