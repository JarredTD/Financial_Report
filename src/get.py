class Get():
    def __init__(self, file) -> None:
        self.file = file

    def transToList(self):
        openedFile = open(self.file, 'r')
        listOfLines = openedFile.readlines()
        openedFile.close()
        return listOfLines

    def transToDict(self, trans):
        indivTrans = trans.strip('\n').split('\t')
        transDict = {'Date':indivTrans[0], 'Description':indivTrans[1], 'Amount':indivTrans[3],
                    'Transaction Type':indivTrans[4], 'Category':indivTrans[5], 'Account Name':indivTrans[6]}
        return transDict
        

def main():
    get = Get('transData/transactions.txt')
    transList = get.transToList()
    transDictList = []

    for trans in transList:
        transDictList.append(get.transToDict(trans))
    
    return transDictList

main()