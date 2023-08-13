graph = {5 : [3, 7], 3 : [2, 4], 7 : [8], 2 : [], 4 : [8], 8 : []}

visited = []

def dfs(node):
    if node not in visited:
        print(node)
        visited.append(node)
        
        for current in graph[node]:
            dfs(current)

dfs(5)