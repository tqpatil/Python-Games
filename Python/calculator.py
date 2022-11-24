#Name:Tanishq Patil
#File: calculator.py
# Student ID:1961827   
# #Date:11/17/2022 
from stack import Stack
from tree import BinaryTree 
from tree import ExpTree
def isNumber(strVal):#A function to determine if the value is a number and not an operator
    possibleOps=["(",")","/","*","+","-","^"]
    isNum=True
    for i in range(len(strVal)):
        if strVal in possibleOps:
            isNum=False
    return isNum

def infix_to_postfix(infix):
    infix.replace(" ", "") #remove spaces from the infix expression
    alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    nums="0123456789."
    possibleOps=["^","(",")","/","*","+","-","^"]
    numOrder=""
    opOrder=""
    infList=[]
    for i in range(len(infix)):
        if infix[i] in nums:
            numOrder+=infix[i]
        if infix[i] in possibleOps:
            infList.append(numOrder)
            infList.append(infix[i])
            numOrder=""
    infList.append(numOrder)
    infList2=[]
    for i in range(len(infList)):
        if infList[i]=='' or infList[i]==' ':
            pass
        else:
            infList2.append(infList[i])
    infList=infList2#^This is all used to parse the infix string input and get an array or list
    precedence={"(":1, "-":2,"+":2,"*":3,"/":3,"^":20} #The precedence for each operator (power is highest, parenthesis is lowest)(PEMDAS)
    operators=Stack()#operator stack
    output=[]
    for i in range(len(infList)):
        if isNumber(infList[i]):    #if the infix value is a number
            output.append(infList[i])#add it to the output list
        elif infList[i]=="(":#if open parenthesis
            operators.push(infList[i])#add it to the stack
        elif infList[i]==")":#if close parenthesis: pop out all the values from the stack until you get an open parenthesis
            x=operators.pop()
            while x!="(":
                output.append(x)
                x=operators.pop()
        else:#else: get the precedence of the operator
            pointerPrec=precedence[infList[i]]
            undisturbed=[]
            while operators.isEmpty()==False:#keep popping out values until you get an operator that is less than the precedence of the value
                if precedence[operators.peek()]>=pointerPrec:
                    pop=operators.pop()
                    output.append(pop)  
                else:
                    break
            operators.push(infList[i])#add this operator to the stack
    strBuilder=""
    if operators.isEmpty():
        for i in range(len(output)):
            strBuilder+=output[i]+" "
        return strBuilder.strip()#build a string postfix and return it 
    else:
        while operators.isEmpty()==False:
            output.append(operators.pop())
        for i in range(len(output)):
            strBuilder+=output[i]+" "
        return strBuilder.strip()#build a string postfix and return it 

def mainGameLoop():#Main game loop
    print("Welcome to Calculator Program!")
    flag=True
    while flag:
        Input=str(input("Please enter your expression here. To quit enter 'quit' or 'q':"))
        if Input.strip()=='q' or Input.strip()=='quit':
            print("\nGoodbye!")
            flag=False
            break
        else:
            output=calculate(Input.strip())
            print("\n")
            print(output)







def calculate(infix):   #Calculate function
    postfix=infix_to_postfix(infix)
    tree=ExpTree.make_tree(postfix)
    return ExpTree.evaluate(tree)
# a driver to test calculate module
if __name__ == '__main__':
    mainGameLoop()
    # # test infix_to_postfix function

    # assert infix_to_postfix('(52+23)*34') == '52 23 + 34 *'
    # assert infix_to_postfix('5+2*3') == '5 2 3 * +'
    # # test calculate function
    # print(calculate('5^2'))
    # assert calculate('5^2') == 25.0
    # assert calculate('4^3') == 64.0
    
    