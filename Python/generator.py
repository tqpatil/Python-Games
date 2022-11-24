
def anagram(word):
    if len(word)>1:
        for x in anagram(word[1:]):
            for i in range(len(word)):
                yield x[:i] + word[0:1]+x[i:]
    else:
        yield word[len(word)-1]
    

def import_dictionary (dictionary_file) :
    dictionary = {}
    try :
        for i in range(50):
            dictionary[i]=[]
        with open(dictionary_file) as f:
            for line in f:
                word=line.strip()
                dictionary[len(word)].append(word)
                   
    except Exception :
        print("Failed to create dictionary of proper size")
    for i in range(len(dictionary)):
        if len(dictionary[i])==0:
            del dictionary[i]    
    return dictionary
    




file="C:\\Users\\tqpat\\OneDrive\\Documents\\Python\\dictionary.txt"
dictionary=import_dictionary(file)
word="ram"
test=list(anagram(word))
# for key in dictionary:
#     for i in range(len(dictionary[key])):
#         if dictionary[key][i] in test:
#             if dictionary[key][i]!=word:
#                 print(dictionary[key][i])


