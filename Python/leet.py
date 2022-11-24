test = [1, 2, 32, 8, 17, 19, 42, 13, 0]
# simple hashing based on the modulo operation
index = [x % 9 for x in test] 

# folding hash function
k = 0
for item in test:
    s = 0
    item = str(item)
    for i in item:
        s += int(i)
    index[ k] = s % len(test)
    k += 1
# mid-square hash function
k = 0
for item in test:
    item = str(item*item)
    s = item
    #print(s)
    if len(item) > 1:
        #print(len(item)//2, len(item)//2 + 1)
        s = item[len(item)//2-1] + item[len(item)//2]
    index[ k] = int(s) % len(test)
    k += 1
def hash(astring, size):
    sum = 0
    for pos in range(len(astring)):
        sum = sum + ord(astring[ pos])
    return sum % size

test2 = ['cat', 'dog', 'horse', 'cow', 'bird', 'turtle', 'rabbit']
print(test2)
hashes = [hash(x, len(test2)) for x in test2]
print(hashes)