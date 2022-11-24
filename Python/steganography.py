#Name:Tanishq Patil
#File: Steganography.py- Used for encoding and decoding images using the supplementary class codec.py
# Student ID:1961827
import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from math import ceil
from codec import Codec, CaesarCypher, HuffmanCodes
class Steganography():
    
    def __init__(self):
        self.text = ''
        self.binary = ''
        self.delimiter = '#'
        self.codec = None
    def encode(self, filein, fileout, message, codec):
        image = cv2.imread(filein)
        #print(image) # for debugging
        
        # calculate available bytes
        max_bytes = image.shape[0] * image.shape[1] * 3 // 8
        print("Maximum bytes available:", max_bytes)
        # convert into binary
        if codec == 'binary':   ##Create Codecs
            self.codec = Codec(delimiter = self.delimiter) 
        elif codec == 'caesar':
            self.codec = CaesarCypher(delimiter = self.delimiter)
        elif codec == 'huffman':
           self.codec = HuffmanCodes(delimiter = self.delimiter)
        binary = self.codec.encode(message + self.delimiter)
        
        # check if possible to encode the message
        num_bytes = ceil(len(binary)//8) + 1 
        if  num_bytes > max_bytes:
            print("Error: Insufficient bytes!")
        else:
            print("Bytes to encode:", num_bytes) 
            self.text = message
            self.binary = binary
            a=0     
            while a<len(binary):       #Loop through the image file and change the least significant bit
                for i in range(len(image)):
                    for j in range(len(image[i])):
                        for k in range(len(image[i][j])):
                            if not a<len(binary):
                                break
                            if binary[a]=="1": 
                                if image[i][j][k]%2==0:
                                    if image[i][j][k]==0:
                                        image[i][j][k]=1
                                    else:
                                        image[i][j][k]-=1
                            if binary[a]=="0":
                                if image[i][j][k]%2==1:
                                    if image[i][j][k]==255:
                                        image[i][j][k]=254
                                    else:
                                        image[i][j][k]+=1
                            a=a+1
                        if not a<len(binary):
                            break
                    if not a<len(binary):
                        break
                if not a<len(binary):
                    break

                
            cv2.imwrite(fileout, image)
                   
    def decode(self, filein, codec):
        image = cv2.imread(filein)
        #print(image) # for debugging      
        flag=True
        # convert into text
        if codec == 'binary':
            self.codec = Codec(delimiter = self.delimiter) 
        elif codec == 'caesar':
            self.codec = CaesarCypher(delimiter = self.delimiter)
        elif codec == 'huffman':
            if self.codec == None or self.codec.name != 'huffman':
                print("A Huffman tree is not set!")
                flag = False
        if flag:
            binary_builder=""
            for i in range(len(image)): #Get the binary 
                for j in range(len(image[i])):
                    for k in range(len(image[i][j])):
                        if image[i][j][k]%2==0:
                            binary_builder+="0"
                        if image[i][j][k]%2==1:
                            binary_builder+="1"
            

            
            binary_data = binary_builder 
            # update the data attributes:
            self.text = self.codec.decode(binary_data)

            self.binary = ''.join([format(ord(i), "08b")for i in self.text]) #get binary
              
        
    def print(self):
        if self.text == '':
            print("The message is not set.")
        else:
            print("Text message:", self.text)
            print("Binary message:", self.binary)          
    def show(self, filename):
        plt.imshow(mpimg.imread(filename))  #show the image in a new figure
        plt.show()



