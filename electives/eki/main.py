from graph import *
from queue import Queue

romania = Graph(['Or', 'Ne', 'Ze', 'Ia', 'Ar', 'Si', 'Fa',
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
                ])


def dfs(problem, initial, goal):
    node = getNode(initial, problem.nodes)

    solution = []
    if goal == node.name:
        return solution

    frontier = Queue()
    frontier.enqueue(node)
    explored = []

    while not frontier.is_empty():
        node = frontier.pop()
        explored.append(node)

        for action in node.edges:
            child = getNode(action.end.name, problem.nodes)
            if child not in (explored or frontier):
                solution.append(action)

                if goal == child.name:
                    return solution_filter(solution, initial, goal)
                frontier.enqueue(child)

    return "failure"


def bfs(problem, initial, goal):
    node = getNode(initial, problem.nodes)

    solution = []
    if goal == node.name:
        return solution

    frontier = Queue()
    frontier.enqueue(node)
    explored = []

    while frontier.elements:
        node = frontier.dequeue()
        explored.append(node)

        for edge in node.edges:
            child = getNode(edge.end.name, problem.nodes)
            child.parent = edge.start.name

            if child not in explored and getNode(child.name, frontier.elements) == -1:  # child is not in explored
                # and queue
                solution.append(edge)

                if child.name == goal:
                    return solution_filter(solution, initial, goal)
                frontier.enqueue(child)
    return "failure"


def solution_filter(action_seq, start, goal):
    filtered_solution = []
    find_start = goal
    while find_start != start:
        for action in action_seq:
            if action.end.name == find_start:
                find_start = action.start.name
                filtered_solution.append(action)

    return reversed(filtered_solution)


def ucs(problem, initial, goal):
    node = getNode(initial, problem.nodes)

    solution = []
    if goal == node.name:
        return solution

    frontier = Queue()
    frontier.prio_enqueue(node)
    explored = []

    while frontier.elements:
        node = frontier.dequeue()

        if node.name == goal:  # goal test
            return solution_filter(solution, initial, goal)

        explored.append(node)  # add node to explored

        for edge in node.edges:  # view possible action
            child = getNode(edge.end.name, problem.nodes)

            if child.parent == 0:
                child.parent = edge.start.name

            current_path = edge.value + getNode(edge.start.name, problem.nodes).value

            if child not in explored and getNode(child.name, frontier.elements) == -1:
                child.value = current_path
                frontier.prio_enqueue(child)
                solution.append(edge)
            elif getNode(child.name, frontier.elements) != -1 and current_path < child.value:
                frontier.elements.remove(child)

                for action in solution:
                    if child.name == action.start.name:
                        solution.remove(action)

                child.parent = edge.start.name
                child.value = current_path
                frontier.prio_enqueue(child)
                solution.append(edge)
    return "failure"
print()

total_cost = 0
for action in dfs(romania, "Bu", "Ti"):
    total_cost += action.value
    print(action.start.name, action.end.name, action.value)
print("----------- TOTAL COST (DFS) = ", total_cost)
print()

total_cost = 0
for action in bfs(romania, "Bu", "Ti"):
    total_cost += action.value
    print(action.start.name, action.end.name, action.value)
print("----------- TOTAL COST (BFS)= ", total_cost)
print()

total_cost = 0
for action in ucs(romania, "Bu", "Ti"):
    total_cost += action.value
    print(action.start.name, action.end.name, action.value)
print("----------- TOTAL COST (UCS)= ", total_cost)
print()
