# without weights

def greedy(start,end,n):
    index=[]
    ans=0
    prev=0
    for i in range(len(start)):
        index.append(i)
    index.sort(key=lambda i:end[i])
    for i in index:
        if start[i]>=prev:
            prev=end[i]
            ans+=1
    return ans

n=int(input("enter no of jobs"))
print("enter start time and finish time on n jobs in n lines separated by spaces")
start=[]
end=[]
for i in range(n):
    time=input().split(" ")
    start.append(int(time[0]))
    end.append(int(time[1]))

print(greedy(start,end,n))