# import get // Testing purposes

class Data():
    def __init__(self, transDictList) -> None:
        self.transDictList = transDictList

    def transTypeSeperator(self, transType):
        '''
        Appends every trans for a specific transType into transTypeDictList.
        Returns the transTypeDictList.
        '''
        transTypeDictList=[]
        #TODO Fix references to Category from transType, to Category
        for trans in self.transDictList:
            if trans['Category'] == transType:
                transTypeDictList.append(trans)
        return transTypeDictList
        

#TODO Once setup, use the exported transTypeList from get.py rather than creating the list in the main function.
def main(transDictList):
    data = Data(transDictList)
    transTypeDict={}
    transTypeList=['Restaurants'] # i.e, don't do this manually.

    #TODO Put each in its own spot as it occurs, rather than iterating through so many times? 
    for transType in transTypeList:
        transTypeDict[transType]=data.transTypeSeperator(transType)
    print(transTypeDict)



# main(get.main('transData\\transactions.txt')) // Testing purposes




