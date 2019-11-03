def weighted(s,f,v):

    n=len(s)
    index=list(range(n))

    index.sort(key=lambda i:f[i])

    ans=0

    dp=[0]*(n+1)
    
    for i in range(n):

        hi=v[index[i]]
        
        for j in range(0,i+1):

            if s[index[i]]>=f[index[j]]:
                hi=dp[j]+v[index[i]]

        dp[i]=hi

    for i in range(n+1):
        ans=max(ans,dp[i])

    return ans

        


s=[1,3,6,2]
f=[2,5,19,100]
v=[50,20,100,200]

print(weighted(s,f,v))
