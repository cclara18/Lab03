class Dictionary:
    def __init__(self):
        self.__dict =[]


    def loadDictionary(self,path):
        with open (path, "r", encoding="utf-8") as file:
            for line in file:
                word= line.strip()
                if word != "":
                    self.__dict.append(word)

    def printAll(self):
        for word in self.__dict:
            print(word)



    @property
    def dict(self):
        return self.__dict


