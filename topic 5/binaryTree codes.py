class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_recursive(self.root, data)

    def _insert_recursive(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert_recursive(node.left, data)
        elif data > node.data:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert_recursive(node.right, data)

    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.data, end=" ")
            self.inorder_traversal(node.right)

    def search(self, data):
        return self._search_recursive(self.root, data)

    def _search_recursive(self, node, data):
        if node is None or node.data == data:
            return node
        if data < node.data:
            return self._search_recursive(node.left, data)
        return self._search_recursive(node.right, data)

# Example usage:
bt = BinaryTree()

# Insert survey responses (e.g., IDs or ratings)
responses = [5, 3, 8, 1, 4, 7, 9]
for response in responses:
    bt.insert(response)

# Display survey responses in sorted order (inorder traversal)
print("Survey Responses (Inorder Traversal):")
bt.inorder_traversal(bt.root)
print()

# Search for a specific response (e.g., response ID)
response_to_search = 4
result = bt.search(response_to_search)
if result:
    print(f"Response {response_to_search} found!")
else:
    print(f"Response {response_to_search} not found!")
