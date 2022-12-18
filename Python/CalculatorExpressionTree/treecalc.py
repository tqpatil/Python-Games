#Name: Tanishq Patil
#ID: 1961827
#File:tree.py
#Date:11/17/2022
#Program: Create a Binary Tree and Expression Tree. One global variable used to store values generated from recursive
          # function stringBuilder() inside Binary Tree. 
strBuild=""
from stack import Stack
class BinaryTree:

    def __init__(self,rootObj): ##Create doubly linked Binary Tree 
        self.key = rootObj
        self.rootNode=None
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self,newNode):   #if you pass a letter, simply create a tree node and set the left child to self
        if type(newNode)==type(""):
            self.leftChild = BinaryTree(newNode)
            self.leftChild.rootNode=self
        else:
            self.leftChild=BinaryTree(newNode.key)  #else, attach the entire tree of the passed tree to the left child of self
            self.leftChild.insertTree(newNode)

    def insertRight(self, newNode): #if you pass a letter, simply create a tree node and set the right child to self
        if self.rightChild == None:
            if type(newNode)==type(""):
                self.rightChild = BinaryTree(newNode)
                self.rightChild.rootNode=self
            else:
                self.rightChild=BinaryTree(newNode.key)#else, attach the entire tree of the passed tree to the right child of self
                self=self.rightChild.insertTree(newNode)
               
    def insertTree(self,tree):
        if tree.leftChild!=None or tree.rightChild!=None:#base case:you have not reached a root node
                if tree.leftChild!=None:
                    self.leftChild=BinaryTree(tree.leftChild.key)#insert left child
                    self.leftChild.rootNode=self
                    BinaryTree.insertTree(self.leftChild,tree.leftChild)#recursive call
                if tree.rightChild!=None:
                    self.rightChild=BinaryTree(tree.rightChild.key)#insert right child
                    self.rightChild.rootNode=self
                    BinaryTree.insertTree(self.rightChild,tree.rightChild)#Recursive call
                
        else:
            return self
            

        

    def getRightChild(self):#returns the right child of the selected node
        if self.rightChild!=None:
            return self.rightChild
        else:
            return None

    def getLeftChild(self):#returns the left child of the selected node
        if self.leftChild!=None:
            return self.leftChild
        else:
            return None
    def getRootVal(self):#returns the root value of a given node
        if self.key!=None:
            return self.key
        else:
            return None
    def setKeyVal(self,obj):#sets the root value of a given node
        self.key=obj
    def getRootNode(self):#gets the parent node of a give node
        return self.rootNode
    def setRootNode(self,node):#sets the parent node of a given node
        x=self.rootNode
        if not self.rootNode:
            self.rootNode=node
        else:
            temp=self.rootNode
            self.rootNode=node
            node.rootNode=temp
            

        
            
    global strBuild #global variable: holds the string built by the recursive function stringBuilder()
    def stringBuilder(self):
        global strBuild
        strBuild+=(self.key+"(")#adds open parenthesis
        if self.leftChild!=None:
            self.leftChild.stringBuilder()#left child
        strBuild+=(")(")#closed and open parenthesis
        if self.rightChild!=None:
            self.rightChild.stringBuilder()#right child
        strBuild+=(")")#and finally, closed parenthesis
    def __str__(self):
        global strBuild
        self.stringBuilder()
        x=strBuild  #Stores and resets the string built from the stringBuilder()
        strBuild=""
        return x

class ExpTree (BinaryTree):
    def make_tree(postfix):
        stack=Stack()  
        
        ops=["*","/","+","-","^"]
        if type(postfix)==type(ops):    #if postfix is an array already
            postfixArr=postfix
        else:
            postfixArr=postfix.split(" ")   #if postfix is a string
        for i in range(len(postfixArr)):#iterate through the postfix array
            flag=False
            for j in range(len(ops)):#check if postfix is an operator
                if ops[j] in postfixArr[i]:
                    flag=True
            if flag==True:  #if it is an operator, pop the 2 operands that correlate to it
                item1=stack.pop()
                item2=stack.pop()
                tree=ExpTree(postfixArr[i])#create a tree with the operator as the parent and the operands as the children
                tree.insertRight(item1)
                tree.insertLeft(item2)
                stack.push(tree)#add it to the stack
            if flag==False:
                stack.push(postfixArr[i]) #if it is an operand, add it to the stack
            
        x=stack.pop() #once the program has made a tree from every single item in postfix, pop it from the stack
        return(x)#return the tree
            

    

    def __str__(self):
        return ExpTree.strBuilder(self)#recursive function stringBuilder used to generate a string from a tree
    def preorder(tree):
        s = ''
        if tree != None:#base case
            s = tree.key#first add the operator
            s += ExpTree.preorder(tree.getLeftChild())#then the left child
            s += ExpTree.preorder(tree.getRightChild())#then the right child
        return s
    def strBuilder(tree):
        s = ''
        if tree != None:#base case
            flag=False
            if tree.leftChild!=None and tree.rightChild!=None:
                flag=True
            if flag:    #if the tree node is a leaf node
                s+="(" #add parenthesis
            s += ExpTree.strBuilder(tree.getLeftChild())#add left child
            s += tree.key#then operator
            s += ExpTree.strBuilder(tree.getRightChild())#then right child
            if flag:
                s+=")"#close parenthesis
            
            
        return s
    def postorder(tree):
        s = ''
        if tree != None:    #base case
            s += ExpTree.postorder(tree.getLeftChild())#add left child
            s += ExpTree.postorder(tree.getRightChild())#then right child
            
            s += tree.key#then operator
            
            
            
            
        return s






    def inorder(tree):
        s = ''
        if tree != None:#base case
            flag=False
            if tree.leftChild==None and tree.rightChild==None:
                flag=True
            if flag==False: #if the tree node is a leaf
                s+="("  #open parenthesis
            s += ExpTree.inorder(tree.getLeftChild())#add left child
           
            s += tree.key#add operator
            s += ExpTree.inorder(tree.getRightChild())#then right child
            if flag==False:
                s+=")"#close parenthesis
        return s
         
    def evaluate(tree):
        ops=["*","/","+","-","^"]
        curr=tree
        if curr ==None:#if the tree is empty, return none
            return None
        if curr.leftChild==None and curr.rightChild==None:#if it is a leaf
            x=float(curr.key)
            return x #return operator value as a float
        left=ExpTree.evaluate(curr.leftChild)   #recursive call on the left operator until you get a leaf
        right=ExpTree.evaluate(curr.rightChild) #recursive call on the right operator until you get a leaf
        if curr.key=='+':   
            return round((left)+(right),8)#add the two floats and avoid floating point precision errors
        if curr.key=='*':
            return round((left)*(right),8)#multiply
        if curr.key=="/":
            try:
                return round((left)//(right),8)#Divide
            except Exception:
                print("Cannot divide by Zero or invalid numbers")#if an invalid input such as 0, catch 
                return None
        if curr.key=="^":
            return round((left)**(right),8)#power
        if curr.key=="-":
            return round((left)-(right),8)#substract
        
                


if __name__ == '__main__':
    # test a BinaryTree
    
    r = BinaryTree('a')
    assert r.getRootVal() == 'a'
    assert r.getLeftChild()== None
    assert r.getRightChild()== None
    assert str(r) == 'a()()'
    
    r.insertLeft('b')
    assert r.getLeftChild().getRootVal() == 'b'
    assert str(r) == 'a(b()())()'
    
    r.insertRight('c')
    assert r.getRightChild().getRootVal() == 'c'
    assert str(r) == 'a(b()())(c()())'
    
    r.getLeftChild().insertLeft('d')
    r.getLeftChild().insertRight('e')
    r.getRightChild().insertLeft('f')
    assert str(r) == 'a(b(d()())(e()()))(c(f()())())'
    assert str(r.getRightChild()) == 'c(f()())()'
    assert r.getRightChild().getLeftChild().getRootVal() == 'f'
    
    # test an ExpTree
    
    postfix = '5.1111 2.1111 3.1111 * +'.split()
    tree = ExpTree.make_tree(postfix)
    assert str(tree) == '(5.1111+(2.1111*3.1111))'
    assert ExpTree.inorder(tree) == '(5.1111+(2.1111*3.1111))'
    assert ExpTree.postorder(tree) == '5.11112.11113.1111*+'
    assert ExpTree.preorder(tree) == '+5.1111*2.11113.1111'
    assert ExpTree.evaluate(tree) == 11.67894321
    postfix = '5 2 + 3 *'.split()
    tree = ExpTree.make_tree(postfix)
    assert str(tree) == '((5+2)*3)'
    assert ExpTree.inorder(tree) == '((5+2)*3)'
    assert ExpTree.postorder(tree) == '52+3*'
    assert ExpTree.preorder(tree) == '*+523'
    assert ExpTree.evaluate(tree) == 21.0
