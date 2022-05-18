class NumberVerbaliser:
    
    roots = ["qanda","nye","bili","tatu","ne","hlanu","thupha","khombisa","shiyagalombili","shiyagalolunye","shumi","khulu","kulungwane"]
    def __init__(self,inputNumber):
        self.inputNumber = inputNumber

    

    def constructNumber(self):
        intAsString = str(self.inputNumber)
        lengthOfNumber = len(intAsString)
        verbalisedNumber = ""

        #singles 0 - 9
        if (lengthOfNumber==1):
            verbalisedNumber = self.individualNumber(self.inputNumber)
        else:
            firstDigit = True
            for digit in range (lengthOfNumber):
                currentDigit = int(intAsString[0])
                if (digit != lengthOfNumber-1):
                    verbalisedNumber = verbalisedNumber + " " + self.numberClass(currentDigit,len(intAsString), firstDigit)
                    verbalisedNumber = verbalisedNumber + " " + self.multiplierDigit(currentDigit,len(intAsString))
                    intAsString = intAsString[1:]
                else:
                    if (currentDigit!=0):
                        verbalisedNumber = verbalisedNumber + " " + self.compound(currentDigit)
                    else:
                        continue
                
                if (digit==0):
                    firstDigit = False
        return verbalisedNumber.replace("  "," ").strip()


    def individualNumber(self,number):
        prefixes = ["i","ku","isi"]
        prefix = ""
        root = self.roots[number]

        if (number==0):
            prefix = prefixes[0]
        elif (number<=5):
            prefix = prefixes[1]
        else:
            prefix = prefixes[2]
        
        return (prefix+root)
    
    #for numbers not ending in zero
    def compound(self,number):
        prefixes = ["na","nam","nan","nesi"]
        prefix = ""
        root = self.roots[number]

        if (number<=5):
            if(root[0] == "n"):
                prefix = prefixes[0]
            elif (root[0] == "b"):
                prefix = prefixes[1]
            elif (root[0]=="t" or root[0] =="h"):
                prefix = prefixes[2]
        else:
            prefix = prefixes[3]
        return (prefix+root)

    #for plural tens, hundreds and thousands
    def multiplierDigit(self,number,group):
        if (number==1 or number==0):
            return ""
        else:
            prefixes = ["ama","ayisi","ezim","ezin","ezi","eziyisi"]
            prefix = ""
            root = self.roots[number]
            if(group==2 or group==3):
                if(1<number<=5):
                    prefix = prefixes[0]
                else:
                    prefix = prefixes[1]
            elif (group==4):
                if(root[0] == "b"):
                    prefix = prefixes[2]
                elif (root[0]=="t" or root[0] =="h"):
                    prefix = prefixes[3]
                elif (root[0]=="n"):
                    prefix = prefixes[4]
                else:
                    prefix = prefixes[5]
            return prefix+root

    def numberClass(self,number,group,first):
        if (number==0):
            return ""
        else:
            prefixes = ["i","ama","ne","nama","in","izin"]
            prefix =""
            root = ""
            if (group==2 or group==3):
                if (number==1): #one hundred
                    if (first == True):
                        prefix = prefixes[0]
                    else:
                        prefix = prefixes[2]
                else: #multiple hundreds
                    if (first==True):
                        prefix = prefixes[1]
                    else:
                        prefix = prefixes[3]
                if (group==2):
                    root = self.roots[10] #shumi
                #hundreds
                else:
                    root = self.roots[11] #khulu
                return prefix+root
            elif (group==4):
                root = self.roots[12] #kulungwane
                if (number==1): #only one thousand
                    prefix = prefixes[4]
                else: #multiple thousands
                    prefix = prefixes[5]
                return prefix+root
            else:
                return prefix+root





                    
            



