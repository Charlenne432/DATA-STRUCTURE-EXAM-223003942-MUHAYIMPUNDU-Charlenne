from collections import deque  # Python's built-in deque class

class MealOrder:
    def __init__(self, order_id, customer_name, meal_name):
        self.order_id = order_id            # Unique order ID
        self.customer_name = customer_name  # Customer name
        self.meal_name = meal_name          # Meal name
    
    def __str__(self):
        return f"Order ID: {self.order_id}, Customer: {self.customer_name}, Meal: {self.meal_name}"

class MealOrderDeque:
    def __init__(self):
        self.deque = deque()  # Create an empty deque to store orders
    
    def add_order_to_front(self, order):
        """ Add a new order to the front of the deque. """
        self.deque.appendleft(order)
    
    def add_order_to_back(self, order):
        """ Add a new order to the back of the deque. """
        self.deque.append(order)
    
    def process_oldest_order(self):
        """ Remove and return the oldest order from the front of the deque. """
        if self.deque:
            return self.deque.popleft()
        else:
            return None
    
    def process_most_recent_order(self):
        """ Remove and return the most recent order from the back of the deque. """
        if self.deque:
            return self.deque.pop()
        else:
            return None
    
    def view_oldest_order(self):
        """ View the oldest order without removing it. """
        if self.deque:
            return self.deque[0]
        else:
            return None
    
    def view_most_recent_order(self):
        """ View the most recent order without removing it. """
        if self.deque:
            return self.deque[-1]
        else:
            return None
    
    def display_orders(self):
        """ Display all the orders in the deque. """
        if not self.deque:
            print("No orders to display.")
            return
        for order in self.deque:
            print(order)

# Example Usage:
order1 = MealOrder(1, "Alice", "Chicken Salad")
order2 = MealOrder(2, "Bob", "Vegan Burger")
order3 = MealOrder(3, "Charlie", "Steak Dinner")

meal_deque = MealOrderDeque()

# Adding orders to the front and back of the deque
meal_deque.add_order_to_front(order1)
meal_deque.add_order_to_back(order2)
meal_deque.add_order_to_back(order3)

print("Orders in the deque:")
meal_deque.display_orders()

# Process and remove the oldest order (from the front)
oldest_order = meal_deque.process_oldest_order()
print(f"\nProcessing and removing the oldest order: {oldest_order}")

# Process and remove the most recent order (from the back)
most_recent_order = meal_deque.process_most_recent_order()
print(f"\nProcessing and removing the most recent order: {most_recent_order}")

print("\nRemaining Orders in the deque:")
meal_deque.display_orders()

# View the most recent order without removing it
recent_order = meal_deque.view_most_recent_order()
print(f"\nMost Recent Order (view only): {recent_order}")
