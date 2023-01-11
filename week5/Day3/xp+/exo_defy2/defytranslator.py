from translate import Translator
translator= Translator(to_lang="en")
translation = translator.translate("bonjour")
print(translation)
french_words= ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"] 
transDict={}
"""for word in french_words:
    translation = translator.translate(word)
    transDict[translation]=word
print(transDict)"""