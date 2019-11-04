def last(n):
    return n[1]
def compatible(l,i):
    for j in range(i-1,-1,-1):
        #print(l[i][0],l[j][1])
        if l[i][0]>=l[j][1]:
            return j
    return -1
def maxJob(l,n):
    dp=[]
    dp.append(l[0][2])
    job=[]
    index=[]
    index.append([0])
    for i in range(1,n):
        ind=compatible(l,i)
        #print(ind)
        if ind==-1:
            dp.append(l[i][2])
            index.append([i])
        else:
            if l[i][2]+l[ind][2]>dp[i-1]:
                dp.append(l[i][2]+l[ind][2])
                index.append(index[ind]+[i])
                #print(index[i])
            else:
                dp.append(dp[i-1])
                index.append(index[i-1])
                #print(index[i])
    for i in index[n-1]:
        print(l[i])
if __name__=="__main__":
    n=int(input())
    l=[]
    for i in range(0,n):
        p=input().split()
        tup=[]
        for j in p:
            tup.append(int(j))
        l.append(tup)
    l.sort(key=lambda x:x[1])
    #print(l)
    maxJob(l,n)