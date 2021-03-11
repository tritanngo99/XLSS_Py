from datetime import datetime
from numba import jit
import random

# create a 2d array of size 5x5
# for adjacency matrix to represent graph



@jit(nopython=True)
def prim():
    INF = 9999999
    # number of vertices in graph
    V = 500
    G = [[0 for _ in range(0,V)] for _ in range(0,V)]
    for i in range(0, V):
        for j in range(0, V):
            if i == j:
                G[i][i] = 0
            else:
                G[i][j] = G[j][i] = random.randint(1,100)
    selected = [False]*V
    selected[0] = True
    no_edge = 0
    while (no_edge < V - 1):
        minimum = INF
        x = 0
        y = 0
        for i in range(V):
            if selected[i]:
                for j in range(V):
                    if ((not selected[j]) and G[i][j]):  
                        # not in selected and there is an edge
                        if minimum > G[i][j]:
                            minimum = G[i][j]
                            x = i
                            y = j
        # print(str(x) + "-" + str(y) + ":" + str(G[x][y]))
        selected[y] = True
        no_edge += 1
start = datetime.now()  
prim()

end = datetime.now()
print("Time: ", end-start)