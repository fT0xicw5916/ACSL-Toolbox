"""
Generates a max heap from given command line input.
"""

from graphviz import Digraph
import sys


class HeapNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent: HeapNode | None = None


def insert_heap(root, node: HeapNode, nodes_list: list[HeapNode]):
    nodes_list.append(node)
    if len(nodes_list) == 1:
        return node
    
    parent_index = (len(nodes_list) - 2) // 2
    parent = nodes_list[parent_index]
    node.parent = parent
    if not parent.left:
        parent.left = node
    else:
        parent.right = node

    current = node
    while current.parent and current.value > current.parent.value:
        current.value, current.parent.value = current.parent.value, current.value
        current = current.parent

    return root


def add_nodes_edges(graph: Digraph, node: HeapNode):
    if node is None:
        return
    node_id = str(id(node))
    graph.node(node_id, label=str(node.value))
    if node.left:
        graph.edge(node_id, str(id(node.left)))
        add_nodes_edges(graph, node.left)
    if node.right:
        graph.edge(node_id, str(id(node.right)))
        add_nodes_edges(graph, node.right)


def main():
    if len(sys.argv) < 2:
        print("Generates a max heap from given command line input")
        print("    Usage: python max_heap.py \"<keys_separated_by_space>\"")
        print("    e.g. python max_heap.py \"1 2 3 4 5 6 7 8 9\"")
        return
    
    root = None
    nodes_list = []
    for key in [int(i) for i in sys.argv[1].split()]:
        node = HeapNode(key)
        root = insert_heap(root, node, nodes_list)
        
    graph = Digraph(format="png")
    graph.attr("node", shape="circle", style="filled", color="lightblue")
    
    add_nodes_edges(graph, root)
    graph.render("max_heap", view=True)


if __name__ == "__main__":
    main()
