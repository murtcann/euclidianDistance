import math

points = [(1, 2),(3, 4)]
def euclidianDistance(point1,point2):
    x = math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)
    return x

distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclidianDistance(points[i], points[j])
        distances.append(distance)

min_distance = distances[0]
for k in range(len(distances)):
    if min_distance > distances[k]:
        min_distance = distances[k]
print(min_distance)
