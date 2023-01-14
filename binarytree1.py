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
        else:
            #add data in right subtree