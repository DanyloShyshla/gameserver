import heapq

inf = float('inf')
nodes_list = []

with open('gamsrv.in', 'r') as input:
    nodes, edges = map(int, input.readline().split())
    graph = [[] for i in range(edges)]
    for node in range(nodes):
        graph.append([])

    clients = list(map(lambda x: int(x), input.readline().split()))

    for edge in range(edges):
        startnode, endnode, latency = map(int, input.readline().split())
        graph[startnode].append((endnode, latency))
        graph[endnode].append((startnode, latency))

max_value = inf
for n in range(1, nodes + 1):
    nodes_list.append(n)
servers = set(nodes_list) - set(clients)
print('Probable servers : ', servers)

for server in servers:
    start_vertex = server
    min_edge = [inf] * (edges + 1)

    heap = []
    heapq.heappush(heap, (0, start_vertex))
    heapq.heapify(heap)
    min_edge[start_vertex] = 0

    while len(heap) > 0:
        min_vertex = heapq.heappop(heap)[1]
        heapq.heapify(heap)

        for vertex, weight in graph[min_vertex]:

            if min_edge[vertex] >= min_edge[min_vertex] + weight:
                min_edge[vertex] = min_edge[min_vertex] + weight
                heapq.heappush(heap, (min_edge[vertex], vertex))
    min_edge.remove(inf)
    if max_value > max(min_edge):
        max_value = max(min_edge)
print('Minimal delay value : ', max_value)

with open('gamsrv.out', 'w+') as output:
    output.write(str(max_value))
