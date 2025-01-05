class OrderNode:
    def __init__(self, order_id, customer_name, meal_name):
        self.order_id = order_id            # Unique order ID
        self.customer_name = customer_name  # Customer name
        self.meal_name = meal_name          # Meal name
        self.next = None                    # Reference to the next order in the list

class FixedSizeLinkedList:
    def __init__(self, max_size):
        self.max_size = max_size        # Maximum size of the linked list
        self.head = None                # Head of the linked list
        self.tail = None                # Tail of the linked list
        self.size = 0                   # Current size of the linked list
    
    def add_order(self, order_id, customer_name, meal_name):
        """ Add a new order to the linked list. If full, remove the oldest order. """
        if self.size == self.max_size:
            self.remove_oldest_order()  # Remove the oldest order if the list is full

        new_order = OrderNode(order_id, customer_name, meal_name)
        if self.tail is None:
            self.head = self.tail = new_order
        else:
            self.tail.next = new_order
            self.tail = new_order

        self.size += 1
    
    def remove_oldest_order(self):
        """ Remove the oldest order from the linked list (FIFO). """
        if self.head is None:
            return
        
        self.head = self.head.next
        if self.head is None:  # If the list becomes empty after removal
            self.tail = None
        self.size -= 1
    
    def display_orders(self):
        """ Display all the orders in the linked list. """
        current = self.head
        if current is None:
            print("No orders to display.")
            return
        
        while current:
            print(f"Order ID: {current.order_id}, Customer: {current.customer_name}, Meal: {current.meal_name}")
            current = current.next

# Example Usage:
order_list = FixedSizeLinkedList(3)  # Create a fixed-size list that can hold 3 orders

# Adding orders
order_list.add_order(1, "Alice", "Chicken Salad")
order_list.add_order(2, "Bob", "Vegan Burger")
order_list.add_order(3, "Charlie", "Steak Dinner")

print("Orders in the system:")
order_list.display_orders()

# Adding a new order when the list is full (should remove the oldest order)
order_list.add_order(4, "David", "Pasta Primavera")

print("\nOrders after adding a new one (oldest order removed):")
order_list.display_orders()
