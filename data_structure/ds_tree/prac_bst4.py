class Node():
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None
    
class BST():
  def __init__(self, data):
    self.head = Node(data)
    
  def insert(self, data):
    self.curn = self.head
    while True:
      if data < self.curn.data:
        if self.curn.left != None:
          self.curn = self.curn.left
        else:
          self.curn.left = Node(data)
          break
      else:
        if self.curn.right != None:
          self.curn = self.curn.right
        else:
          self.curn.right = Node(data)
          break
    
  def search(self, data):
    self.curn = self.head
    while self.curn:
      if data == self.curn.data:
        print(f"{data} found")
        return
      elif data < self.curn.data:
        self.curn = self.curn.left
      else:
        self.curn = self.curn.right
    print(f"{data} not found")
    
  def delete(self, data):
    self.curn = self.head
    self.parent = self.head
    searched = False
    
    while self.curn:
      if data == self.curn.data:
        searched = True
        break
      elif data < self.curn.data:
        self.parent = self.curn
        self.curn = self.curn.left
      else:
        self.parent = self.curn
        self.curn = self.curn.right
    
    if searched == False:
      print(f"{data} not able to delete, not found")
      return
    
    if self.curn.left == None and self.curn.right == None:
      if data < self.parent.data:
        self.parent.left = None
      else:
        self.parent.right = None
        
    elif self.curn.left != None and self.curn.right == None:
      if data < self.parent.data:
        self.parent.left = self.curn.left
      else:
        self.parent.right = self.curn.left
        
    elif self.curn.left == None and self.curn.right != None:
      if data < self.parent.data:
        self.parent.left = self.curn.right
      else:
        self.parent.right = self.curn.right
        
    elif self.curn.left != None and self.curn.right != None:
      if data < self.parent.data:
        self.change_node = self.curn.right
        self.chang_parent = self.curn.right
        
        while self.change_node.left != None:
          self.change_parent = self.change_node
          self.change_node = self.change_node.left
          
        if self.change_node.right != None:
          self.change_parent.left = self.change_node.right
        else:
          self.change_parent.left = None
        
        self.parent.left = self.change_node
        self.change_node.left = self.curn.left
        self.change_node.right = self.curn.right
        
      else:
        self.change_node = self.curn.right
        self.chang_parent = self.curn.right
        
        while self.change_node.left != None:
          self.change_parent = self.change_node
          self.change_node = self.change_node.left
          
        if self.change_node.right != None:
          self.change_parent.left = self.change_node.right
        else:
          self.change_parent.left = None
          
        self.parent.right = self.change_node
        self.change_node.left = self.curn.left
        self.change_node.right = self.curn.right    
        
    print(f"{data} successfully deleted")
    
    
import random
bst = BST(0)
bst_nums = set()

while len(bst_nums) < 100:
  bst_nums.add(random.randint(0, 999))

for num in bst_nums:
  bst.insert(num)
  
delete_nums = set()
bst_nums = list(bst_nums)

while len(delete_nums) < 10:
  delete_nums.add(bst_nums[random.randint(0, 99)])
  
for num in delete_nums:
  bst.delete(num)
  
  