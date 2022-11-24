def is_palindrome(s):
    stack=Stack()
    stack2=""
    for i in range(len(s)):
        stack.push(s[i])
    while stack.isEmpty()==False:
        stack2+=(stack.pop())
    if stack2==s:
        return True
    else:
        return False    
        
    

class Stack():
    def __init__(self):
         self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)
if __name__ == '__main__':
    print(is_palindrome("hello"))
    print(is_palindrome("madam"))   