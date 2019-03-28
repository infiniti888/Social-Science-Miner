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
        punto=0
        j=0
        span[i] = (doc[start:(end+30)])
        j+=1
    while (punto == 0):
        if(not (str(span[i].__getitem__(j)) == ".")):
            j += 1
        else:
            a = span[i]
            span[i]= a[0:j].text
            print(span[i])
            punto = 1
    i += 1
