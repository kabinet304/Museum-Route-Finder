import tkinter as tk
from collections import defaultdict

# Rooms
rooms = ["PG1", "PG2", "S1G1", "S1G2", "S1G3", "S1G4", "S1G5", "S2G1", "S2G2", "S2G3", "S2G4", "S2G5", "S2G6", "S2G7"]

# Provided room connections
connections = {
    "UL1": ["PG1", "PG2", "S1G1", "S1G5", "S2G1", "S2G2", "S2G7"],
    "UL2": ["S1G2", "S1G3", "S2G3", "S2G4"],
    "UL3": ["S1G3", "S1G4", "S2G4", "S2G5", "S2G6"],
    "S1G1": ["S1G2"],
    "S1G2": ["S1G3", "S1G5"],
    "S1G3": ["S1G4"],
    "S2G1": ["S2G2"],
    "S2G2": ["S2G3"],
    "S2G3": ["S2G4"],
    "S2G4": ["S2G5"],
    "S2G5": ["S2G6"],
}
graph = defaultdict(list)
for key, values in connections.items():
    for value in values:
        graph[key].append(value)
        graph[value].append(key)


def generate_routes_excluding_subsets(graph, entrances, target_rooms):
    routes = set()
    unique_combinations = {}

    def dfs(current, path):
        if current in target_rooms:
            # Generate a key for the current path based on the rooms included, ignoring order
            path_key = frozenset(path)
            path_str = '>'.join(path)
            # Add the path to routes if it's not a subset of an existing path
            if path_key not in unique_combinations or len(path_str) > len(unique_combinations[path_key]):
                unique_combinations[path_key] = path_str
            routes.add(path_str)
        for neighbor in graph[current]:
            if neighbor not in path and neighbor in target_rooms:
                dfs(neighbor, path + [neighbor])

    for entrance in entrances:
        dfs(entrance, [entrance])

    # Filter out subsets: keep longer routes when paths include the same set of rooms
    final_routes = set(unique_combinations.values())

    # Additional filtering to remove any route that is a subset of another route
    to_remove = set()
    for route in final_routes:
        route_parts = set(route.split('>'))
        for other_route in final_routes:
            if route != other_route and route_parts.issubset(set(other_route.split('>'))):
                to_remove.add(route)

    refined_routes = final_routes - to_remove

    return sorted(refined_routes)

# Tkinter GUI
window = tk.Tk()
window.title("Route finding")

# Input frame
entrance_frame = tk.LabelFrame(window, text="Entrance")
entrance_frame.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)

entrance_options = ["UL1", "UL2", "UL3"]
entrance_vars = [tk.IntVar(value=1) for _ in entrance_options]
entrance_checkboxes = [tk.Checkbutton(entrance_frame, text=option, variable=var)
                       for option, var in zip(entrance_options, entrance_vars)]
for checkbox in entrance_checkboxes:
    checkbox.pack(side=tk.LEFT, padx=5)

# Target frame
target_frame = tk.LabelFrame(window, text="Selected galleries")
target_frame.grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)

target_options = [room for room in rooms if room not in entrance_options]
target_vars = [tk.IntVar() for _ in target_options]
target_checkboxes = [tk.Checkbutton(target_frame, text=option, variable=var)
                       for option, var in zip(target_options, target_vars)]
for checkbox in target_checkboxes:
    checkbox.pack(side=tk.LEFT, padx=5)

# Routes display area
routes_frame = tk.LabelFrame(window, text="Museum walks or routes:")  # Create LabelFrame
routes_frame.grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)

routes_label = tk.Label(routes_frame, text="Computer-generated museum walks or routes:")  # Label inside frame
routes_label.pack(pady=5)  # Some spacing

routes_text = tk.Text(routes_frame, width=126, height=10, font=("Arial", 18), wrap=tk.WORD)
routes_text.pack()  # Directly pack inside frame

def get_selected_entrances():
    """Function that retrieves selected starting locations."""
    selected_entrances = []
    for option, var in zip(entrance_options, entrance_vars):
        if var.get():
            selected_entrances.append(option)
    return selected_entrances

# Function for finding routes
def get_selected_targets():
    selected_targets = []
    for option, var in zip(target_options, target_vars):
        if var.get():
            selected_targets.append(option)
    return selected_targets

def find_routes():
    selected_entrances = get_selected_entrances()
    selected_targets = get_selected_targets()
    routes = generate_routes_excluding_subsets(graph, selected_entrances, selected_targets)

    routes_text.delete('1.0', tk.END)  # Clear previous results
    if routes:
        routes_text.insert(tk.END, "Computer-generated museum walks or routes:\n")
        for route in routes:
            routes_text.insert(tk.END, f"- {route}\n")
    else:
        routes_text.insert(tk.END, "No route found for the given rooms.\n")

# Button
btn_find_routes = tk.Button(window, text="Find routes", command=find_routes)
btn_find_routes.grid(row=2, column=2)

window.mainloop()
