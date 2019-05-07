array=[]
fnames=[]	
# Load all the txt files in the directory and save their filenames in another array
import glob
for file in glob.glob("*.txt"): 
    print(file)
    with open(file, 'rt', encoding='utf-8') as a:
         array = array + [a.read()] 
         fnames = fnames + [a.name]

#https://spacy.io The Spacy library for the dependency parser		 
import spacy
nlp  = spacy.load('es_core_news_sm') #One of the two Spanish models in Spacy trained using Wikipedia data

#Tool for searching specific tokens in a document to determine where to start extracting
from spacy.matcher import PhraseMatcher
matcher = PhraseMatcher(nlp.vocab)
terminology_list = ['Bibliografía', 'BIBLIOGRAFÍA']
patterns = [nlp.make_doc(text) for text in terminology_list]
matcher.add('TerminologyList', None, *patterns)

biblio= [None]* (len(array))
matches = [None]* (len(array))
i=0
#Extract from the start of the bibliography section until the end 
while i < len(filtered_words):
    doc = nlp(array[i])
    matches = matcher(doc)
    print('Documento: ' + str(i))
    for match_id, start, end in matches:
        biblio[i] = doc[start:len(doc)]
    year = 0
    #also will print the tokens corresponding to years, numbers with 4 digits
    for token in biblio[i]:
        if token.like_num and token.shape_ == 'dddd':
            print(token)
    i +=1

#This tool can compare how similar are 2 given bibliography strings, in general the numbers are very small
from difflib import SequenceMatcher
SequenceMatcher(None, str(biblio[0]), str(biblio[1])).ratio()





