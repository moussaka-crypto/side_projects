from collections import Counter

def read_file(filename):
    with open(filename, 'r') as file:
        return file.readlines()

"""
Eine Liste der Koordinaten wird als String in `coordinates` gespeichert.
Dann werden die Informationen in der Liste weiter aufgesplittet, in float umgewandelt
und als Liste von Tupeln zurückgegeben.
"""
def parse(line):
    coordinates = line.strip().split('->')
    return [tuple(map(float, point.split(','))) for point in coordinates]

"""
Generiert eine Liste von Punkten, die von `start` bis `end` gehen.
Es werden nur Linien berücksichtigt für welche folgende Bedingung erfüllt ist:
x1 = x2 oder y1 = y2

Es wird eine Liste von Punkten mit einem konstanten Wert (start[0] bei X und start[1] bei Y) generiert.
Der variable Wert variiert von dem Minimum bis zum Maximum von start[1] und end[1] für X, 
analog mit start[0] und end[0] für Y.
"""
def generate_points(start, end):
    # when vertical
    if start[0] == end[0]:
        return [(start[0], y) for y in range(int(min(start[1], end[1])), int(max(start[1], end[1])) + 1)]
    # when horizontal
    elif start[1] == end[1]:
        return [(x, start[1]) for x in range(int(min(start[0], end[0])), int(max(start[0], end[0])) + 1)]
    
    return []

def count_points_in_lines(data):
    point_count = Counter()
    for line in data:
        start, end = parse(line)
        points = generate_points(start, end)
        point_count.update(points)

    return sum(matched_lines for count in point_count.values() if (matched_lines := count >= 2))

if __name__ == "__main__":
    test = "./test.txt"
    test_data = read_file(test)
    test_res = count_points_in_lines(test_data)

    file = "./input.txt"
    data = read_file(file)
    res = count_points_in_lines(data)
    print("Test: {}\nInput: {}".format(test_res, res))
