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

#Tool for searching specific tokens in a document to determine where to end extracting
from spacy.matcher import PhraseMatcher
matcher = PhraseMatcher(nlp.vocab)
terminology_list = ['1', 'RESUMEN', 'Resumen']
patterns = [nlp.make_doc(text) for text in terminology_list]
matcher.add('TerminologyList', None, *patterns)
# doc = nlp('1 1 1 RESUMEN')
# print(matcher(doc)



intro= [None]* (len(array))
matches = [None]* (len(array))
i=0
#extract from the beginning until the end of the introduction which is in the Spanish documents a '1' or "Resumen"
while i < len(array):
    intro_bool = 0
    doc = nlp(array[i])
    matches[i] = matcher(doc)
    print('Documento: ' + str(i))
    for match_id, start, end in matches[i]:
        if intro_bool == 0:		
            intro[i] = doc[0:start]
            intro_bool = 1
    print(intro[i])
    i +=1



