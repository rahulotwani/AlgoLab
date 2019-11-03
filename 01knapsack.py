'''def KnapSack(val, wt, n, W): 
    dp = [0]*(W+1); 
    for i in range(n): 
        for j in range(W,wt[i],-1): 
            dp[j] = max(dp[j] , val[i] + dp[j-wt[i]])
    return dp[W]
'''
def knapSack(W, wt, val, n): 
    K = [[0 for x in range(W+1)] for x in range(n+1)] 
  
    # Build table K[][] in bottom up manner 
    for i in range(n+1): 
        for w in range(W+1): 
            if i==0 or w==0: 
                K[i][w] = 0
            elif wt[i-1] <= w: 
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]],  K[i-1][w]) 
            else: 
                K[i][w] = K[i-1][w] 
  
    return K[n][W] 

val=[]
wt=[]
n=int(input("enter no of values:"))
print("enter values:")
for i in range(n):
    val.append(int(input()))
print("enter weights:")
for i in range(n):
    wt.append(int(input()))

W=int(input("enter Weight:"))
 
print(knapSack(W,wt,val,n))