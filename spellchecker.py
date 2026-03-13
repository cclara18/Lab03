import time

import multiDictionary as md
from dictionary import Dictionary
from multiDictionary import MultiDictionary

class SpellChecker:

    def __init__(self):
        self._multiDictionary = MultiDictionary()

        diz_it=Dictionary()
        diz_it.loadDictionary("resources/Italian.txt")

        diz_en=Dictionary()
        diz_en.loadDictionary("resources/English.txt")

        diz_es=Dictionary()
        diz_es.loadDictionary("resources/Spanish.txt")

        self._multiDictionary.addDictionary("italian", diz_it)
        self._multiDictionary.addDictionary("english", diz_en)
        self._multiDictionary.addDictionary("spanish", diz_es)

    def handleSentence(self, scelta, language):
        scelta = scelta.lower()
        scelta = replaceChars(scelta)
        words = scelta.split()
        return self._multiDictionary.searchWord(words, language)

        result = self._multiDictionary.searchWord(words, language)
        return result

    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


def replaceChars(text):
    chars = ".,;:!?()[]{}\"'"

    for c in chars:
        text = text.replace(c, " ")

    return text