# 🌳 Binary Search Tree for City and Population

class Node:
    def _init_(self, city, population):
        self.city = city
        self.population = population
        self.left = None
        self.right = None


class CityBST:
    def _init_(self):
        self.root = None

    # ----------- INSERT (Add City) -----------
    def insert(self, root, city, population):
        if root is None:
            return Node(city, population)

        if city.lower() < root.city.lower():
            root.left = self.insert(root.left, city, population)
        elif city.lower() > root.city.lower():
            root.right = self.insert(root.right, city, population)
        else:
            print(f"City '{city}' already exists! Use update option instead.")
        return root

    def add_city(self, city, population):
        self.root = self.insert(self.root, city, population)

    # ----------- UPDATE POPULATION -----------
    def update_population(self, root, city, new_pop):
        if root is None:
            print(f"City '{city}' not found!")
            return
        if city.lower() < root.city.lower():
            self.update_population(root.left, city, new_pop)
        elif city.lower() > root.city.lower():
            self.update_population(root.right, city, new_pop)
        else:
            root.population = new_pop
            print(f"Population of '{city}' updated to {new_pop}.")

    # ----------- DELETE CITY -----------
    def delete_city(self, root, city):
        if root is None:
            return root

        if city.lower() < root.city.lower():
            root.left = self.delete_city(root.left, city)
        elif city.lower() > root.city.lower():
            root.right = self.delete_city(root.right, city)
        else:
            # Node found
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            # Node with two children
            temp = self.min_value_node(root.right)
            root.city = temp.city
            root.population = temp.population
            root.right = self.delete_city(root.right, temp.city)
        return root

    def min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    # ----------- DISPLAY (Ascending Order) -----------
    def display_ascending(self, root):
        if root:
            self.display_ascending(root.left)
            print(f"{root.city} → Population: {root.population}")
            self.display_ascending(root.right)

    # ----------- DISPLAY (Descending Order) -----------
    def display_descending(self, root):
        if root:
            self.display_descending(root.right)
            print(f"{root.city} → Population: {root.population}")
            self.display_descending(root.left)

    # ----------- SEARCH & COUNT COMPARISONS -----------
    def search_city(self, root, city):
        comparisons = 0
        while root is not None:
            comparisons += 1
            if city.lower() == root.city.lower():
                print(f"City '{city}' found with population {root.population}.")
                print(f"Total comparisons made: {comparisons}")
                return
            elif city.lower() < root.city.lower():
                root = root.left
            else:
                root = root.right
        print(f"City '{city}' not found after {comparisons} comparisons.")


# ----------- MAIN PROGRAM -----------
bst = CityBST()

# Add cities
bst.add_city("Pune", 7000000)
bst.add_city("Mumbai", 12500000)
bst.add_city("Delhi", 11000000)
bst.add_city("Nagpur", 3000000)
bst.add_city("Nashik", 500000)

print("\n🌆 Cities in Ascending Order:")
bst.display_ascending(bst.root)

print("\n🌇 Cities in Descending Order:")
bst.display_descending(bst.root)

# Search a city
print("\n🔍 Searching for 'Delhi':")
bst.search_city(bst.root, "Delhi")

# Update population
print("\n✏ Updating population of 'Nagpur':")
bst.update_population(bst.root, "Nagpur", 3500000)

# Delete a city
print("\n🗑 Deleting city 'Nashik':")
bst.root = bst.delete_city(bst.root, "Nashik")

print("\n🏙 Cities after deletion (Ascending Order):")
bst.display_ascending(bst.root)