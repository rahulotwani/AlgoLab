
def bfs(graph):

    vis=[0]*7

    queue=[]
    queue.append(1)
    vis[1]=1

    while len(queue):

        tmp=[]

        for i in range(len(queue)):

            for j in range(len(graph[queue[i]])):

                if vis[graph[queue[i]][j]]==0:
                    vis[graph[queue[i]][j]]=3-vis[queue[i]]
                    tmp.append(graph[queue[i]][j])
                else:
                    if vis[graph[queue[i]][j]]+vis[queue[i]]!=3:
                        return 0

        queue=tmp

    return 1



graph={1:[2,5],
       2:[1,3],
       3:[2,4],
       4:[3,5],
       5:[1,4]}

#graph={1:[2,4],
 #      2:[1,3],
  #     3:[2,4],
   #    4:[1,3]}

print(bfs(graph))
