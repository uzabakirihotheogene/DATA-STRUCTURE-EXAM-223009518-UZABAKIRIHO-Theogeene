class Queue:
    def __init__(self, capacity):
        # Initialize an empty queue with a specified capacity
        self.capacity = capacity
        self.queue = []
    
    def is_empty(self):
        # Check if the queue is empty
        return len(self.queue) == 0

    def is_full(self):
        # Check if the queue is full
        return len(self.queue) == self.capacity
    
    def enqueue(self, data):
        # Add a new item to the queue
        if self.is_full():
            print("Queue is full. Cannot enqueue more responses.")
        else:
            self.queue.append(data)
            print(f"Enqueued: {data}")

    def dequeue(self):
        # Remove the first item from the queue (FIFO)
        if self.is_empty():
            print("Queue is empty. No responses to process.")
            return None
        else:
            data = self.queue.pop(0)
            print(f"Dequeued: {data}")
            return data

    def peek(self):
        # Look at the front item of the queue without removing it
        if self.is_empty():
            print("Queue is empty.")
            return None
        return self.queue[0]
    
    def display(self):
        # Display the current queue of survey responses
        if self.is_empty():
            print("Queue is empty.")
        else:
            print("Current queue of survey responses:")
            for item in self.queue:
                print(item, end=" ")
            print()

# Example usage of the Queue class:

# Create a queue with a capacity of 5 responses
survey_queue = Queue(capacity=5)

# Enqueue survey responses
survey_queue.enqueue("Response 1: Agree")
survey_queue.enqueue("Response 2: Disagree")
survey_queue.enqueue("Response 3: Neutral")
survey_queue.enqueue("Response 4: Agree")
survey_queue.enqueue("Response 5: Strongly Agree")

# Display the current queue of responses
survey_queue.display()

# Try to enqueue another response when the queue is full
survey_queue.enqueue("Response 6: Disagree")

# Process (dequeue) survey responses one by one
survey_queue.dequeue()  # Process the first response
survey_queue.dequeue()  # Process the next response

# Display the queue after some responses have been processed
survey_queue.display()

# Peek the front of the queue
survey_queue.peek()

# Dequeue remaining responses
survey_queue.dequeue()
survey_queue.dequeue()
survey_queue.dequeue()

# Try to dequeue from an empty queue
survey_queue.dequeue()
