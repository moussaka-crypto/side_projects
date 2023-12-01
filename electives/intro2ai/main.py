from graph import *
from miqueue import MiQueue

romania = Graph( ['Or', 'Ne', 'Ze', 'Ia', 'Ar', 'Si', 'Fa',
 'Va', 'Ri', 'Ti', 'Lu', 'Pi', 'Ur', 'Hi',
 'Me', 'Bu', 'Dr', 'Ef', 'Cr', 'Gi'],
[
   ('Or', 'Ze', 71), ('Or', 'Si', 151),
   ('Ne', 'Ia', 87), ('Ze', 'Ar', 75),
   ('Ia', 'Va', 92), ('Ar', 'Si', 140),
   ('Ar', 'Ti', 118), ('Si', 'Fa', 99),
   ('Si', 'Ri', 80), ('Fa', 'Bu', 211),
   ('Va', 'Ur', 142), ('Ri', 'Pi', 97),
   ('Ri', 'Cr', 146), ('Ti', 'Lu', 111),
   ('Lu', 'Me', 70), ('Me', 'Dr', 75),
   ('Dr', 'Cr', 120), ('Cr', 'Pi', 138),
   ('Pi', 'Bu', 101), ('Bu', 'Gi', 90),
   ('Bu', 'Ur', 85), ('Ur', 'Hi', 98),
   ('Hi', 'Ef', 86)
] )

def reverse_path(action_sequence, start, goal):
    filtered_solution = []
    reverse_start = goal
  
    while reverse_start != start:
        filtered_solution.extend(action for action in action_sequence if action.end.name == reverse_start)
        reverse_start = filtered_solution[-1].start.name if filtered_solution else start

    return filtered_solution[::-1]

"""
g: graph
start: starting node
goal: ending node
"""
def bfs(g, start, goal):
    node = getNode(start, g.nodes)
    path = []
  
    if goal == node.name:
        return path

    queue = MiQueue()
    queue.enqueue(node)
    visited = []

    while queue.items:
        node = queue.dequeue()
        visited.append(node)

        for edge in node.edges:
            child = getNode(edge.end.name, g.nodes)
            child.parent = edge.start.name
            
            # child is neither visited nor in queue
            if child not in visited and getNode(child.name, queue.items) == -1:
                path.append(edge)

                if child.name == goal:
                    return reverse_path(path, start, goal)
                queue.enqueue(child)
    return -1

def dfs(g, start, goal):
    node = getNode(start, g.nodes)
    path = []
  
    if goal == node.name:
        return path

    stack = MiQueue()
    stack.push(node)
    visited = []

    while stack:
        node = stack.pop()
        visited.append(node)

        for edge in node.edges:
            child = getNode(edge.end.name, g.nodes)
            child.parent = edge.start.name
            
            # child is neither visited nor in queue
            if child not in visited and getNode(child.name, stack.items) == -1:
                path.append(edge)

                if child.name == goal:
                    return reverse_path(path, start, goal)
                stack.push(child)
    return -1

if __name__ == '__main__':
    
    # path and travelling costs from Bucharest to Timisoara
    total_costs = 0
    path = bfs(romania, "Bu", "Ti")
    for action in path:
        total_costs += action.value
        print(action.start.name, "->", action.end.name, action.value)
    print("BFS Traversal Cost: ", total_costs, '\n')

    total_costs = 0
    path = dfs(romania, "Bu", "Ti")
    for action in path:
        total_costs += action.value
        print(action.start.name, "->", action.end.name, action.value)
    print("DFS Traversal Cost: ", total_costs, '\n')
