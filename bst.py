"""
Generate binary search trees (BSTs) based on input keys from command line.
"""

from graphviz import Digraph
import sys
from typing import Any


class Node:
    def __init__(self, key: Any):
        self.left: Node | None = None
        self.right: Node | None = None
        self.key: Any = key


def insert(root: Node | None, key: Any):
    if root is None:
        return Node(key)
    if key > root.key:
        root.right = insert(root.right, key)
    else:
        root.left = insert(root.left, key)
    return root


def add_nodes_edges(graph: Digraph, node: Node | None):
    if node is None:
        return
    node_id = str(id(node))
    graph.node(node_id, label=str(node.key))
    if node.left:
        graph.edge(node_id, str(id(node.left)))
        add_nodes_edges(graph, node.left)
    if node.right:
        graph.edge(node_id, str(id(node.right)))
        add_nodes_edges(graph, node.right)


def main():
    if len(sys.argv) < 2:
        print("A simple script that generates a binary search tree based on input keys from command line input")
        print("    Usage: python bst.py <keys>")
        print("    e.g. python bst.py HELLOWORLD")
        return
    
    root = None
    for key in sys.argv[1]:
        root = insert(root, key)
        
    graph = Digraph(comment="Binary Search Tree", format="png")
    graph.attr("node", shape="circle", style="filled", color="lightblue")
    
    add_nodes_edges(graph, root)
    graph.render("bst", view=True)


if __name__ == "__main__":
    main()
