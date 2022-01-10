import get
import json

class Clean():
    def __init__(self, transDictList) -> None:
        self.transDictList = transDictList

    def removeDataType(self, dataType):
        # Issue is here
        del self.transDictList[dataType]









def main(transDictList):
    clean = Clean(transDictList)
    config = open('config\config.json')
    configData = json.load(config)


    for dataType in configData['Data_Types_Remove']:
        for trans in transDictList:
            clean.removeDataType(dataType)

    return transDictList


#main(get.main(('input\\transactions.txt')))