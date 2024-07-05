import heapq
import networkx as nx
import matplotlib.pyplot as plt
import random

def prim(graph, start):
    mst = []
    visited = set()
    min_heap = [(0, start, None)]

    while min_heap:
        weight, current_vertex, from_vertex = heapq.heappop(min_heap)

        if current_vertex in visited:
            continue

        visited.add(current_vertex)

        if from_vertex is not None:
            mst.append((from_vertex, current_vertex, weight))

        for neighbor, edge_weight in graph[current_vertex]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (edge_weight, neighbor, current_vertex))

    return mst

def draw_graph(graph, mst):
    G = nx.Graph()
    
    # Add edges to the graph
    for vertex in graph:
        for neighbor, weight in graph[vertex]:
            G.add_edge(vertex, neighbor, weight=weight)

    pos = nx.spring_layout(G)  # positions for all nodes
    edge_labels = nx.get_edge_attributes(G, 'weight')

    plt.figure(figsize=(10, 8))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=15)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')
    
    # Highlight the edges in the MST
    mst_edges = [(u, v) for u, v, w in mst]
    nx.draw_networkx_edges(G, pos, edgelist=mst_edges, edge_color='blue', width=2)

    plt.title("Árvore Geradora Mínima (MST) usando o Algoritmo de Prim")
    plt.show()

def generate_random_graph(vertices):
    graph = {vertex: [] for vertex in vertices}
    for i in range(len(vertices)):
        for j in range(i + 1, len(vertices)):
            weight = random.randint(1, 10)  # Peso aleatório entre 1 e 10
            graph[vertices[i]].append((vertices[j], weight))
            graph[vertices[j]].append((vertices[i], weight))
    return graph

# Gerar grafo aleatório com vértices de 'A' a 'E'
vertices = ['A', 'B', 'C', 'D', 'E']
random_graph = generate_random_graph(vertices)

# Exibir o grafo gerado
print("Grafo Gerado:")
for vertex in random_graph:
    print(f"{vertex}: {random_graph[vertex]}")

# Encontrar a MST usando o algoritmo de Prim
mst = prim(random_graph, 'A')

# Exibir as arestas da MST
print("\nÁrvore Geradora Mínima (MST):")
for edge in mst:
    print(f"{edge[0]} - {edge[1]}: {edge[2]}")

# Visualização
draw_graph(random_graph, mst)
