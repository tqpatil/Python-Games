def make_dict(list):
    dictionary={}
    for i in range(11):
        dictionary[i]=[]
    for i in range(len(list)):
        if len(list[i])>10:
            dictionary[10].append(list[i])
        else:
            dictionary[len(list[i])].append(list[i])
    for i in range(len(dictionary)):
        if len(dictionary[i])==0:
            del dictionary[i]
    return dictionary
if __name__ == '__main__':
    
    d = {2: ['at', 'to', 'no'], 3: ['add', 'sun'], 10: ['Hello! How are you?']}
    dictionary = make_dict(['at', 'add', 'sun', 'to', 'no', 'Hello! How are you?'])
    print (dictionary)
    assert dictionary == d
    print('Everything works correctly!')
    
