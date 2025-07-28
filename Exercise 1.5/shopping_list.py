class ShoppingList(object):

    # initialized data attributes
    def __init__(self, list_name):

        # name of the shopping list
        self.list_name = list_name

    # a list that will contain names of items
        self.shopping_list = []

    # adds an item to a self.shopping_list if item is not already there
    def add_item(self, item):
        if item not in self.shopping_list:
            self.shopping_list.append(item)

            # removes an item from shopping_list
    def remove_item(self, item):
        if item in self.shopping_list:
            self.shopping_list.remove(item)

            # prints the contents of self.shopping_list
    def view_list(self):
        print(self.shopping_list)
