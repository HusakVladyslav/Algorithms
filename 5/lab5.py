import random
import matplotlib.pyplot as plt
import networkx as nx


class Node:
    def __init__(self, key, parent=None):
        self.key = key
        self.left = None
        self.right = None
        self.parent = parent


class Tree:
    def __init__(self):
        self.root = None

    def add_node(self, key, node=None):
        if self.root is None:
            self.root = Node(key)
        else:
            if node is None:
                node = self.root
            if key < node.key:
                if node.left is None:
                    node.left = Node(key, parent=node)
                else:
                    self.add_node(key, node.left)
            else:
                if node.right is None:
                    node.right = Node(key, parent=node)
                else:
                    self.add_node(key, node.right)

    def search(self, key, node=None):
        if node is None:
            node = self.root
        if node is None:
            print("Tree is empty")
            return None
        if node.key == key:
            print(f"Key {key} exists")
            return node
        elif key < node.key and node.left is not None:
            print("Searching left")
            return self.search(key, node.left)
        elif key > node.key and node.right is not None:
            print("Searching right")
            return self.search(key, node.right)
        else:
            print("Key does not exist")
            return None

    def delete_node(self, key, node=None):
        if node is None:
            node = self.search(key)
        if node is None:
            print("Key to delete does not exist")
            return
        parent_node = node.parent
        if node.left is None and node.right is None:
            if key <= parent_node.key:
                parent_node.left = None
            else:
                parent_node.right = None
        elif node.left is not None and node.right is None:
            if node.left.key < parent_node.key:
                parent_node.left = node.left
            else:
                parent_node.right = node.left
        elif node.right is not None and node.left is None:
            if node.key <= parent_node.key:
                parent_node.left = node.right
            else:
                parent_node.right = node.right
        else:
            min_value = self.find_minimum(node.right)
            node.key = min_value.key
            self.delete_node(min_value.key, min_value)

    def find_minimum(self, node=None):
        if node is None:
            node = self.root
        while node.left is not None:
            node = node.left
        return node

    def tree_data(self, node=None):
        if node is None:
            node = self.root
        stack = []
        while stack or node:
            if node is not None:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                yield node.key
                node = node.right


# Функція для візуалізації дерева
def visualize_tree(tree):
    G = nx.DiGraph()

    def add_edges(node):
        if node.left:
            G.add_edge(node.key, node.left.key)
            add_edges(node.left)
        if node.right:
            G.add_edge(node.key, node.right.key)
            add_edges(node.right)

    if tree.root:
        add_edges(tree.root)

    pos = knuth_layout(tree.root)
    node_colors = ["red" if node == tree.root.key else "skyblue" for node in G.nodes()]
    
    nx.draw(G, pos=pos, with_labels=True, node_size=700, node_color=node_colors, font_size=10, font_weight="bold", arrows=False)
    plt.show()


def knuth_layout(root):
    levels = {}
    def traverse(node, depth=0, pos=0):
        if node is not None:
            if depth not in levels:
                levels[depth] = []
            levels[depth].append((node, pos))
            traverse(node.left, depth + 1, pos - 1)
            traverse(node.right, depth + 1, pos + 1)

    traverse(root)

    pos = {}
    for depth in levels:
        nodes_at_level = levels[depth]
        nodes_at_level.sort(key=lambda x: x[1])
        for idx, (node, _) in enumerate(nodes_at_level):
            pos[node.key] = (idx, -depth)

    return pos


# Створення дерева та додавання рандомних чисел
tree = Tree()
for _ in range(10):
    tree.add_node(random.randint(-500, 0))

# Візуалізація дерева
visualize_tree(tree)
