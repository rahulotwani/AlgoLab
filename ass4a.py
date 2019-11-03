
def greedy(s,f):

    n=len(s)
    index=list(range(n))

    index.sort(key=lambda i:f[i])

    ans=0
    prev=0
    for i in index:
        if s[i]>=prev:
            ans+=1
            prev=f[i]

    return ans



#s=[1, 3, 0, 5, 8, 5]
#f=[2, 4, 6, 7, 9, 9]

s=[10, 12, 20]
f=[20, 25, 30]

print(greedy(s,f))
