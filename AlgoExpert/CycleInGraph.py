# 0(v + e) time | 0(v) space where v is the number of
# vertices and e is the number of edges in the graph
def cycleInGraph1(edges):
    numberofNodes = len(edges)
    visited = [False for _ in range(numberofNodes)]
    currentlyInStack = [False for _ in range(numberofNodes)]

    for node in range(numberofNodes):
        if visited[node]:
            continue
        
        containesCycle = isNodeInCycle1(edges, node, visited, currentlyInStack)

        if containesCycle:
            return True

    return False

def isNodeInCycle1(edges, node, visited, currentlyInStack):
    visited[node] = True
    currentlyInStack[node] = True

    neighbors = edges[node]

    for neighbor in neighbors:
        if not visited[neighbor]:
            containesCycle = isNodeInCycle1(edges, neighbor, visited, currentlyInStack)
            
            if containesCycle:
                return True
            
        elif currentlyInStack[neighbor]:
            return True

    currentlyInStack[node] = False
    
    return False



# 0(v + e) time | 0(v) space where v is the number of

WHITE, GREY, BLACK = 0, 1, 2

def cycleInGraph2(edges):
    numberofNodes = len(edges)
    colors = [WHITE for _ in range(numberofNodes)]

    for node in colors:
        if colors[node] != WHITE:
            continue
        
        containesCycle = TraversAndColorNode2(node, edges, colors)
        if containesCycle:
            return True
    return False


def TraversAndColorNode2(node, edges, colors):
    colors[node] = GREY
    neighbors = edges[node]

    for neighbor in neighbors:
        neighborColor = colors[neighbor]

        if neighborColor == GREY:
            return True
        if neighborColor != WHITE:
            continue
        containesCycle = TraversAndColorNode2(neighbor, edges, colors)

        if containesCycle:
            return True

    colors[node] = BLACK
    return False




edges = [
  [1, 3],
  [2, 3, 4],
  [0],
  [],
  [2, 5],
  [],
]

print(cycleInGraph1(edges))
print(cycleInGraph2(edges))

# Test Case 1
# {
#   "edges": [
#     [1, 3],
#     [2, 3, 4],
#     [0],
#     [],
#     [2, 5],
#     []
#   ]
# }
# Test Case 2
# {
#   "edges": [
#     [1, 2],
#     [2],
#     []
#   ]
# }
# Test Case 3
# {
#   "edges": [
#     [1, 2],
#     [2],
#     [1]
#   ]
# }
# Test Case 4
# {
#   "edges": [
#     [1, 2],
#     [2],
#     [1, 3],
#     [3]
#   ]
# }
# Test Case 5
# {
#   "edges": [
#     [],
#     [0, 2],
#     [0, 3],
#     [0, 4],
#     [0, 5],
#     [0]
#   ]
# }
# Test Case 6
# {
#   "edges": [
#     [0]
#   ]
# }
# Test Case 7
# {
#   "edges": [
#     [8],
#     [0, 2],
#     [0, 3],
#     [0, 4],
#     [0, 5],
#     [0],
#     [7],
#     [8],
#     [6]
#   ]
# }
# Test Case 8
# {
#   "edges": [
#     [1],
#     [2, 3, 4, 5, 6, 7],
#     [],
#     [2, 7],
#     [5],
#     [],
#     [4],
#     []
#   ]
# }
# Test Case 9
# {
#   "edges": [
#     [1],
#     [2, 3, 4, 5, 6, 7],
#     [],
#     [2, 7],
#     [5],
#     [],
#     [4],
#     [0]
#   ]
# }
# Test Case 10
# {
#   "edges": [
#     [0],
#     [1]
#   ]
# }
# Test Case 11
# {
#   "edges": [
#     [1, 2],
#     [2],
#     []
#   ]
# }
# Test Case 12
# {
#   "edges": [
#     [],
#     [0, 3],
#     [0],
#     [1, 2]
#   ]
# }
