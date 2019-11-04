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
        print(graph)
        return max_flow
if __name__=='__main__':
    graph=[[0, 16, 13, 0, 0, 0], 
        [0, 0, 10, 12, 0, 0], 
        [0, 4, 0, 0, 14, 0], 
        [0, 0, 9, 0, 0, 20], 
        [0, 0, 0, 7, 0, 4], 
        [0, 0, 0, 0, 0, 0]]
    g=Graph(graph)
    s=0
    t=5
    print(g.FordFulkerson(s,t)) 