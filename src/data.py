import get
import json

class Data():
    def __init__(self, transDictList) -> None:
        self.transDictList = transDictList

    def transTypeSeperator(self, category):
        '''
        Appends every trans for a specific Category into transCategoryDictList.
        Returns the transCategoryDictList.
        '''
        transCategoryDictList=[]
        for trans in self.transDictList:
            if trans['Category'] == category:
                transCategoryDictList.append(trans)
        return transCategoryDictList
        

def main(transDictList):
    data = Data(transDictList)
    config = open('config\config.json')
    configData = json.load(config)
    transCategoryDict={}
    

    #TODO Put each in its own spot as it occurs, rather than iterating through so many times? 
    for category in configData['Categories']:
        transCategoryDict[category]=data.transTypeSeperator(category)
    print(transCategoryDict) # Viewing dict, for debugging.

    config.close()



main(get.main('input\\transactions.txt'))




