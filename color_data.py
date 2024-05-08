import math

# A KNN approach to attempt to solve the lack of accuracy in the color sensor. A better set of data points can achieve
# higher accuracy in comparisson to the present set of points.

class COLORS():
    YELLOW  = 0
    RED     = 1
    BLUE    = 2
    GREEN   = 3
    AIR     = 4

yellow  = [[53, 31, 21],[53, 31, 21],[45, 26, 16],[57, 34, 23],[58, 33, 23],[59, 34, 18],[58, 33, 18],[59, 36, 20],[60, 36, 20],[57, 31, 17],[50, 26, 11],[50, 27, 7],[53, 30, 10],[5, 1, 0],[6, 1, 0],[7, 2, 0],[37, 23, 13],[36, 23, 12],[34, 21, 11],[41, 26, 14]]
red     = [[43, 7, 11],[43, 7, 10],[43, 7, 9],[43, 8, 10],[26, 4, 7],[41, 7, 11],[40, 5, 7],[43, 8, 10],[40, 7, 11],[37, 6, 10],[38, 3, 16],[39, 3, 17],[33, 3, 9],[30, 2, 8],[32, 2, 8],[33, 3, 10],[36, 3, 13],[39, 4, 15],[40, 4, 17],[40, 3, 17]]
blue    = [[3, 10, 53],[4, 12, 62],[3, 10, 52],[2, 6, 39],[2, 6, 38],[2, 5, 36],[2, 5, 35],[2, 6, 41],[4, 11, 60],[4, 10, 56],[3, 10, 58],[4, 11, 59],[4, 11, 59],[4, 11, 59],[3, 9, 52],[3, 9, 52],[3, 9, 52],[3, 8, 50],[3, 9, 51],[3, 9, 50]]
green   = [[4, 21, 15],[5, 25, 19],[7, 29, 25],[7, 30, 25],[2, 12, 10],[2, 12, 10],[2, 13, 11],[2, 12, 10],[2, 10, 8],[3, 15, 13],[6, 27, 27],[4, 19, 18],[4, 18, 17],[4, 20, 19],[7, 29, 32],[7, 30, 30],[7, 30, 30],[7, 29, 30],[5, 23, 23],[5, 19, 19]]
air     = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]

points  = [yellow, red, blue, green, air]
group_names = [COLORS.YELLOW, COLORS.RED, COLORS.BLUE, COLORS.GREEN, COLORS.AIR]
group_str = ["YELLOW", "RED", "BLUE", "GREEN", "AIR"]

def ClassifyColor(p, k = 3):
    distances = []
    for i in range(len(points)):
        group = points[i]
        for _color in group:
            euclid_dist = math.sqrt((_color[0] - p[0])**2 + (_color[1] - p[1])**2 + (_color[2] - p[2])**2)
            distances.append((euclid_dist, i))
    
    distances = sorted(distances)[:k]
    freq = [0, 0, 0, 0, 0]
    for dist in distances:
        freq[dist[1]] += 1
    
    print(group_str[freq.index(max(freq))])
    return group_names[freq.index(max(freq))]
