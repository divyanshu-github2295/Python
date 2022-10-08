def main():
    x=input("What time is it? ")
    time=convert(x)

    if 7<=time<=8:
        print("breakfast time")
    elif 12<=time<=13:
        print("lunch time")
    elif 18<=time<=19:
        print("dinner time")

#for converting time in str to float
def convert(t):
    hours, minutes=t.split(":")
    hours=float(hours)
    minutes=float(minutes)
    return hours+minutes/60


if __name__ == "__main__":
    main()

