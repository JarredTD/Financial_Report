import json

class Get():
    def __init__(self, file) -> None:
        self.file = file

    def transToList(self):
        '''
        Opens file and retrieves a list of all the lines (trans).
        '''
        openedFile = open(self.file, 'r') 
        listOfLines = openedFile.readlines()
        openedFile.close()
        return listOfLines

    def lineCleaner(self, trans, configData):
        '''
        Cleans newline character at end of each line, and splits per delimiter.
        '''
        
        indivTrans = trans.strip('\n').split(configData['Delimiter'])
        return indivTrans

    def transToDict(self, indivTrans, configData):
        '''
        Creates dict for each trans, giving each transInfo a key to access the transInfo value.
        '''
        transDict = {}
        #TODO Make more elegant 
        index = 0
        for dataType in configData['Data_Types']:
            transDict[dataType] = indivTrans[index]
            index += 1

        return transDict
        

def main(file):
    
    get = Get(file)
    transList = get.transToList()
    transDictList = []
    config = open('config\config.json')
    configData = json.load(config)

    for trans in transList:
        indivTrans=get.lineCleaner(trans, configData)
        transDictList.append(get.transToDict(indivTrans, configData))
    
    config.close()
    return transDictList

#main('input\\transactions.txt')
