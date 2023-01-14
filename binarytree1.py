#general tree which node can have any of the elements  
class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        #leftsearchtree
        self.left = None #elements are less than the current node
        #rightsearchtree
        self.right = None #elements are greater than the current node
     
    #method of checking the value 
    def add_child(self, data):
        if data == self.data: #see if the value already exists
            return

        #if the data is less than self.data
        if data < self.data: 
            #add data in left subtree
            if self.left: #check if the left element has value
                self.left.add_child(data) #call child method
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            #add data in right subtree
            if self.left: #check if the right element has value
                self.left.add_child(data) #call child method
            else:
                self.right = BinarySearchTreeNode(data)
    
    #method that return the list of elements in binary tree in specific order       
    def in_order_traversal(self):
    