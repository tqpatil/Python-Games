#Name:Tanishq Patil
#Student ID:1961827
#File:stack.py
#Date:11/17/2022
#Sources: Professor Munishkina, Google Colab, https://colab.research.google.com/drive/1jfk6wrSwB9m7fOYWbtv4MUIqEoDvRd0f?authuser=1#scrollTo=r42CkqOuC0vD
class Stack:

    def __init__(self):
        self.items=[]
    def isEmpty(self):
        if self.items==[]:
            return True
        else:
            return False
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if len(self.items)==0:
            return None
        else:
            return self.items.pop()
    def peek(self):
        if len(self.items)==0:
            return None
        else:
            return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)

        