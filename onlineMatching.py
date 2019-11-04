if __name__=='__main__':
    print("Enter The Number of Girls")
    n=int(input())
    b=[False]*n
    l=[]
    cnt=0
    while 1:
        inp=[int(x) for x in input().split()]
        for i in inp:
            if b[i]==False:
                b[i]=True
                tup=i,cnt
                l.append(tup)
                break
        cnt+=1
        print(l)
        if len(l)==n:
            break



