
def bfs(graph):
    n=len(graph)
    m=len(graph[0])

    vis=[[0,0,0,0,0,0],
       [0,0,0,0,0,0],
       [0,0,0,0,0,0],
       [0,0,0,0,0,0],
       ]
    ans=0
    
    for i in range(0,n):
        for j in range(0,m):

            #print(len(vis))
            #print(i,j)
            if vis[i][j]==0:

                queue=[]
                queue.append([i,j])
                vis[i][j]=1
                col=graph[i][j]

                #print(i,j)
                #print(col)

                ans+=1

                while len(queue)!=0:
                    tmp=[]

                    for k in range(len(queue)):

                        x=queue[k][0]
                        y=queue[k][1]

                        #print(x,y)

                        if x!=0 and vis[x-1][y]==0 and graph[x-1][y]==col:
                            tmp.append([x-1,y])
                            vis[x-1][y]=1

                        if y!=0 and vis[x][y-1]==0 and graph[x][y-1]==col:
                            tmp.append([x,y-1])
                            vis[x][y-1]=1

                        #print(graph[x+1][y],x,vis[x+1][y])

                        if x!=n-1 and vis[x+1][y]==0 and graph[x+1][y]==col:
                            tmp.append([x+1,y])
                            vis[x+1][y]=1

                        if y!=m-1 and vis[x][y+1]==0 and graph[x][y+1]==col:
                            tmp.append([x,y+1])
                            vis[x][y+1]=1

                    queue=tmp

    return ans



graph=[[1,0,0,0,0,1],
       [1,1,2,0,0,0],
       [1,2,2,0,0,0],
       [1,1,2,1,1,1],
       ]

print(bfs(graph))

