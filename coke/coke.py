def main():
    cashier(50)

# Doing calculation and computing amount owned
def cashier(due):
    while True:
        print("Amount Due:",due)
        coin=int(input("Insert coin: "))
        if coin==25 or coin==10 or coin==5:
            due=due-coin
        if(due<=0):
            print("Amount Owned:",due*-1)
            break

main()
