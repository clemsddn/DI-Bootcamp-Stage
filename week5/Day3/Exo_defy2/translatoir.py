from translate import Translator
translator= Translator(from_lang="fr", to_lang="en")
french_words= ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"] 
transDict={}
for word in french_words:
    translation = translation = translator.translate(word)
    transDict[translation]=word
print(transDict)