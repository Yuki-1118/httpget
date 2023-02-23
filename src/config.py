class config:
    saveEnable = False
    printResponse = False
    
    def __init__(self):
        self.saveEnable = False
        self.printResponse = False
        pass
    
    def __init__(self,saveEnable = False,printResponse = False) :
        self.saveEnable = saveEnable
        self.printResponse = printResponse
        pass
    
    def setSaveEnable(self, bool):
        self.saveEnable = bool
        pass
    
    def setPrintResponse(self, bool):
        self.printResponse = bool
        pass