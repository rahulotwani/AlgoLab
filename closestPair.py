import math
def last(n):
    return n[1]
def dist(p1,p2):
    return math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)
def stpCls(st,d):
    m=d
    n=len(st)
    st.sort(key=lambda x:x[1])
    for i in range(n):
        for j in range(i+1,n):
            if dist(st[i],st[j])<m and (st[j][1]-st[i][1])<m:
                m=dist(st[i],st[j])
    return m
def findDist(pt,n):
    m=float("inf")
    for i in range(n):
        for j in range(i+1,n):
            if dist(pt[i],pt[j])<m:
                m=dist(pt[i],pt[j])
    return m
def closest(pt,n):
    if n<=3:
        return findDist(pt,n)
    mid=n//2
    mp=pt[mid]
    dl=closest(pt[:mid],mid)
    dr=closest(pt[(mid-1):],n-mid)
    d=min(dl,dr)
    strip=[]
    for i in range(n):
        if abs(pt[i][0]-mp[0])<d:
            strip.append(pt[i])
    return min(d,stpCls(strip,d))
if __name__=="__main__":
    #print("Enter Total No. of points")
    n=int(input())
    #print("Enter Points")
    pt=[]
    for i in range(n):
        inp=[int(x) for x in input().split()]
        pt.append(inp)
    pt.sort()
    print(closest(pt,n))

