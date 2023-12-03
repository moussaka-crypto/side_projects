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

bulgaria = Graph(['CB', 'CO', 'PB', 'B', 'A', 'P', 'CT', 'EH',
                 'CH', 'TX', 'H', 'PK', 'Y', 'X', 'E',
                 'BT', 'EB', 'BP', 'KH', 'PA', 'M'],
                [
                    ('CB', 'CO', 70),
                    ('CB', 'B', 200),
                    ('CB', 'A', 250),
                    ('PB', 'B', 180),
                    ('PB', 'CT', 50),
                    ('B', 'P', 300),
                    ('B', 'TX', 120),
                    ('A', 'PB', 120),
                    ('A', 'CT', 90),
                    ('P', 'B', 250),
                    ('P', 'BT', 130),
                    ('CT', 'PB', 40),
                    ('CT', 'A', 60),
                    ('EH', 'P', 180),
                    ('CH', 'CT', 70),
                    ('TX', 'B', 80),
                    ('H', 'B', 100),
                    ('PK', 'CB', 30),
                    ('Y', 'A', 110),
                    ('X', 'PB', 120),
                    ('E', 'CB', 80),
                    ('BT', 'P', 100),
                    ('EB', 'CT', 60),
                    ('BP', 'CB', 50),
                    ('KH', 'CB', 70),
                    ('PA', 'PB', 90),
                    ('M', 'BP', 40)
                ])

def reverse_path(action_sequence, start, goal):
    filtered_path = []
    reverse_start = goal
  
    while reverse_start != start:
        filtered_path.extend(action for action in action_sequence if action.end.name == reverse_start)
        reverse_start = filtered_path[-1].start.name if filtered_path else start

    return filtered_path[::-1]

"""
Uninformed Search Algorithms
g: graph
start: star node
goal: end node
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


def ucs(g, start, goal):
    node = getNode(start, g.nodes)
    path = []

    if goal == node.name:
        return path

    pq = MiQueue()
    pq.pq_enqueue(node)
    visited = []

    while pq.items:
        node = pq.dequeue()

        if node.name == goal:
            return reverse_path(path, start, goal)

        visited.append(node)  # mark as visited

        for edge in node.edges:  # determine child nodes
            child = getNode(edge.end.name, g.nodes)

            if child.parent == 0:
                child.parent = edge.start.name

            current_path = edge.value + getNode(edge.start.name, g.nodes).value

            # child is neither visited nor in queue
            if child not in visited and getNode(child.name, pq.items) == -1:
                child.value = current_path
                pq.pq_enqueue(child)
                path.append(edge)
            # child is in queue but with higher path cost
            elif getNode(child.name, pq.items) != -1 and current_path < child.value:
                pq.items.remove(child)

                for step in path:
                    if child.name == step.start.name:
                        path.remove(step)

                child.parent = edge.start.name
                child.value = current_path
                pq.pq_enqueue(child)
                path.append(edge)
    return -1


if __name__ == '__main__':
    
    # path and travelling costs from Bucharest to Timisoara
    total_cost = 0
    path = bfs(romania, "Bu", "Ti")
    for action in path:
        total_cost += action.value
        print(action.start.name, "->", action.end.name, action.value)
    print("BFS Traversal Cost: ", total_cost, '\n')

    total_cost = 0
    path = dfs(romania, "Bu", "Ti")
    for action in path:
        total_cost += action.value
        print(action.start.name, "->", action.end.name, action.value)
    print("DFS Traversal Cost: ", total_cost, '\n')

    total_cost = 0
    path = ucs(romania, "Bu", "Ti")
    for action in path:
        total_cost += action.value
        print(action.start.name, "->", action.end.name, action.value)
    print("UCS Traversal Cost: ", total_cost)
