graph={'A':['C','B'],
    'C':['F','A'],
    'B':['E','D'],
    'F':['C','E'],
    'E':['F','B'],
    'D':['B']}

levels = {}

def bfs(start):
    visited = [start]
    queue = [start]
    levels[start] = 0
    
    while queue:
        node = queue.pop(0)
 
        for current in graph[node]:
            if current not in visited:
                visited.append(current)
                queue.append(current)
                levels[current] = levels[node] + 1
    return levels

print(bfs('A'))

visited=[] 
queue=[]

def bfs (start,goal):
    visited.append(start)
    queue.append(start)

    while queue:
        node = queue.pop(0)
        print(node)
        if node == goal:
            return
        
        for current in graph[node]:
            if current not in visited:
                visited.append(current)
                queue.append(current)
                
bfs('F','A')