class hashtable:
   def __init__(self):
       self.size = 10
       self.table = [none]*self.size
       
   def hash_function(self,key):
       return key % self.size
   
   def insert(self,value,key):
        index = self.hash_function(key)
        self.table[index] = value
        
        print(f"inserted key{key} at index{index}")
        
   def get(self,key):
       index = self.hash_function(key)
       return self.table[index]
   
   hash_table = hash.Table()
   hash_table.insert(100 , 450)
   hash_table.insert(101 , 500)
   hash_table.insert(203 , 700)
   
   print("value for key 102:",hash_table.get(101))
   print("value for key 203:", hash_table.get(203))
       
        
        
   
    
   