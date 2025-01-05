class MealOrder:
    def __init__(self, order_id, customer_name, meal_name, priority):
        self.order_id = order_id              # Unique order ID
        self.customer_name = customer_name    # Customer name
        self.meal_name = meal_name            # Meal name
        self.priority = priority              # Priority level (1 to 5)
    
    def __str__(self):
        return f"Order ID: {self.order_id}, Customer: {self.customer_name}, Meal: {self.meal_name}, Priority: {self.priority}"

def counting_sort_orders_by_priority(orders):
    # Find the maximum priority value in the orders (assuming priority ranges from 1 to 5)
    max_priority = 5  # Hardcoded for simplicity (can be dynamically calculated)
    
    # Initialize a count array for each priority level (1 to max_priority)
    count = [0] * (max_priority + 1)  # Count array for priorities 1 through max_priority
    
    # Create a list to store the sorted orders
    sorted_orders = [None] * len(orders)
    
    # Count the frequency of each priority in the orders
    for order in orders:
        count[order.priority] += 1
    
    # Update the count array to hold the cumulative sum
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    
    # Place the orders into the sorted array using the cumulative count array
    for order in reversed(orders):  # Traverse in reverse to maintain stable sorting
        sorted_orders[count[order.priority] - 1] = order
        count[order.priority] -= 1
    
    return sorted_orders

# Example Usage:
order1 = MealOrder(1, "Alice", "Chicken Salad", 3)
order2 = MealOrder(2, "Bob", "Vegan Burger", 1)
order3 = MealOrder(3, "Charlie", "Steak Dinner", 4)
order4 = MealOrder(4, "David", "Vegan Pasta", 5)
order5 = MealOrder(5, "Eve", "Fish Tacos", 2)

orders = [order1, order2, order3, order4, order5]

# Display orders before sorting
print("Orders Before Sorting:")
for order in orders:
    print(order)

# Sorting orders by priority using Counting Sort
sorted_orders = counting_sort_orders_by_priority(orders)

# Display orders after sorting
print("\nOrders After Sorting by Priority:")
for order in sorted_orders:
    print(order)
