import heapq  # Python's built-in module for heaps

class MealOrder:
    def __init__(self, order_id, customer_name, delivery_time):
        self.order_id = order_id          # Unique order ID
        self.customer_name = customer_name  # Customer name
        self.delivery_time = delivery_time  # Time when meal should be delivered
    
    def __lt__(self, other):
        """ Define comparison for heap (based on delivery_time) """
        return self.delivery_time < other.delivery_time

    def __str__(self):
        return f"Order ID: {self.order_id}, Customer: {self.customer_name}, Delivery Time: {self.delivery_time}"

class MealOrderHeap:
    def __init__(self):
        self.heap = []

    def add_order(self, order):
        """ Add a new order to the heap (priority queue). """
        heapq.heappush(self.heap, order)

    def process_next_order(self):
        """ Remove and return the order with the earliest delivery time. """
        if self.heap:
            return heapq.heappop(self.heap)
        else:
            return None

    def peek_next_order(self):
        """ Look at the order with the earliest delivery time without removing it. """
        if self.heap:
            return self.heap[0]
        else:
            return None
    
    def display_orders(self):
        """ Display all orders in the heap. """
        for order in self.heap:
            print(order)

# Example Usage:
order1 = MealOrder(1, "Alice", "2025-01-06 12:00")
order2 = MealOrder(2, "Bob", "2025-01-05 09:30")
order3 = MealOrder(3, "Charlie", "2025-01-06 10:00")

heap = MealOrderHeap()
heap.add_order(order1)
heap.add_order(order2)
heap.add_order(order3)

print("All Orders (sorted by delivery time):")
heap.display_orders()

# Processing the next order (earliest delivery time):
next_order = heap.process_next_order()
print(f"\nProcessing Next Order: {next_order}")

print("\nRemaining Orders after Processing:")
heap.display_orders()
