# Name: Tanishq Patil
# File: Codec.py- Contains all supplementary methods to Steagnography.py used for encoding and decoding
# Student ID:1961827
import numpy as np
class Codec():
    
    def __init__(self,delimiter):
        self.name = 'binary'
        self.delimiter = '#'
    # convert text or numbers into binary form    
    def encode(self, text):
        if type(text) == str:
            return ''.join([format(ord(i), "08b") for i in text])
        else:
            print('Format error')
    # convert binary data into text
    def decode(self, data):
        binary = []        
        for i in range(0,len(data),8):
            byte = data[i: i+8]
            if byte == self.encode(self.delimiter):
                break
            binary.append(byte)
        text = ''
        for byte in binary:
            text += chr(int(byte,2))       
        return text 
class CaesarCypher(Codec):
    def __init__(self, delimiter='#',shift=3):
        self.name = 'caesar'
        self.delimiter = '#'  
        self.shift = shift    
        self.chars = 256      # total number of characters
    # convert text into binary form
    # your code should be similar to the corresponding code used for Codec
    def encode(self, text):
        data = ''
        if type(text)==str:
            return data.join([format(ord(i)+self.shift%256,"08b") for i in text])## Add shift and convert to binary
        else:
            print('Format Error')
        # your code goes here
        return data
    
    # convert binary data into text
    # your code should be similar to the corresponding code used for Codec
    def decode(self, data):
        text = ''
        bin=[]
        for i in range(0,len(data),8):
            byte=data[i:i+8]
            if byte==self.encode(self.delimiter):
                break
            bin.append(byte)
        text=''
        for byte in bin:
            text+=chr(int(byte,2)-self.shift%256)   ## Substract shift convert back to text

        # your code goes here
        return text
# a helper class used for class HuffmanCodes that implements a Huffman tree
class Node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.left = left
        self.right = right
        self.freq = freq
        self.symbol = symbol
        self.code = ''
annoyingThingy={}   #Global variable used to move values out from the recursive function traverse_tree()
class HuffmanCodes(Codec):
    global annoyingthingy
    def __init__(self,delimiter="#"):
        self.nodes = None
        self.data = {}
        self.name = 'huffman'
        self.delimiter = '#'
    # make a Huffman Tree    
    def make_tree(self, data):
        # make nodes
        nodes = []
        for char, freq in data.items():
            nodes.append(Node(freq, char))
            
        # assemble the nodes into a tree
        while len(nodes) > 1:
            # sort the current nodes by frequency
            nodes = sorted(nodes, key=lambda x: x.freq)
            # pick two nodes with the lowest frequencies
            left = nodes[0]
            right = nodes[1]
            # assign codes
            left.code = '0'
            right.code = '1'
            # combine the nodes into a tree
            root = Node(left.freq+right.freq, left.symbol+right.symbol,
                        left, right)
            # remove the two nodes and add their parent to the list of nodes
            nodes.remove(left)
            nodes.remove(right)
            nodes.append(root)
        
        return nodes
    # traverse a Huffman tree
    def traverse_tree(self, node, val):
        global annoyingThingy
        next_val = val + node.code
        if(node.left):
            self.traverse_tree(node.left, next_val)
        if(node.right):
            self.traverse_tree(node.right, next_val)
        if(not node.left and not node.right):
            # print(f"{node.symbol}->{next_val}")# this is for debugging
            annoyingThingy[node.symbol]=next_val #add the value generated inside the recursion 
                                                #into a global variable
            
    # convert text into binary form
    def encode(self, text):
        global annoyingThingy
        data = ''
        returner={}
        for i in range(len(text)):
            if text[i] in returner:
                returner[text[i]]+=1
            else:
                returner[text[i]]=1
        tree=self.make_tree(returner)
        self.nodes=tree
        x=[]
        for i in range(len(tree)):
            self.traverse_tree(tree[i],"")
        for i in range(len(text)):
            data=data+annoyingThingy[text[i]]
        self.data=annoyingThingy
        annoyingThingy={}
        
    



        

        
        # your code goes here
        # you need to make a tree
        # and traverse it
        return data
    # convert binary data into text
    def decode(self, data):
        global annoyingThingy
        nodes=self.nodes
        root=nodes[0]
        letterBuilder=""
        for i in range(len(nodes)):
            self.traverse_tree(nodes[i],"")
        container=""
        flag=False
        for j in range(len(data)):
            container=container+data[j]
            if container in annoyingThingy.values():
                for key, value in annoyingThingy.items():
                    if container == value:
                        letterBuilder+=key
                        if key==self.delimiter:
                            flag=True
                if flag:
                    break
                container=""
        
                
                

        text = letterBuilder



        # your code goes here
        # you need to traverse the tree
        return text.rstrip(self.delimiter)

# driver program for codec classes
if __name__ == '__main__':
    text = 'hello'
    #text = 'Casino Royale 10:30 Order martini'
    print('Original:', text)
    c = Codec('#')
    binary = c.encode(text + c.delimiter)
    print('Binary:',binary)
    data = c.decode(binary)
    print('Text:',data)
    cc = CaesarCypher('#')
    binary = cc.encode(text + cc.delimiter)
    print('Binary:',binary)
    data = cc.decode(binary)
    print('Text:',data)
    h = HuffmanCodes()
    binary = h.encode(text + h.delimiter)
    print('Binary:',binary)
    data = h.decode(binary)
    print('Text:',data)  