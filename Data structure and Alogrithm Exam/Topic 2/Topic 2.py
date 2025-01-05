class TreeNode:
    def __init__(self, meal_name, price):
        self.meal_name = meal_name  # Name of the meal (e.g., "Chicken Salad")
        self.price = price          # Price of the meal (e.g., 12.99)
        self.left = None            # Left child (less expensive meal)
        self.right = None           # Right child (more expensive meal)

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert(self, meal_name, price):
        """ Insert a new meal plan into the binary tree. """
        new_node = TreeNode(meal_name, price)
        if self.root is None:
            self.root = new_node
        else:
            self._insert_recursive(self.root, new_node)
    
    def _insert_recursive(self, current_node, new_node):
        """ Helper function to recursively insert a new node. """
        if new_node.price < current_node.price:
            if current_node.left is None:
                current_node.left = new_node
            else:
                self._insert_recursive(current_node.left, new_node)
        else:
            if current_node.right is None:
                current_node.right = new_node
            else:
                self._insert_recursive(current_node.right, new_node)
    
    def in_order_traversal(self, node):
        """ Perform in-order traversal of the tree. """
        if node:
            self.in_order_traversal(node.left)
            print(f"Meal: {node.meal_name}, Price: ${node.price}")
            self.in_order_traversal(node.right)

# Example Usage:
bt = BinaryTree()
bt.insert("Chicken Salad", 12.99)
bt.insert("Vegan Burger", 10.99)
bt.insert("Steak Dinner", 25.99)

print("Meal Plans (in-order):")
bt.in_order_traversal(bt.root)

class BSTNode:
    def __init__(self, customer_name, order_value):
        self.customer_name = customer_name  # Name of the customer
        self.order_value = order_value      # Order value (e.g., price)
        self.left = None                    # Left child
        self.right = None                   # Right child

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, customer_name, order_value):
        """ Insert a new order into the binary search tree. """
        new_node = BSTNode(customer_name, order_value)
        if self.root is None:
            self.root = new_node
        else:
            self._insert_recursive(self.root, new_node)
    
    def _insert_recursive(self, current_node, new_node):
        """ Helper function to recursively insert a new node. """
        if new_node.order_value < current_node.order_value:
            if current_node.left is None:
                current_node.left = new_node
            else:
                self._insert_recursive(current_node.left, new_node)
        else:
            if current_node.right is None:
                current_node.right = new_node
            else:
                self._insert_recursive(current_node.right, new_node)
    
    def search(self, order_value):
        """ Search for an order by value. """
        return self._search_recursive(self.root, order_value)
    
    def _search_recursive(self, current_node, order_value):
        """ Helper function to search recursively. """
        if current_node is None or current_node.order_value == order_value:
            return current_node
        elif order_value < current_node.order_value:
            return self._search_recursive(current_node.left, order_value)
        else:
            return self._search_recursive(current_node.right, order_value)
    
    def in_order_traversal(self, node):
        """ Perform in-order traversal of the tree. """
        if node:
            self.in_order_traversal(node.left)
            print(f"Customer: {node.customer_name}, Order Value: ${node.order_value}")
            self.in_order_traversal(node.right)

# Example Usage:
bst = BinarySearchTree()
bst.insert("Alice", 25.99)
bst.insert("Bob", 10.99)
bst.insert("Charlie", 18.50)

print("Customer Orders (in-order):")
bst.in_order_traversal(bst.root)

# Searching for an order:
order = bst.search(18.50)
if order:
    print(f"\nFound Order: {order.customer_name}, Order Value: ${order.order_value}")
else:
    print("\nOrder not found.")
