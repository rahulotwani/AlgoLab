den=[50,25,5,1]

def coin(n):

    ans=0

    for i in range(len(den)):

        ans+=n//den[i]
        n-=(n//den[i])*den[i]

    return ans

print(coin(77))
print(coin(81))
