def inv(l):
    ans=0
    n=len(l)

    if n==1:
        return 0

    mid=n//2

    arr1=l[:mid]
    arr2=l[mid:n]
    ans+=inv(arr1)
    ans+=inv(arr2)

    i=0
    j=0
    k=0

    while i<mid and j<len(arr2):

        if arr1[i]<=arr2[j]:
            l[k]=arr1[i]
            i+=1
        else:
            l[k]=arr2[j]
            ans+=(mid-i)
            j+=1

        k+=1

    while i<mid:
        l[k]=arr1[i]
        i+=1
        k+=1

    while j<len(arr2):
        l[k]=arr2[j]
        j+=1
        k+=1

    
    return ans


l=[5,1,3,4,2]
#l=[1, 20, 6, 4, 5]

print(inv(l))
#print(l)
