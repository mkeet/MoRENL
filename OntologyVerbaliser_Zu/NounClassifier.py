from typing import Collection
from NounData import NounData

class NounClassifier:

    
    def __init__(self, noun):
        self.noun = noun
        self.nounsOfPeople = ["umuntu","ubaba","ubhuti","umfana","umntwana","umngane"]

    def getNounData(self):
        firstLetter = self.noun.lower()[0]

        if (firstLetter=="a"):
            return self.aPrefixes(self.noun)
        elif (firstLetter=="o"):
            return self.oPrefixes(self.noun)
        elif (firstLetter=="i"):
            return self.iPrefixes(self.noun)
        elif (firstLetter=="u"):
            return self.uPrefixes(self.noun)
    

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
    
    def aPrefixes (self, noun):
        if (noun[:3] == "aba"): #class 1
            return NounData(1,"aba","ba",False)
        elif (noun[:3] == "ama"): #class 2
            return  NounData(2, "ama","a",False)
        else:
            return NounData(0)
    def oPrefixes (self,noun):
        #beginning with o, all fall into class 1
        return  NounData(1, "aba","ba",False)
    def iPrefixes (self,noun):
        if (noun[:4]=="izim" or noun[:4] == "izin"):
            #classes 3 or 6, indeterminant : Plural
            return NounData(36, noun[:4],"zi",False)
        
        elif (noun[:3]=="imi"):
            #class 5 : Plural
            return NounData(5, "imi","i",False)
        
        elif(noun[:3] == "izi" and  (noun[:4]!="izim" or noun[:4]!="izin" )):
            #class 4 : Plural
            return  NounData(4, "izi","zi",False)
        elif(noun[:2]=="im" or noun[:2]=="in"):
            # class 3 : Singular
            return NounData(3, noun[:2],"i",True)
        elif(noun[:3] == "isi" ):
            # class 4 : Singular
            return NounData(4, noun[:2],"si",True)
        else:
            """
             * If singular and does not start with either im,in or isi
             * Class 2: Singular
             * Problem with determining prefix, textbook implies it will either be i or ili
            """
            if (noun[:3]=="ili"):
                return NounData(2,"ili","li",True)
            else:
                return NounData(2,"i","li",True)
        
    def uPrefixes(self,noun):
        """
         * class 1
         * consists of people, words of foreign origin and words beginning with the prefix uno (first else if statement)
         * Cant possibly know all nouns for people, so create array of few which will be sufficient for DAFT
         * foreign words will be ignored, lot of unnecessary work determining origin of word
        """
        if((noun[:3]=="umu" or noun[:2]=="um" or noun[:1]=="u") and self.inPeople(noun)):
            if(noun[:3]=="umu"):
                return NounData(1, "umu","u",True)
            
            elif(noun[:2]=="um"):
                return NounData(1, "um","u",True)
            
            else:
                return NounData(1, "u","u",True)
        
        elif( noun[:3]=="uno"):
            return NounData(1, "uno","u",True)
        
        """ class 5
            if u is followed by m and it is not a person or a foreign word
        """
        if(noun[:2]=="um"  and self.inPeople(noun) == False):
            return NounData(5, "um","u",True)
        #class 7        
        elif(noun[:3]=="ubu"):
            return NounData(7, "ubu","bu",True)
        #class 8 
        elif(noun[:3]=="uku"):
            return NounData(8, "uku","ku",True)
        #class 6
        else: 
            if (noun[:3]=="ulu"):
                return NounData(6, "ulu","lu",True)
            else:
                return NounData(6, "u","lu",True)

    def inPeople(self,noun):
       return noun in self.nounsOfPeople 