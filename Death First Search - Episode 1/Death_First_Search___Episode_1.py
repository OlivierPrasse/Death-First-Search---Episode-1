import sys
import math

# n: the total number of nodes in the level, including the gateways
# l: the number of links
# e: the number of exit gateways
n, l, e = [int(i) for i in input().split()]

graph = {i: [] for i in range(n)}

for i in range(l):
    # n1: N1 and N2 defines a link between these nodes
    n1, n2 = [int(j) for j in input().split()]
    graph[n1].append(n2)
    graph[n2].append(n1)

gateways = []
for i in range(e):
    ei = int(input())  # the index of a gateway node
    gateways.append(ei)

# game loop
while True:
    si = int(input())  # The index of the node on which the Bobnet agent is positioned this turn
    node_to_cut_1 = -1
    node_to_cut_2 = -1

    danger_immediat = False

    for voisin in graph[si]:
       
        if voisin in gateways:
            node_to_cut_1 = si
            node_to_cut_2 = voisin
            danger_immediat = True
            break
    

    if not danger_immediat:
        
        for gateway in gateways:
            if len(graph[gateway]) > 0:
                node_to_cut_1 = gateway
                node_to_cut_2 = graph[gateway][0]
                break

    print(f"{node_to_cut_1} {node_to_cut_2}")
    
    if node_to_cut_2 in graph[node_to_cut_1]:
        graph[node_to_cut_1].remove(node_to_cut_2)
    if node_to_cut_1 in graph[node_to_cut_2]:
        graph[node_to_cut_2].remove(node_to_cut_1)

