class node:
    def __init__(self):
        self.explored = 'no'
        self.finish_time = None
        self.adj_lst = []
        
def depth_first_search(graph,source,finish_time = 1):
    graph[source-1].explored = 'yes'
    for vtx in graph[source-1].adj_lst:
        if graph[vtx-1].explored == 'no':
            finish_time = depth_first_search(graph,vtx,finish_time)
    graph[source-1].finish_time = finish_time
    return finish_time + 1
            
def kosaraju(graph,rev_graph,n_vtx):
    #DFS on G transpose
    finish_time = 1;
    for vtx in range(n_vtx,0,-1):
        if rev_graph[vtx-1].explored == 'no':
            finish_time = depth_first_search(rev_graph,vtx,finish_time)
    #Sort by finish time        
    view_order = [None]*n_vtx
    for vtx in range(1,n_vtx+1):
        view_order[rev_graph[vtx-1].finish_time-1] = vtx
    #DFS on G by finish times    
    scc_n = []
    for i in range(n_vtx,0,-1):
        vtx = view_order[i-1]
        if graph[vtx-1].explored == 'no':
            scc_n.append(depth_first_search(graph,vtx)-1)
    return scc_n
  
file = open('SCC.txt','r')
graph = []; rev_graph = []; n_vtx = 875714
for v in range(0,n_vtx):
    graph.append(node())
    rev_graph.append(node())
edge = file.readline()
while edge:
    [tail,head] = [int(edge.split()[0]),int(edge.split()[1])]
    graph[tail-1].adj_lst.append(head)
    rev_graph[head-1].adj_lst.append(tail)
    edge = file.readline()
scc_n = kosaraju(graph,rev_graph,n_vtx)
print(sorted(scc_n)[-5:])
