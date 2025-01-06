class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = self.rear = -1  # Initialize both front and rear to -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front

    def enqueue(self, data):
        if self.is_full():
            print("Queue is full. Overwriting the oldest data.")
            self.dequeue()  # Remove the oldest data when the queue is full
        
        if self.is_empty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.capacity

        self.queue[self.rear] = data
        print(f"Enqueued: {data}")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. No data to dequeue.")
            return None
        data = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1  # Queue becomes empty
        else:
            self.front = (self.front + 1) % self.capacity
        return data

    def peek(self):
        if self.is_empty():
            print("Queue is empty.")
            return None
        return self.queue[self.front]

    def display(self):
        if self.is_empty():
            print("Queue is empty.")
        else:
            i = self.front
            while True:
                print(self.queue[i], end=" ")
                if i == self.rear:
                    break
                i = (i + 1) % self.capacity
            print()

# Example usage:
cq = CircularQueue(5)

# Enqueue data (representing survey responses)
cq.enqueue("Response 1")
cq.enqueue("Response 2")
cq.enqueue("Response 3")
cq.enqueue("Response 4")
cq.enqueue("Response 5")

# Display queue
cq.display()

# Dequeue data
cq.dequeue()
cq.display()

# Enqueue another response after dequeue
cq.enqueue("Response 6")
cq.display()

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

