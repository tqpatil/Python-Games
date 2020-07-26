##hour = int(input("Starting time (hours): "))
##mins = int(input("Starting time (minutes): "))
##dura = int(input("Event duration (minutes): "))
##
##mins = ((mins + (dura%60))%60)
##hour = (hour + dura//60) + ((mins + (dura%60))//60)
##
##print(hour, mins, sep="\n")

##x = input()
##if x == "Spathiphyllum":
##    print("Yes - Spathiphyllum is the best plant ever!")
##elif x == "spathiphyllum":
##    print("No, I want a big Spathiphyllum!")
##else:
##    print("Spathiphyllum! Not ", x, "!", sep="")



##year = int(input("Enter a year: "))
##
##if year%4 != 0:
##    type = "common"
##elif year%100 != 0:
##    type = "leap"
##elif year%400 != 0:
##    type = "common"
##else:
##    type = "leap"
##print(type)
##if year < 1582:
##    print("Not within the Gregorian calendar period")



##secret_number = 777
##
##print(
##"""
##+================================+
##| Welcome to my game, muggle!    |
##| Enter an integer number        |
##| and guess what number I've     |
##| picked for you.                |
##| So, what is the secret number? |
##+================================+
##""")
##
##x = input()
##while int(x) != secret_number:
##    print("Ha ha! You're stuck in my loop!")
##    x = input("Enter another number: ")
##print("Well done, muggle! You are free now.")

##userWord = input("Enter a word: ")
##userWord = userWord.upper()
##for letter in userWord:
##    if letter == "A" or "E" or "I" or "O" or "U":
##        continue
##    else:
##        print(letter)

### step 1
##beatles = []
##print("Step 1:", beatles)
##
### step 2
##beatles.append("John Lennon")
##beatles.append("Paul McCartney")
##beatles.append("George Harrison")
##print("Step 2:", beatles)
##
### step 3
##for i in range(2):
##    x = input("Add a member: ")
##    beatles.append(x)
##print("Step 3:", beatles)
##
### step 4
##del beatles[4]
##del beatles[3]
##print("Step 4:", beatles)
##
### step 5
##beatles.insert(0, "Ringo Starr")
##print("Step 5:", beatles)
##
##
### testing list legth
##print("The Fab", len(beatles))


myList = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
for i in range(len(myList)):
    for j in range(len(myList)):
        if (myList[i] == myList[j] and i != j):
            del myList[i]
print("The list with unique elements only:")
print(myList)
