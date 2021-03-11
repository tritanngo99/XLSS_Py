from datetime import datetime
import numba
import random
INF = 9999999
# number of vertices in graph
V = 500
# create a 2d array of size 5x5
# for adjacency matrix to represent graph
G = [[0 for _ in range(0,V)] for _ in range(0,V)]
for i in range(0, V):
    for j in range(0, V):
        if i == j:
            G[i][i] = 0
        else:
            G[i][j] = G[j][i] = random.randint(1,100)
selected = [False]*V
no_edge = 0
selected[0] = True
start = datetime.now()
while (no_edge < V - 1):
    minimum = INF
    x = 0
    y = 0
    for i in range(V):
        if selected[i]:
            for j in range(V):
                if ((not selected[j]) and G[i][j]):
                    if minimum > G[i][j]:
                        minimum = G[i][j]
                        x = i
                        y = j
    selected[y] = True
    no_edge += 1
end = datetime.now()

print("Time: ", end-start)