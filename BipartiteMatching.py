from collections import defaultdict
class Graph:
    def __init__(self,graph):
        self.graph=graph
        self.row=len(graph)
    def BFS(self,s,t,parent):
        visited=[False]*(self.row)
        q=[]
        q.append(s)
        visited[s]=True
        while q:
            u=q.pop(0)
            for v in range(0,self.row):
                if visited[v]==False and graph[u][v]>0:
                    q.append(v)
                    parent[v]=u
                    visited[v]=True
        return visited[t]
    def FordFulkerson(self,source,sink):
        parent=[-1]*(self.row)
        max_flow=0
        while self.BFS(source,sink,parent):
            path_flow=float("Inf")
            s=sink
            while source!=s:
                path_flow=min(path_flow,self.graph[parent[s]][s])
                s=parent[s]
            max_flow+=path_flow
            v=sink
            while v!=source:
                u=parent[v]
                self.graph[u][v]-=path_flow
                self.graph[v][u]+=path_flow
                v=parent[v]
        return max_flow
    def findPair(self,n,j):
        for i in range(n+j+2):
                print(graph[i])
        for i in range(n+1,n+j+1):
            for k in range(1,n+1):
                if graph[i][k]==1:
                    print(k,i)
if __name__=='__main__':
    #print("Enter No of People")
    n=int(input())
    #print("Enter No of jobs")
    j=int(input())
    l=defaultdict(list)
    for i in range(1,n+1):
        inp=input().split()
        for val in inp:
            l[i].append(int(val))
    graph=[[0 for col in range(n+j+2)]for row in range(n+j+2)]
    for k in range(1,n+1):
        graph[0][k]=1
    for i in range(1,n+1):
        for v in l[i]:
            graph[i][v]=1
    for v in range(n+1,n+j+1):
        graph[v][n+j+1]=1
    #print(graph)
    #print(l)
    '''
    for i in range(n+j+2):
        print(graph[i])'''
    print("")
    '''graph=[[0,1,1,1,0,0,0,0],
            [0,0,0,0,1,1,1,0],
            [0,0,0,0,1,0,0,0],
            [0,0,0,0,0,1,0,0],
            [0,0,0,0,0,0,0,1],
            [0,0,0,0,0,0,0,1],
            [0,0,0,0,0,0,0,1],
            [0,0,0,0,0,0,0,0]]'''
    g=Graph(graph)
    print(g.FordFulkerson(0,n+j+1))
    g.findPair(n,j)
