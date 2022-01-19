import get
import json

class Clean():
    def __init__(self, transDictList) -> None:
        pass

    def removeDataType(self, trans, dataType):
        del trans[dataType]









def main(transDictList):
    clean = Clean(transDictList)
    config = open('config\config.json')
    configData = json.load(config)


    for dataType in configData['Data_Types_Remove']:
        for trans in transDictList:
            clean.removeDataType(trans, dataType)

    return transDictList


#main(get.main(('input\\transactions.txt')))