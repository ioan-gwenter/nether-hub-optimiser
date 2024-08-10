import matplotlib.pyplot as plt

def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def closest_point(reference, points):
    """Find the closest point to the reference from a list of points."""
    return min(points, key=lambda p: manhattan_distance(reference, p[0]))

def build_branching_paths(hub, portals):
    paths = []
    connected_portals = [(hub, 'Hub')] 
    
    while portals:
        best_dist = float('inf')
        best_path = None
        best_portal = None
        
        for portal in portals:
            for connected, _ in connected_portals:  # Only use the coordinates part of the connected portals
                path = axis_aligned_path(connected, portal[0]) 
                path_distance = sum(manhattan_distance(p1, p2) for p1, p2 in path)
                
                if path_distance < best_dist:
                    best_dist = path_distance
                    best_path = path
                    best_portal = portal
        
        # Add the best path to the paths list
        paths.extend(best_path)
        connected_portals.append(best_portal) 
        portals.remove(best_portal)
    
    return paths, connected_portals

def axis_aligned_path(p1, p2):
    """Generate an axis-aligned path between two points p1 and p2."""
    return [(p1, (p2[0], p1[1])), ((p2[0], p1[1]), p2)]

def plot_paths(hub, portals, paths):
    fig, ax = plt.subplots()
    
    # hub
    ax.plot(hub[0], hub[1], 'go', label='Hub') 
    
    # paths
    for path in paths:
        x_values = [path[0][0], path[1][0]]
        z_values = [path[0][1], path[1][1]]
        ax.plot(x_values, z_values, 'b-')
    
    # portals and labels
    for portal, label in portals[1:]:  
        ax.plot(portal[0], portal[1], 'ro')
        ax.text(portal[0] + 1, portal[1] + 1, f'{label} ({portal[0]}, {portal[1]})', fontsize=9, color='black')

    ax.set_xlabel('X Coordinate')
    ax.set_ylabel('Z Coordinate')
    ax.set_title('Optimized Nether Highway Layout')
    ax.legend()
    plt.grid(True)
    plt.show()

# Example portal coordinates (X, Z) with labels

hub = (42,22) 

portals = [
    ((359, -220), "IOAN MAIN"),
    ((97, 267), "OLD CRAVENDALE"),
    ((-119, 85), "HOBBIT HOLE"),
    ((-125, 15), "SHIT MANSION"),
    ((-209, 1), "CATHEDRAL"),
    ((-193, 30), "WHEAT FARM"),
    ((-221, -42), "NORDPACK JUNCTION"),
    ((210, 288), "SLIME FARM"),
    ((119, -180), "COCK n'BALLS BASE"),
    ((52, 268), "GEORGE HOUSE"),
    ((240, -66), "END PORTAL"),
    
]

# Compute the axis-aligned highway paths with branching
paths, connected_portals = build_branching_paths(hub, portals.copy())

# Plot
plot_paths(hub, connected_portals, paths)
