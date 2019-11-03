def coin(n,coins):
    for i in range(0,len(coins)):
        no=n//coins[i]
        n=n%coins[i]
        print(coins[i],"->",no)
    print()

coins=[50,25,5,1]
n=int(input("enter amount:"))
coin(n,coins)