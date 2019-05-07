#Check the time at the start and at the end of the process, can be commented
import time
ts = time.time()
print(ts)
import datetime
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
print(st)

#https://radimrehurek.com/gensim/ Gensim a Topic Modelling library 
import gensim
from gensim import corpora, models
from gensim.corpora import Dictionary
import pickle
corpus = []
dictionary=[]
lda_model=[]
#Load the word dictionary and the bag-of-words representation of the corpus
dictionary = Dictionary.load('dictionary.gensim')
corpus=pickle.load(open('corpus.pkl', 'rb'))

#Load an already trained model
# lda_model= gensim.models.LdaMulticore.load('docs_es_25T_750p')


#Calculate the Latent Dirichlet Allocation system for Topic Modelling, it takes about 4 hours to calculate in my case
lda_model = gensim.models.LdaMulticore(corpus, num_topics=25, id2word=dictionary, passes=1000, decay =0.9, gamma_threshold = 0.001, workers = 2)#workers = numero de cores -1
lda_model.save('TM25_750p')
import pyLDAvis.gensim
lda_display = pyLDAvis.gensim.prepare(lda_model, corpus, dictionary)
pyLDAvis.display(lda_display)
pyLDAvis.save_html(lda_display, 'TM25_1000p.html')


#doctop will store the probability of each document to belonging to a certain topic
doctop=[None] * (len(corpus))
th=0.2
import numpy as np
topicdocs = np.empty(25, dtype=np.object)
topicdocs[:] = [1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14], [15], [16], [17], [18], [19], [20], [21], [22], [23], [24], [25]
j=0
#in the loop we will calculate which documents have a probability higher than a threshold of belonging to a certain topic
while j<len(corpus):
    doctop[j]=[lda_model.get_document_topics(corpus[j], minimum_probability=None, minimum_phi_value=None, per_word_topics=False)]
    i=0
    while i<len(doctop[j][0]):    
        if doctop[j][0][i][1]>th:   
            topicdocs[doctop[j][0][i][0]].append(j)  
        i+=1
    j+=1
	
#The first 20% of the corpus will be used as validation for calculating the perplexity metric
val_corpus = corpus[0:50] 
perplexity = lda_model.log_perplexity(val_corpus, total_docs=None)

#Finish time
ts2 = time.time()
print(ts)
print(ts2)
st2 = datetime.datetime.fromtimestamp(ts2).strftime('%Y-%m-%d %H:%M:%S')
print(st)
print(st2)









