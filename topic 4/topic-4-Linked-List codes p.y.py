class Node:
    def __init__(self, data):
        self.data = data  # The data of the node (survey response)
        self.next = None  # The reference to the next node (initially None)

class SinglyLinkedList:
    def __init__(self, max_size):
        self.head = None  # Initially, the list is empty
        self.tail = None  # The tail of the list (used for efficient append)
        self.size = 0  # The current size of the linked list
        self.max_size = max_size  # The fixed size of the list

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.max_size

    def add_order(self, data):
        """Add a new order (survey response) to the list."""
        new_node = Node(data)

        if self.is_empty():
            # If the list is empty, both head and tail will point to the new node
            self.head = self.tail = new_node
        else:
            # Otherwise, append the new node to the end of the list
            self.tail.next = new_node
            self.tail = new_node

        self.size += 1

        # If the list exceeds the max size, remove the oldest order
        if self.size > self.max_size:
            self.remove_oldest_order()

        print(f"Order Added: {data}")

    def remove_oldest_order(self):
        """Remove the oldest order (the head of the list)."""
        if not self.is_empty():
            # The oldest order is the head of the list
            removed_data = self.head.data
            self.head = self.head.next  # Move the head to the next node
            self.size -= 1
            print(f"Order Removed: {removed_data}")
    
    def display_orders(self):
        """Display all the orders in the linked list."""
        if self.is_empty():
            print("No orders in the list.")
        else:
            current = self.head
            print("Orders in the list:")
            while current:
                print(current.data, end=" -> ")
                current = current.next
            print("None")  # End of list

# Example Usage:

# Initialize the linked list with a fixed size of 3 (Maximum 3 orders can be stored)
survey_orders = SinglyLinkedList(max_size=3)

# Add orders (survey responses) to the list
survey_orders.add_order("Response 1: Agree")
survey_orders.add_order("Response 2: Disagree")
survey_orders.add_order("Response 3: Neutral")

# Display the current orders
survey_orders.display_orders()

# Add another order, which will cause the oldest order to be removed
survey_orders.add_order("Response 4: Agree")

# Display the orders again to see the updated list
survey_orders.display_orders()

# Add more orders and continue to remove the oldest ones if the list exceeds the max size
survey_orders.add_order("Response 5: Strongly Agree")
survey_orders.display_orders()

survey_orders.add_order("Response 6: Disagree")
survey_orders.display_orders()
