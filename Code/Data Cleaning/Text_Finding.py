import csv
import os
import pandas as pd
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
stopWords = set(stopwords.words('english'))
wordnet = WordNetLemmatizer()
final=[]

path = 'Data/'
for filename in os.listdir(path):
    if '.DS' not in filename:
        print(filename)
        file = open(path + filename, "r")
        text=file.read()
        tok=text.split()
        word=[words.lower() for words in tok if words.isalpha()]
        wordsFiltered=[]
        for w in word:
            if w not in stopWords:
                w = wordnet.lemmatize(w)
                wordsFiltered.append(w)
        final.append(wordsFiltered)

new_path = 'Akhil Labels/'


for folder in os.listdir(new_path):
    if '.DS'not in folder:
        for filename in os.listdir(new_path + folder + "/"):
            if '.txt' in filename:
                print(new_path + folder + "/" + filename)
                file = open(new_path + folder + "/" + filename, "r")
                text = file.read()
                tok = text.split()
                word = [words.lower() for words in tok if words.isalpha()]
                wordsFiltered = []
                for w in word:
                    if w not in stopWords:
                        w = wordnet.lemmatize(w)
                        wordsFiltered.append(w)
                final.append(wordsFiltered)


new_path_2 = 'Whitehouse/'


for folder in os.listdir(new_path_2):
    if '.DS'not in folder:
        for filename in os.listdir(new_path_2 + folder + "/"):
            if 'Topics' not in filename:
                print(new_path_2 + folder + "/" + filename)
                file = open(new_path_2 + folder + "/" + filename, "r")
                text = file.read()
                tok = text.split()
                word = [words.lower() for words in tok if words.isalpha()]
                wordsFiltered = []
                for w in word:
                    if w not in stopWords:
                        w = wordnet.lemmatize(w)
                        wordsFiltered.append(w)
                final.append(wordsFiltered)


final = []
new_path_3 = 'Test/'
for filename in os.listdir(new_path_3):
    if '.DS' not in filename:
        print(filename)
        file = open(new_path_3 + filename, "r")
        text=file.read()
        tok=text.split()
        word=[words.lower() for words in tok if words.isalpha()]
        wordsFiltered=[]
        for w in word:
            if w not in stopWords:
                w = wordnet.lemmatize(w)
                wordsFiltered.append(w)
        final.append(wordsFiltered)

text = []
for file in final:
    text += [" ".join(file)]

exit(0)
df = pd.DataFrame(text, columns = ['content'])
df.to_csv('Testdata.csv')
