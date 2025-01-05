class MealTreeNode:
    def __init__(self, name, is_leaf=False):
        self.name = name            # Name of the category or item
        self.is_leaf = is_leaf      # Flag indicating if the node is a leaf (meal item)
        self.children = []          # List of child nodes (subcategories or meal items)
    
    def add_child(self, node):
        """ Add a child node to the current node. """
        self.children.append(node)

    def __str__(self):
        """ Return the name of the node (used for display). """
        return self.name


class MealMenuTree:
    def __init__(self):
        self.root = None  # Root node of the tree
    
    def set_root(self, root_node):
        """ Set the root node of the tree. """
        self.root = root_node

    def display_menu(self, node, level=0):
        """ Recursively display the meal menu starting from the root. """
        if node is None:
            return
        # Print the node name (with indentation for hierarchy)
        print(" " * level * 4 + node.name)
        # Recursively display each child node
        for child in node.children:
            self.display_menu(child, level + 1)

# Example Usage:
# Create meal categories and items
root = MealTreeNode("Menu")  # Root node representing the meal menu

# Main categories
entrees = MealTreeNode("Entrees")
vegan = MealTreeNode("Vegan", is_leaf=False)
vegan_salad = MealTreeNode("Vegan Salad", is_leaf=True)
vegan_pasta = MealTreeNode("Vegan Pasta", is_leaf=True)
entrees.add_child(vegan)  # Add Vegan category to Entrees

# Add vegan items to vegan category
vegan.add_child(vegan_salad)
vegan.add_child(vegan_pasta)

# Non-vegan category
non_vegan = MealTreeNode("Non-Vegan", is_leaf=False)
chicken = MealTreeNode("Chicken", is_leaf=True)
beef = MealTreeNode("Beef", is_leaf=True)
non_vegan.add_child(chicken)
non_vegan.add_child(beef)
entrees.add_child(non_vegan)

# Desserts category
desserts = MealTreeNode("Desserts", is_leaf=False)
cake = MealTreeNode("Chocolate Cake", is_leaf=True)
ice_cream = MealTreeNode("Ice Cream", is_leaf=True)
desserts.add_child(cake)
desserts.add_child(ice_cream)

# Root menu node connects everything
root.add_child(entrees)
root.add_child(desserts)

# Create the tree and display the menu
menu_tree = MealMenuTree()
menu_tree.set_root(root)
print("Meal Menu Structure:")
menu_tree.display_menu(menu_tree.root)
