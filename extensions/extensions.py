def main():
    file=input("File name: ").strip().lower()

    # Slicing and index() to find index of particular char in string
    ext=file[file.index(".")+1:]
    check(ext)

def check(ans):
    if ans=="gif" or ans=="png":
        print(f"image/{ans}")
    elif ans=="jpeg" or ans=="jpg":
        print("image/jpeg")
    elif ans=="pdf" or ans=="zip":
        print(f"application/{ans}")
    elif ans=="txt":
        print("text/plain")
    else:
        print("application/octet-stream")

main()