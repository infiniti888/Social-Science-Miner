doc_count= 0
array=[]
fnames=[]
with open('0012_miguel_alexander_quintanilla.txt', 'rt', encoding='utf-8') as a:
    array = [a.read()]
    fnames = [a.name]
	
	
# Cargar todos los ficheros txt en el directorio
import glob, os 
for file in glob.glob("*.txt"): 
    print(file)
    with open(file, 'rt', encoding='utf-8') as a:
         array = array + [a.read()] 
         fnames = fnames + [a.name]#Comentar si no hace falta el nombre de los archivos

array = array[1:len(array)]
fnames = fnames[1:len(fnames)]

#import os dir_path = os.path.dirname(os.path.realpath(__file__))

import spacy

nlp  = spacy.load('es_core_news_sm')
#nlp  = spacy.load('es_core_news_md')

def keep_token(t):
    return (t.is_alpha and 
            not (t.is_space or t.is_punct or 
                 t.is_stop or t.like_num))

def lemmatize_doc(doc):
    return [ t.lemma_ for t in doc if keep_token(t)]
	
#Antes cargar documentoset_stop_words
from stop_words import get_stop_words
stop_words = get_stop_words('es')

#import random
docs = [lemmatize_doc(nlp(doc)) for doc in array]

filtered_words = [None] * (len(array))
j = 0

while j < (len(array)):
 filtered_words[j] = [i for i in docs[j] if i not in stop_words] 
 filtered_words[j] = [token for token in filtered_words[j] if len(token) > 5]#quita los stop-word que se cuelan y algun nombre propio
 j += 1
 