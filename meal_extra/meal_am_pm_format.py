def main():
    x=input("What time is it? ")
    z, y=x.split(" ")
    time=convert(z)

    if y=="a.m.":
        if 7<=time<=8:
            print("breakfast time")
    else:
        if 12<=time<=12.99 or time==1:
            print("lunch time")
        elif 6<=time<=7:
            print("dinner time")

#for converting time in str to float
def convert(t):
    hours, minutes=t.split(":")
    hours=float(hours)
    minutes=float(minutes)
    return hours+minutes/60


if __name__ == "__main__":
    main()

