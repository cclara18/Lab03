import dictionary as d
import richWord as rw
from richWord import RichWord


class MultiDictionary:

    def __init__(self):
       self._dictionaries= {}

    def addDictionary(self, language, dictionary):
        self._dictionaries[language] = dictionary

    def printDic(self, language):
        if language in self._dictionaries:
            self._dictionaries[language].printAll()
        else:
            print("lingua non presente")

    def searchWord(self, words, language):
        result=[]
        if language not in self._dictionaries:
            print("lingua non presente")
            return result
        selected_dictionary= self._dictionaries[language].dict
        for word in words:
            rich_word= RichWord(word)
            if word in selected_dictionary:
                rich_word.corretta= True
            else:
                rich_word.corretta= False
                print(word)
            result.append(rich_word)
        return result

    def searchWordLinear(self, word):
        for i in range(len(self.words)):
            if self.words[i] == word:
                return i
        return -1

    def searchWordDichotomic(self, word):
        left = 0
        right = len(self.words) - 1

        while left <= right:
            mid = (left + right) // 2

            if self.words[mid] == word:
                return mid
            elif word < self.words[mid]:
                right = mid - 1
            else:
                left = mid + 1

        return -1

