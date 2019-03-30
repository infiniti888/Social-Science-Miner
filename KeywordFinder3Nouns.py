doc_count= 0
with open('0012_miguel_alexander_quintanilla.txt', 'rt', encoding='utf-8') as a:
    array = [a.read()]
    fnames = [a.name]
	
	
# Cargar todos los ficheros txt en el directorio
import glob
for file in glob.glob("*.txt"): 
    print(file)
    with open(file, 'rt', encoding='utf-8') as a:
         array = array + [a.read()] 
         fnames = fnames + [a.name]#Comentar si no hace falta el nombre de los archivos

array = array[1:len(array)]
fnames = fnames[1:len(fnames)]

import spacy
from spacy.matcher import PhraseMatcher
nlp  = spacy.load('es_core_news_sm')
matcher = PhraseMatcher(nlp.vocab)
terminology_list = ['Palabras clave', 'Palabras Clave' , 'Palavras-chave', 'Palabras  clave:']
# Only run nlp.make_doc to speed things up
patterns = [nlp.make_doc(text) for text in terminology_list]
matcher.add('TerminologyList', None, *patterns)


matches = [None]* (len(array))
span = [None]* (len(array))
i=0
while i < len(array):
    doc = nlp(array[i])
    matches[i] = matcher(doc)
    print('Documento: ' + str(i))
    for match_id, start, end in matches[i]:
        nouns = 0
        j = start
        j += 1
    while nouns < 3 or j<(end+30):
        j += 1
        if(doc.__getitem__(j).pos_ == "NOUN"):
            nouns+=1
        span[i] = (doc[start:(j)])
        print(span[i])
    i += 1

