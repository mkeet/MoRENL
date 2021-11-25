from NumberVerbaliser import NumberVerbaliser
from NounClassifier import NounClassifier
from NounData import NounData

class NumberContextControl:

    def __init__(self, *arguments):
        self.number = int(arguments[0])
        if (len(arguments))>1:
            self.noun = arguments[1].lower()
            self.numberType = arguments[2].lower()

    def verbaliseWithout(self):
        numberVerbaliser = NumberVerbaliser(self.number)
        numberAsString = numberVerbaliser.constructNumber()

        #For numbers less than and equal to five, remove the "ku" prefix
        if  (self.number>=1 and self.number <=5):
            numberAsString = numberAsString[2:]

        return numberAsString
    
    def verbaliseWith(self):
        numberVerbaliser = NumberVerbaliser(self.number)
        numberAsString = numberVerbaliser.constructNumber()

        nounClassifier = NounClassifier(self.noun)
        nounData = nounClassifier.getNounData()
        relativeNoun = self.getRelativePronoun(self.noun)

        if (self.numberType[0]== "o"):
            ordinalNumber = self.constructOrdinalNumber(nounData,self.number,numberAsString)
            return ordinalNumber
        else:
            cardinalNumber = self.constructCardinalNumber(relativeNoun,nounData,self.number,numberAsString)
            return cardinalNumber
        
    

    def constructCardinalNumber(self,relativeNoun,nounData,number,numberAsString):

        personalNoun = nounData.get_personalNoun()
        prefix = nounData.get_prefix()
        nounClass = nounData.get_nounClass()

        # print(numberAsString)
        # print(personalNoun)
        # print(prefix)
        # print(nounClass)
        
        specialPrefix = ""
        finalNumber = ""

        #individuals numbers less than and equal to five, remove the "ku" prefix
        if  (number>=1 and number <=5):
            numberAsString = numberAsString[2:]
        
        
        #Rule 1: Bili, tatu and hlanu prefix "ma" and "mi" when they qualify "ama" and "imi" nouns
        if ((prefix=="ama" or prefix=="imi") and (numberAsString=="bili" or numberAsString=="tatu" or numberAsString=="hlanu")):
            specialPrefix = prefix[1:] #remove the first letter
        
        # Rule 2: Bili prefixes “m” after the pronoun “zi” and the conjunction “na” 
        elif (numberAsString=="bili" and personalNoun=="zi"):
            specialPrefix = "m"
        
        #Rule 3: Tatu and hlanu prefix “n” after the pronoun “zi” and the conjunction 'na'
        elif((numberAsString=="tatu" or numberAsString=="hlanu") and (personalNoun=="zi")):
            specialPrefix = "n"
        
        # Rule 4 : The prefixes "mu" or "mi" or "ma" when qualifying noun beginning with "Umu", "imi" or "ama".
        elif ((prefix=="ama" or prefix=="imi" or prefix=="umu") and numberAsString=="ne"):
            specialPrefix = prefix[1:] #remove the first letter
        
        #  Rule 5, From observation ,If numberAsString starts with i, prefix y after the pronoun
        elif(numberAsString[0]=='i'):
            specialPrefix = "y"
        
        # Rule 6, Also from observation : If number starts with a and the relative noun is an e
        elif (numberAsString[0]=='a' and relativeNoun =='e'):
            specialPrefix = "ng"
        

        
        # Rule 7: odwa vs nye, odwa often used for single objects in each class with slight variations for that class
        possessiveParticles = ["y","l","y","s","w","l","b","k"]
        if (number==1 and nounData.get_singular()):
            if(nounClass==1):
                #class 1, uses an e instead of o to combine the innerprefix and the 'dwa'
                numberAsString = possessiveParticles[nounClass-1] + "e" + "dwa"
            
            else:
                numberAsString = possessiveParticles[nounClass-1] + "o" + "dwa"

        
        # rule 8 if two vowels(relative and pronoun) ,discard the pronoun vowel
        if ( personalNoun!="a" and personalNoun!="u" and personalNoun!="i"):
            #Do not discard pronoun
            finalNumber = relativeNoun+personalNoun+specialPrefix+numberAsString
        else:
            #discard pronoun
            #print(specialPrefix)
            finalNumber = relativeNoun+specialPrefix+numberAsString
            if (numberAsString[0]=='a' and relativeNoun=='a'):
                finalNumber = specialPrefix+numberAsString
            
        return finalNumber


        #Ordinal number construction
        #Confirm the rules with linguist or isiZulu speakers, worked of assumptions as textbook very vague
        

    def constructOrdinalNumber(self,nounData,number,numberAsString):
        possessiveParticle = ""
        finalNumber = ""
        nounClass = nounData.get_nounClass()
        
        possesiveParticles = ["w","l","y","s","w","lw","b","kw"]
                
        #Rule 1
        #remove the ku prefix and replace the isi prefix for numbers 1-5
            
        if(number>=1 and number<=5):
            numberAsString = "isi"+numberAsString[2:]
        #Rule 2
        #If number =1 change the root to ukuqala
            
        if (number==1):
            numberAsString = "ukuqala"
            
    
        #Rule 3
        #get the relative pronoun using the number as a noun.
        #Why are we not sending the both possesive and the number, by default class relative pronoun
        #assumes final vowel is a which is the case here.
        relPronoun = self.getRelativePronoun(numberAsString)
        
        #Rule 4
        #remove the first letter of the number, isiZulu rule to never have consecutive vowels
        #all numbers will start with vowels, isi prefix added to individual numbers except 1, and 
        #by default numbers greater than or equal to 10 start with either i or a
            
        numberAsString = numberAsString[1:]
        
        #Rule 5
        #Choose correct prefix option, and add the relative pronoun to that prefixOption to form the prefix of the overall number
            

        possessiveParticle = possesiveParticles[nounClass-1] + relPronoun
        finalNumber = possessiveParticle+numberAsString

        return finalNumber 

    def getRelativePronoun(self,noun):
        firstLetter = noun[0]
        if (firstLetter == "a"):
            return "a"
        elif (firstLetter == "i"):
            return "e"
        elif (firstLetter == "u"):
            return "o"
        else:
            return "a"