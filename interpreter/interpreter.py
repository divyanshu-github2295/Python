def main():
    expression=input("Expression:")
    x,y,z=expression.split(" ")
    inter(x,y,z)

def inter(a,b,c):
    a=int(a)
    c=int(c)
    if b!="/" or c!=0:
        if b=="/":
            print(float(round(a/c,1)))
        elif b=="+":
            print(float(round(a+c,1)))
        elif b=="-":
            print(float(round(a-c,1)))
        elif b=="*":
            print(float(round(a*c,1)))
    else:
        print("its infinity")

main()
