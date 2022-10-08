from PIL import Image

_ = Image.open("shirt.png")
size1 = _.size

_ = Image.open("before1.jpg")
size2 = _.size

_ = Image.open("before2.jpg")
size3 = _.size

_ = Image.open("before3.jpg")
size4 = _.size

print(f"{size1}\n{size2}\n{size3}\n{size4}")

img = Image.open("after.jpg", mode = "rb")
