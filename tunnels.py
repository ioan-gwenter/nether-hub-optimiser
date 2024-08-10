import matplotlib.pyplot as plt
from collections import defaultdict

# plot the highway and portals on the map
def plot_highways(hub, highways, portals):
    plt.figure(figsize=(10, 10))

    # hub
    plt.scatter(*hub, color='red', s=100, label='Hub')

    # portals
    for name, (x, z) in portals.items():
        plt.scatter(x, z, s=50)
        plt.text(x + 0.5, z + 0.5, name, fontsize=9)

    # highways
    for start, end in highways:
        plt.plot([start[0], end[0]], [start[1], end[1]], color='blue')

    plt.xlabel("X Coordinate")
    plt.ylabel("Z Coordinate")
    plt.title("Nether Highway System")
    plt.legend()
    plt.grid(True)
    plt.show()

# create main highways and sub-highways
def create_highways(hub, portals):
    sorted_portals = sorted(portals.items(), key=lambda item: (item[1][0] - hub[0])**2 + (item[1][1] - hub[1])**2)
    
    highways = []
    sub_highways = defaultdict(list)
    axis_lines = defaultdict(list)

    # main highways in cardinal directions
    for name, (x, z) in sorted_portals:
        if abs(x - hub[0]) > abs(z - hub[1]):
            axis_lines['X'].append((x, z))
        else:
            axis_lines['Z'].append((x, z))

    # main highways
    for axis, points in axis_lines.items():
        if axis == 'X':
            points = sorted(points, key=lambda p: p[0])
        else:
            points = sorted(points, key=lambda p: p[1])

        prev_point = hub
        for point in points:
            if axis == 'X':
                highways.append(((prev_point[0], prev_point[1]), (point[0], prev_point[1])))
                prev_point = (point[0], prev_point[1])
            else:
                highways.append(((prev_point[0], prev_point[1]), (prev_point[0], point[1])))
                prev_point = (prev_point[0], point[1])

            sub_highways[axis].append(point)

    # sub-highways from main highways
    for axis, points in sub_highways.items():
        if axis == 'X':
            for x, z in points:
                highways.append(((x, hub[1]), (x, z)))
        else:
            for x, z in points:
                highways.append(((hub[0], z), (x, z)))

    return highways

hub = (42, 22)
portals = {
    "IOAN MAIN": (359, -220),
    "OLD CRAVENDALE": (97, 267),
    "HOBBIT HOLE": (-119, 85),
    "MANSION": (-125, 15),
    "CATHEDRAL": (-209, 1),
    "WHEAT FARM": (-193, 30),
    "NORDPACK JUNCTION": (-221, -42),
    "SLIME FARM": (210, 288),
    "BALLS BASE": (119, -180),
    "GEORGE HOUSE": (52, 268),
    "END PORTAL": (240, -66),
}

highways = create_highways(hub, portals)

plot_highways(hub, highways, portals)
