from copy import copy

def parent(i):
    return int((i-1)/2)
def left(i):
    return i*2 + 1
def right(i):
    return i*2 + 2
    
class node:
    def __init__(self,name):
        self.name = name
        self.adj_lst = []
        self.key = float('inf')
        self.min_path_found = 'no'
        self.heap_loc = name-1 #constant time addressing after key update
        
class minHeap:
    def __init__(self,arr):
        self.arr = copy(arr)
        self.size = len(arr)
        for i in range(int(self.size/2)-1,-1,-1):
            self.bubble_down(i)
    
    def swap_nodes(self,i,j):
        self.arr[i].heap_loc = j
        self.arr[j].heap_loc = i
        temp = self.arr[i]
        self.arr[i] = self.arr[j]
        self.arr[j] = temp
        
    def bubble_down(self,i):
        l = left(i)
        r = right(i)
        min_loc = i
        if l < self.size and self.arr[min_loc].key > self.arr[l].key:
            min_loc = l
        if r < self.size and self.arr[min_loc].key > self.arr[r].key:
            min_loc = r
        if min_loc != i:
            self.swap_nodes(i,min_loc)
            self.bubble_down(min_loc)
            
    def decrease_key(self,vtx,key):
        vtx.key = key
        loc = vtx.heap_loc
        while loc > 0 and self.arr[parent(loc)].key > self.arr[loc].key:
            self.swap_nodes(loc,parent(loc))
            loc = parent(loc)
                       
    def extract_min(self):
        min_node = self.arr[0]
        self.arr[0] = self.arr[self.size - 1]
        self.size = self.size - 1
        self.bubble_down(0)
        return min_node
        
def dijkstra(graph,source):
    graph[source-1].key = 0
    heap = minHeap(graph)
    while(heap.size > 0):
        cur_node = heap.extract_min()
        cur_node.min_path_found = 'yes'
        for vtx_name,edge_wt in cur_node.adj_lst:
            adj_node = graph[vtx_name-1]
            if adj_node.min_path_found == 'no':
                if adj_node.key > cur_node.key + edge_wt:
                    heap.decrease_key(adj_node,cur_node.key + edge_wt)
        
file = open('dijkstraData.txt','r')
graph = []; n_vtx = 200
for v in range(0,n_vtx):
    graph.append(node(v+1))
    
line = file.readline().split()
while line:
    tail = int(line[0])
    graph[tail-1].name = tail
    for i in range(1,len(line)):
        vtx_name,edge_wt = line[i].split(',')
        graph[tail-1].adj_lst.append([int(vtx_name),int(edge_wt)])
    line = file.readline().split()
    
dijkstra(graph,1)
ans_set = [7,37,59,82,99,115,133,165,188,197]
for i in ans_set:
    print(graph[i-1].key,end=',')