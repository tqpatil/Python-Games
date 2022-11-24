#Name: Tanishq Patil
#ID: 1961827
#Program: Create a Binary Tree. One global variable used to store values generated from recursive
          # function stringBuilder(). 
strBuild=""
class BinaryTree:

    def __init__(self,rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t
    def insertRight(self, newNode):
        if self.rightChild==None:
            self.rightChild= BinaryTree(newNode)
        else:
            t= BinaryTree(newNode)
            t.leftChild=self.leftChild
            self.leftChild=t
    
    def getRightChild(self):
        if self.rightChild!=None:
            return self.rightChild
        else:
            return None

    def getLeftChild(self):
        if self.leftChild!=None:
            return self.leftChild
        else:
            return None
    def getRootVal(self):
        if self.key!=None:
            return self.key
        else:
            return None
    def setRootVal(self,obj):
        self.key=obj
        
    global strBuild
    def stringBuilder(self):
        global strBuild
        strBuild+=(self.key+"[")
        if self.leftChild!=None:
            self.leftChild.stringBuilder()
        strBuild+=("][")
        if self.rightChild!=None:
            self.rightChild.stringBuilder()
        strBuild+=("]")
    def __str__(tree):
        global strBuild
        tree.stringBuilder()
        x=strBuild
        strBuild=""
        return x
        
        

        
if __name__ == '__main__':
    r = BinaryTree('a')
    print(r)
    r.insertLeft('b')
    r.insertRight('c')
    print(r)
    r.getLeftChild().insertLeft('d')
    r.getLeftChild().insertRight('e')
    r.getRightChild().insertLeft('f')
    
    print(r)
    print(r.getRootVal())
    print(r.getLeftChild())
    print(r.getRightChild())