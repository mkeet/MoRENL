class NounData:

    #def __init__(self, nounClass,prefix,personalNoun,singular):
    def __init__(self, *arguments):
        self.nounClass = arguments[0]
        if (len(arguments))>1:
            self.prefix = arguments[1]
            self.personalNoun = arguments[2]
            self.singular = arguments[3]
 
    
     # getter methods
    def get_nounClass(self):
        return self.nounClass

    def get_prefix(self):
        return self.prefix

    def get_personalNoun(self):
        return self.personalNoun
          
    def get_singular(self):
        return self.singular
      
    # setter methods
    def set_nounClass(self, nc):
        self.nounClass = nc
    def set_prefix(self, prfx):
        self.prefix = prfx
    def set_PersonalNoun(self, pn ):
        self.personalNoun = pn
    def set_singular(self, sing):
        self.singular = sing
        