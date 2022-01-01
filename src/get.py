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


    #TODO Seperate transToDict into two functions; Seperation of functionality.
    def transToDict(self, trans):
        '''
        Seperates transInfo by tab delimiter, cleans new line character at the end.
        Creates dict for each trans, giving each transInfo a key to access the transInfo value.
        '''
        indivTrans = trans.strip('\n').split('\t')
        #TODO Pull this info from a file, use boolean to determine whether to use.
        # Perhaps, create a list from the file, drop false values, iterate through list setting each value from list as a key.

        # i.e for transDataType, index in [transDataTypeList, len(transDataTypeList):
        #       transDict[transDataType] = indivTrans[index]

        # This should set each transDataType as a key in transDict, with each value in indivTrans corresponding with a key.
        # Ideally, this is dynamic, so that changing what transDataTypes you want doesn't break the script.

        transDict = {'Date':indivTrans[0], 'Description':indivTrans[1], 'Amount':indivTrans[3],
                    'Transaction Type':indivTrans[4], 'Category':indivTrans[5], 'Account Name':indivTrans[6]}
        return transDict
        

#TODO Pull transTypes from a file, so that file can be config for what types to use. Use boolean to determine what types to include, this will be exported
# to data.py to determine what types of transactions specifically to do math on.
def main(file):
    get = Get(file)
    transList = get.transToList()
    transDictList = []

    for trans in transList:
        transDictList.append(get.transToDict(trans))
    
    return transDictList

# main()
