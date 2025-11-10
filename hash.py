class HashTable:
    def __init__(self):
        self.size = 10
        self.table = [None] * self.size

    def hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        self.table[index] = value
        print(f"Inserted key {key} at index {index}")  # <-- f-string added here

    def get(self, key):
        index = self.hash_function(key)
        return self.table[index]


hash_table = HashTable()

hash_table.insert(101, 500)
hash_table.insert(102, 600)
hash_table.insert(203, 700)

print("Value for key 102:", hash_table.get(102))
print("Value for key 203:", hash_table.get(203))