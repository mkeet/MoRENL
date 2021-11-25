from owlready import *


class OntologyExtractor:
    'loads ontology and returns triplets'

    def __init__(self, path, iri):
        onto_path.append(path)
        self.onto_zu = get_ontology(iri).load()

        
        self.my_dict = {}

        with open('propertyExcept.txt', 'r') as f:
            self.SPECIAL_PROPERTIES = f.readlines()
            for i in range(0, len(self.SPECIAL_PROPERTIES)):
                if self.SPECIAL_PROPERTIES[i][-1] == '\n':
                    self.SPECIAL_PROPERTIES[i] = self.SPECIAL_PROPERTIES[i][:-1]

    def getSubclasses(self):
        """
        finds subclasses  of each class in the ontology
        :return: list of subclasses arranged in pairs
        """
        subclasses_pairs = []

        for superclass in self.onto_zu.classes:
            subclasses = [sub.name for sub in \
            self.onto_zu.subclasses_of(superclass) if sub != superclass]

            if len(subclasses) > 0:
                [subclasses_pairs.append((sub, superclass.name)) \
                for sub in subclasses]
        
        return subclasses_pairs

    def getDisjoint(self):
        """
        find disjoints in the ontology
        :return: list of disjoint classes in pairs
        """
        disjoint_pairs = []

        for disjoint_pair in self.onto_zu.all_disjoints:
            disjoint_pairs.append((disjoint_pair.Entities[0].name, \
            disjoint_pair.Entities[1].name))

        return disjoint_pairs

    def getProperties(self):
        dataProperties_pairs = []

        for data_property in self.onto_zu.instances:
            members = [attr for attr in dir(data_property) if not callable(getattr(data_property, attr)) and not attr.startswith("__")]
          
            dataProperties_pairs.append((data_property.name,members[-1],data_property.unyaka[0]))
            
        return dataProperties_pairs
        


    def isValidTriplet(self, superclass, op, sub):
        """
        return: True if the super and subclass classes are in the domain
        and range of the property/operator
        """
        if len(op.domain) == 0 or len(op.range) == 0:
            return True # TODO check if domain and range defined  execute

        for classtype in superclass.is_a:
            if classtype not in op.domain:
                return False

        for classtype in sub.is_a:
            if classtype not in op.range:
                return False

        return True

    def isMassNoun(self, word):
        with open('nncPairs.txt') as f:
            lines = f.readlines()

            for line in lines:
                [w, nc] = line.split(',')
                if w == word:
                    return nc[-2] == 'm'
        return False

    def push(self, key, value):
        try:
            self.my_dict[key].append(value) # TODO remove underscore
            #print("*****",value)
        except:
            self.my_dict[key] = [value]

    def add(self, superclass, op, sub):
        tupl = (superclass, sub)

        if op not in self.SPECIAL_PROPERTIES:
            tupl = (superclass, op, sub)
            op = 'exists'

        elif op == 'ingxenye':
            if self.isMassNoun(superclass) or self.isMassNoun(sub):
                op = 'ingxenye_s' # TODO: check DOLCE
        
        elif op == 'has': #needs to go
            tupl = (superclass, op, sub)
            

        
        self.push(op, tupl)
        return

    def addModified(self, superclass, number,numType ,op, sub):
        tupl = (superclass, sub,number,numType)

        if op not in self.SPECIAL_PROPERTIES:
            tupl = (superclass, op, sub,number,numType) #don't forget this modification
            op = 'exists'

        elif op == 'ingxenye':
            if self.isMassNoun(superclass) or self.isMassNoun(sub):
                op = 'ingxenye_s' # TODO: check DOLCE

        self.push(op, tupl)
        return

    def readRestrictions(self):
        for superclass in self.onto_zu.classes:
            for classtype in superclass.is_a:
                if isinstance(classtype, PropertyValueRestriction):
                    if self.isValidTriplet(superclass, classtype.Prop, \
                    classtype.Class) and not isinstance(classtype.Class, \
                    NotRestriction):
                        members = [attr for attr in dir(classtype.Class) if not callable(getattr(classtype.Class, attr)) and not attr.startswith("__")]
                        try:
                            self.addModified(superclass.name, classtype.cardinality,classtype.type,classtype.Prop.name,classtype.Class.name)
                        except AttributeError:
                            members = [attr for attr in dir(superclass) if not callable(getattr(superclass, attr)) and not attr.startswith("__")]
                            
                            if classtype.Class == int: #if dataproperty
                                self.add(superclass.name, "has",classtype.Prop.name)
                            else: 
                                self.add(superclass.name, classtype.Prop.name, classtype.Class.name)
                            
                            
                            
                            
                    else:
                        self.push('nexist', (superclass.name, \
                        classtype.Prop.name, classtype.Class.Class.name))

                elif isinstance(classtype, AndRestriction):
                    for property in classtype.Classes:
                        if self.isValidTriplet(superclass, property.Prop, \
                        property.Class):
                            self.add(superclass.name, property.Prop.name, \
                            property.Class.name)

                elif isinstance(classtype, NotRestriction):
                    self.push('nexist', (superclass.name, \
                    classtype.Class.Prop.name, classtype.Class.Class.name))

                # elif isinstance(classtype, OperatorRestriction):
                #     print(" OP ",classtype)
                # elif isinstance(classtype, OneOfRestriction):
                #     print(" ONE_OF ",classtype)
                # elif isinstance(classtype, Restriction):
                #     print(" RES ",classtype)
                else:
                    pass

    def extract(self):
        self.readRestrictions()
        self.my_dict['subclasses'] = self.getSubclasses()
        self.my_dict['disjoint'] = self.getDisjoint()
        # self.my_dict['unyaka'] = self.getProperties()
        
