"""
Find and normalize simple cycles in directed or undirected graphs.
"""

def find_cycles(graph: dict[int, list[int]]):
    all_cycles = []
    for start_node in graph:
        stack = [(start_node, [start_node])]
        while stack:
            current_node, path = stack.pop()
            for neighbor in graph.get(current_node, []):
                if neighbor == start_node and len(path) > 1:
                    cycle = path + [neighbor]
                    all_cycles.append(cycle)
                elif neighbor not in path:
                    stack.append((neighbor, path + [neighbor]))
    return all_cycles


def normalize_cycles(cycles: list[list[int]]):
    unique_cycles_set = set()
    for cycle in cycles:
        min_node = min(cycle[:-1])
        min_node_index = cycle.index(min_node)
        normalized_cycle_path = cycle[min_node_index:-1] + cycle[:min_node_index]
        normalized_cycle = normalized_cycle_path + [normalized_cycle_path[0]]
        unique_cycles_set.add(tuple(normalized_cycle))
    return [list(c) for c in unique_cycles_set]


def main():
    print("Find and normalize simple cycles in directed or undirected graphs")
    print("    Usage: Set the `graph` variable in main() as the target graph, then run `python cycles.py`.")
    print(r"    e.g. graph = {1: [2, 3], 2: [1], 3: [1]}; `$ python cycles.py`")
    
    graph = {1: [3, 5, 7], 2: [3, 6], 3: [2, 4, 6], 4: [], 5: [3, 6], 6: [2, 5, 7], 7: [1, 2, 4, 6]}
    all_cycles = find_cycles(graph)
    unique_cycles = normalize_cycles(all_cycles)

    print("\nTotal number of cycles:", len(all_cycles))
    print("All cycles:", all_cycles)
    print("\nTotal number of unique cycles:", len(unique_cycles))
    print("Unique cycles:", unique_cycles)


if __name__ == "__main__":
    main()
