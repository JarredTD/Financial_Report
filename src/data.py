import json
import clean
import get

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

    def miscTrans(self, trans):
        transCategoryDictList=[]
        transCategoryDictList.append(trans)
        return transCategoryDictList

def main(transDictList):
    data = Data(transDictList)
    config = open('config\config.json')
    configData = json.load(config)
    transCategoryDict={}
    

    #TODO Put each in its own spot as it occurs, rather than iterating through so many times? 
    #This categorizes each transaction based on categories in config
    for category in configData['Categories']:
        transCategoryDict[category]=data.transTypeSeperator(category)


#This logic makes no sense, push non-main logic into the function miscTrans.
    for trans in transDictList:
        try:
            if trans[category] not in configData['Categories']:
                transCategoryDict["Misc"] = data.transTotal(trans)
        except KeyError:
            continue



    config.close()
    return transCategoryDict


#Run this file to test output.
transDictList=get.main('input\\transactions.txt')
cleanedTransDictList=clean.main(transDictList)
transCategoryDict=main(cleanedTransDictList)
print(transCategoryDict)



