import glob

class file_walker():

    def __init__(self, start="/home/coder/Workspace/aktueller-kurs/Teilnehmer/tn11/test/", endung="txt"): 
        self.test = start + "/**/*." + endung
        #print(self.test) 
        
    def search_me(self):
        self.result = []
        self.result = glob.glob(self.test, recursive=True)
       # print(self.result) 
        return self.result
    

#file_walker(endung="jpg")

print(file_walker(endung="jpg").search_me()) 
