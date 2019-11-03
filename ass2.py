
def piv(l):
    n=len(l)

    if(n<=5):
        l.sort()
        mid=l[n//2]
        #print(type(mid),type(ind))
        return mid

    i=0
    tmp=[]

    while i<n:
        ref=l[i:min(n,i+5)]
        tmp.append(piv(ref))
        i+=5

    return piv(tmp)

def order(l,k):

    if len(l)==1:
        return l[0]
    mid=piv(l)
    tmp1=[]
    tmp2=[]

    for i in range(len(l)):
        if l[i]<mid:
            tmp1.append(l[i])
        else:
            tmp2.append(l[i])

    if(k<=len(tmp1)):
        return order(tmp1,k)
    else:
        return order(tmp2,k-len(tmp1))




l=[7,5,2,3,1,4,8,6,9,11,12,13,14,15,10]
k=7

print(order(l,k))
