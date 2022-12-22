

GRAPH = {
    'A': {'B': 11, 'C': 14, 'D': 7},
    'B': {'A': 11, 'E': 15},
    'C': {'A': 14, 'E': 8, 'F' : 10},
    'D': {'A': 7, 'F': 25},
    'E': {'B': 15, 'H': 9, 'C' : 8},
    'F': {'D': 25, 'G': 20},
    'G': {'H': 10, 'F': 20},
    'H': {'E': 9, 'G': 10},
    
}


def bestfirst(source, destination):

    straight_line = {
        'A': 40,
        'B': 32,
        'C': 25,
        'D': 35,
        'E': 19,
        'F': 17,
        'G': 0,
        'H': 10,
    }
    from queue import PriorityQueue
    priority_queue, visited = PriorityQueue(), {}
    priority_queue.put((straight_line[source], 0, source, [source]))
    visited[source] = straight_line[source]
    while not priority_queue.empty():
        (heuristic, cost, vertex, path) = priority_queue.get()
        if vertex == destination:
            return heuristic, cost, path
        for next_node in GRAPH[vertex].keys():
            current_cost = cost + GRAPH[vertex][next_node]
            heuristic = straight_line[next_node]
            if not next_node in visited or visited[next_node] >= heuristic:
                visited[next_node] = heuristic
                priority_queue.put(
                    (heuristic, current_cost, next_node, path + [next_node]))


def main():
    print('ENTER SOURCE :', end=' ')
    source = input().strip()
    print('ENTER GOAL :', end=' ')
    goal = input().strip()
    if source not in GRAPH or goal not in GRAPH:
        print('ERROR: NODE DOES NOT EXIST.')
    else:
        print('\nBFS PATH:')
        heuristic, cost, optimal_path = bestfirst(source, goal)
        print('PATH COST =', cost)
        print(' -> '.join(city for city in optimal_path))


if __name__ == '__main__':
    main()


# // Pseudocode for Best First Search
# Best-First-Search(Graph g, Node start)
#     1) Create an empty PriorityQueue
#        PriorityQueue pq;
#     2) Insert "start" in pq.
#        pq.insert(start)
#     3) Until PriorityQueue is empty
#           u = PriorityQueue.DeleteMin
#           If u is the goal
#              Exit
#           Else
#              Foreach neighbor v of u
#                 If v "Unvisited"
#                     Mark v "Visited"                    
#                     pq.insert(v)
#              Mark u "Examined"                    
# End procedure


# let open be a priority queue containing initial node

# Loop
#     if open is empty return faliour
#         node <- remove - first(open)
#     if node is goal state 
#         then return __path__
#     else generate all succssor of node and put newly generated node into open
#     acc to h Value
# END LOOP 
    