import random
from datetime import datetime

from numpy.core.arrayprint import DatetimeFormat
# The number of vertices





# Algorithm implementation
def floyd_warshall():
    V = 500
    G = [[0 for _ in range(0,V)] for _ in range(0,V)]
    for i in range(0, V):
        for j in range(0, V):
            if i == j:
                G[i][i] = 0
            else:
                G[i][j] = G[j][i] = random.randint(1,100)
    distance = list(map(lambda i: list(map(lambda j: j, i)), G))
    for k in range(V):
        for i in range(V):
            for j in range(V):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])


# Printing the solution
# def print_solution(distance):
#     for i in range(nV):
#         for j in range(nV):
#             if(distance[i][j] == INF):
#                 print("INF", end=" ")
#             else:
#                 print(distance[i][j], end="  ")
#         print(" ")

start = datetime.now()

floyd_warshall()

end = datetime.now()
print("Time: ", end - start)