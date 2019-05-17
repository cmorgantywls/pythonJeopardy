import requests
import random

#me and all my global variables
score=0
global mythologyChoice
mythologyChoice=[200,400,600,800,1000]
global literatureChoice
literatureChoice=[200,400,600,800,1000]
global foodDrinkChoice
foodDrinkChoice=[200,400,600,800,1000]
global popMusicChoice
popMusicChoice=[200,400,600,800,1000]
global hodgepodgeChoice
hodgepodgeChoice=[200,400,600,800,1000]
global stupidAnswersChoice
stupidAnswersChoice=[200,400,600,800,1000]
global categoryCode
#idk if this made my life easier but I'm glad I played with it!
#maybe should have just made a variable to hold each as a separate dictionary from the start so it could be treated more like an object?
categoryCode = [
    {"category":"mythology","code":135,"list":mythologyChoice},{"category":"literature","code":574,"list":literatureChoice},{"category":"foodDrink","code":253,"list":foodDrinkChoice},
    {"category":"popMusic","code":195,"list":popMusicChoice},{"category":"hodgepodge","code":227,"list":hodgepodgeChoice},{"category":"stupidAnswers","code":301,"list":stupidAnswersChoice}
    ]

response = requests.get('http://jservice.io/api/clues?category=139').json()
playGame = True

#me and all my functions

def isItThere(target,list):
    found = False
    for each in list:
        if each == target:
            found = True
    return found

#get and return category
def getCategory():
    correctChoice = False
    
    while correctChoice==False:
        #this could be smoother but I just don't have time for it rn
        userChoice=input("What category would you like?\n1: Mythology\n2: Literature\n3:Food and Drink\n4:Pop Music\n5: Hodgepodge\n6:Stupid Answers\n")
        if userChoice.lower()=="mythology" or userChoice.lower()=="1" or userChoice.lower()==1 and len(mythologyChoice)>0:
            theCategory = categoryCode[0]["category"]
            correctChoice=True
            print(f"You chose {theCategory}.")
            return theCategory
        elif userChoice.lower()=="literature" or userChoice=="2" or userChoice==2 and len(literatureChoice)>0:
            theCategory=categoryCode[1]["category"]
            correctChoice=True
            print(f"You chose {theCategory}.")
            return theCategory
        elif userChoice.lower()=="food and drink" or userChoice=="3" or userChoice==3 and len(foodDrinkChoice)>0:
            correctChoice=True
            theCategory=categoryCode[2]["category"]
            print(f"You chose {theCategory}.")
            return theCategory
        elif userChoice.lower()=="pop music" or userChoice=="4" or userChoice==4 and len(popMusicChoice)>0:
            correctChoice=True
            theCategory=categoryCode[3]["category"]
            print(f"You chose {theCategory}.")
            return theCategory
        elif userChoice.lower()=="hodgepodge" or userChoice=="5" or userChoice==5 and len(hodgepodgeChoice)>0:
            correctChoice=True
            theCategory=categoryCode[4]["category"]
            print(f"You chose {theCategory}.")
            return theCategory
        elif userChoice.lower()=="stupid answers" or userChoice=="6" or userChoice==6 and len(stupidAnswersChoice)>0:
            correctChoice=True
            theCategory=categoryCode[5]["category"]
            print(f"You chose {theCategory}.")
            return theCategory
        else:
            print("Sorry, that is not a valid answer choice.\nPlease enter either the number or name of your category.")
            userChoice=input("What category would you like?\n1: Mythology\n2: Literature\n3:Food and Drink\n4:Pop Music\n5: Hodgepodge\n6:Stupid Answers\n")

def listAndGetPts(category):
    goodChoice = False
    for points in categoryCode[category]["list"]:
            print(points)
    while goodChoice == False:
        thePoints=int(input(" "))
        wellIsIt=isItThere(thePoints,categoryCode[category]["list"])
        
        if wellIsIt == True:
            goodChoice==True
            print(f"Get ready for your {thePoints} question.")
            return thePoints
        else:
            print("Sorry, that option is unavailable. Look at your options again and only enter a numeric value:\n")
            for points in categoryCode[category]["list"]:
                print(points)
            thePoints=int(input(" "))
            wellIsIt=isItThere(thePoints,categoryCode[category]["list"])
            
            
#get and return point value
def getPoints(category):
    #I know this could be simplified too but I would need to make a function to select and return the list based on each category and just UGH
    print("What point value would you like?")
    if category == "mythology":
        thePoints = listAndGetPts(0)
    elif category=="literature":
        thePoints = listAndGetPts(1)
    elif category=="foodDrink":
        thePoints = listAndGetPts(2)
    elif category=="popMusic":
        thePoints = listAndGetPts(3)
    elif category=="hodgepodge":
       thePoints = listAndGetPts(4)
    elif category=="stupidAnswers":
        thePoints = listAndGetPts(5)
    return thePoints
    

def updatePointValues(category,pointValue):
    if category=="mythology":
        global mythologyChoice
        mythologyChoice.remove(int(pointValue))
    elif category=="literature":
        global literatureChoice
        literatureChoice.remove(int(pointValue))
    elif category=="foodDrink":
        global foodDrinkChoice
        foodDrinkChoice.remove(int(pointValue))
    elif category=="popMusic":
        global popMusicChoice
        popMusicChoice.remove(int(pointValue))
    elif category=="hodgepodge":
        global hodgepodgeChoice
        hodgepodgeChoice.remove(int(pointValue))
    elif category=="stupidAnswers":
        global stupidAnswersChoice
        stupidAnswersChoice.remove(int(pointValue))
    
#getQuestion

def getQuestion(position, pointValue):
    #this would be way more efficient if I made a dictionary of categories:their number in the API but I'm doing this while I'm teaching so this is what we get for now.
    #I recognize there is a lot of abstraction and that means there is always room for a function.
    if position=="mythology":
        theQuestions=requests.get(f'http://jservice.io/api/clues?category={categoryCode[0]["code"]}&value={pointValue}').json()
    elif position=="literature":
        theQuestions=requests.get(f'http://jservice.io/api/clues?category={categoryCode[1]["code"]}&value={pointValue}').json()
    elif position=="foodDrink":
        theQuestions=requests.get(f'http://jservice.io/api/clues?category={categoryCode[2]["code"]}&value={pointValue}').json()
    elif position=="popMusic":
        theQuestions=requests.get(f'http://jservice.io/api/clues?category={categoryCode[3]["code"]}&value={pointValue}').json()
    elif position=="hodgepodge":
        theQuestions=requests.get(f'http://jservice.io/api/clues?category={categoryCode[4]["code"]}&value={pointValue}').json()
    elif position=="stupidAnswers":
        theQuestions=requests.get(f'http://jservice.io/api/clues?category={categoryCode[5]["code"]}&value={pointValue}').json()
    randomQ = random.randint(0,len(theQuestions))
    currentQ=theQuestions[randomQ]
    return currentQ

#get Answer if correct return true, else return false
def getAnswer(currentQ):
    theAnswer=input(f'{currentQ["question"]}\n')
    if theAnswer.lower()==currentQ["answer"].lower():
        print("Nice job!")
        return True
    else:
        print(f'Sorry, that is incorrect. The correct answer was {currentQ["answer"]}.')
        return False
        
#update score based on the answer
def updateScore(answer,pointValue,score):
    if answer==True:
        score+=int(pointValue)
        print(f"You earned {pointValue}. Your score is {score}.")
        return score
    else:
        print(f"You earned 0. Your score is {score}.")
        return score
        
#get and ask question, update score.
def playRound(category,pointValue,score):
        currentQ = getQuestion(category,pointValue)
        ansYorN=getAnswer(currentQ)
        score=updateScore(ansYorN,pointValue,score)
        return score

def keepPlaying():
    gotResponse = False
    while gotResponse==False:
        userResponse=input("Enter Y to play another round or N to exit.")
        if userResponse.lower() == "y":
            print("Okay, get ready for another round!")
            gotResponse=True
            return True
        elif userResponse.lower() == "n":
            print("Thanks for playing! Goodbye!")
            gotResponse=True
            return False
        else:
            print("I'm sorry, I don't understand that command.")
            userResponse=input("Enter Y to play another round or N to exit.")

#actual game code begins below here lalalalala

print("Welcome to Jeopardy!")

while playGame==True:
    if len(mythologyChoice)==0 and len(literatureChoice)==0 and len(foodDrinkChoice)==0 and len(popMusicChoice)==0 and len(hodgepodgeChoice)==0 and len(stupidAnswersChoice)==0:
        playGame=False
        print(f"You've answered every question! Congratulations - your final score is {score}.")
    
    theCategory=getCategory()
    thePoints=getPoints(theCategory)
    updatePointValues(theCategory,thePoints)
    score = playRound(theCategory,thePoints,score)
    playGame=keepPlaying()

