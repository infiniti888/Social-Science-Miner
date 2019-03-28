#Hacer antes C:\Users\isaac\Desktop\TFG\$ cd ALAS2017.TrabajosCompletos cd Desktop/TFG
doc_count= 0
array=[]
fnames=[]
with open('0012_miguel_alexander_quintanilla.txt', 'rt', encoding='utf-8') as a:
    array = [a.read()]
#    fnames = [a.name]
	
	
# Cargar todos los ficheros txt en el directorio
import glob, os 
for file in glob.glob("*.txt"): 
    print(file)
    with open(file, 'rt', encoding='utf-8') as a:
         array = array + [a.read()] 
#         fnames = fnames + [a.name]#Comentar si no hace falta el nombre de los archivos

#array = array[1:len(array)]
#fnames = fnames[1:len(fnames)]

#import os dir_path = os.path.dirname(os.path.realpath(__file__))

import spacy

nlp  = spacy.load('es_core_news_sm')
#nlp  = spacy.load('es_core_news_md')
#or (t.pos_ == "PROPN") 

def keep_token(t):
    return (t.is_alpha and 
            not (t.is_space or t.is_punct or 
                 t.is_stop or (t.pos_ == "PROPN") or t.like_num))

def lemmatize_doc(doc):
    return [ t.lemma_ for t in doc if keep_token(t) ]
	
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
 
 
 
 
#Tokenizado y extraer stop-words de los documentos ( que estรก cada uno en una array)


import gensim
from gensim import corpora, models
from gensim.corpora import Dictionary
from gensim.models.tfidfmodel import TfidfModel
#from gensim.matutils import sparse2full
dictionary = corpora.Dictionary(filtered_words)
corpus = []

corpus = [dictionary.doc2bow(text) for text in filtered_words]
import pickle
pickle.dump(corpus, open('corpus.pkl', 'wb'))
dictionary.save('dictionary.gensim')
#We are asking LDA to find 5 topics in the data:




# word_counts_tfidf = [[(count, dictionary[id] ) for id, count in line] for line in corpus_tfidf]

#Topic Modelling sin usar tfidf
lda_model = gensim.models.LdaMulticore(corpus, num_topics=30, id2word=dictionary, passes=100, decay =0.5, chunksize = 4, gamma_threshold = 0.01, workers =3)#workers = numero de cores -1
lda_model.save('lda_1500p_30t_param')
# for idx, topic in lda_model.print_topics(-1):
    # print('Topic (sin tf-idf): {} \nWords: {}'.format(idx, topic))

#Topic Modelling usando tfidf
# tfidf = models.TfidfModel(corpus)
# corpus_tfidf = tfidf[corpus]
# lda_model_tfidf = gensim.models.LdaMulticore(corpus_tfidf, num_topics=10, id2word=dictionary, passes=150)#workers = 4
# for idx, topic in lda_model_tfidf.print_topics(-1):
    # print('Topic (usando tf-idf): {} Word: {}'.format(idx, topic))
	
# dictionary = gensim.corpora.Dictionary.load('dictionary.gensim')
# corpus = pickle.load(open('corpus.pkl', 'rb'))

import pyLDAvis.gensim
lda_display = pyLDAvis.gensim.prepare(lda_model, corpus, dictionary)
pyLDAvis.display(lda_display)
pyLDAvis.save_html(lda_display, 'lda_1500p_30t_param.html')
#pyLDAvis.show(lda_display)
#ctrl-C para salir	
	
	
# j=0#print palabras tfidf ordenadas por documentos y por orden descendente de tfidf
# while j < (len(docs)):
 # print('Documento', j)
 # print(sorted(word_counts_tfidf[j], key=None, reverse=True)) 
 # j += 1
 
#Imprime todo el diccionario y su tfidf ordenado por numero
#from pprint import pprint
#for doc in corpus_tfidf:
#    pprint(doc)