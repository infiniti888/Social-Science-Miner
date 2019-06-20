#Check the time at the start and at the end of the process, can be commented
import time
ts = time.time()
print(ts)
import datetime
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
print(st)

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
nlp = spacy.load("es_core_news_sm")
# nlp  = spacy.load('es_core_news_sm') #One of the two Spanish models in Spacy trained using Wikipedia data

#Functions for preprocessing data for Topic Modelling, got this two functions from: http://dsgeek.com/2018/02/19/tfidf_vectors.html 
#Keep only tokens with alphabetic characters, no spaces, no punctuation, no stop-words, and no numeric expressions
#and no proper nouns(this last thing was a requirement for my project
def keep_token(t):
    return (t.is_alpha and 
            not (t.is_space or t.is_punct or 
                 t.is_stop or (t.pos_ == "PROPN") or t.like_num))

def lemmatize_doc(doc):
    return [ t.lemma_ for t in doc if keep_token(t) ]
	
#Spacy misses some stop-words so I searched for a second set of stop-words to remove 
from stop_words import get_stop_words
# stop_words = get_stop_words('es') #Spanish stop-words
stop_words = get_stop_words('es') #Portuguese stop-words

#apply the nlp linguistic model and the first two functions 
docs = [lemmatize_doc(nlp(doc)) for doc in array]

filtered_words = [None] * (len(array))
j = 0
while j < (len(array)):
    filtered_words[j] = [i for i in docs[j] if i not in stop_words] #second stop-words filter
    filtered_words[j] = [token for token in filtered_words[j] if len(token) > 5]#filtering tokens with length smaller than 5 gives more meaningful topics
    j += 1
 
#https://radimrehurek.com/gensim/ Gensim a Topic Modelling library 

import gensim

from gensim import corpora, models
from gensim.corpora import Dictionary
#Create a dictionary with each individual word found in the documents
dictionary = corpora.Dictionary(filtered_words)
corpus = []

#Process into bag-of-words(bow) format the documents
corpus = [dictionary.doc2bow(text) for text in filtered_words]
import pickle
#Save the bow corpus and dictionary in files
pickle.dump(corpus, open('corpus.pkl', 'wb'))
dictionary.save('dictionary.gensim')

#Calculate the Latent Dirichlet Allocation system for Topic Modelling, it takes about 4 hours to calculate in my case
lda_model = gensim.models.LdaMulticore(corpus, num_topics=25, id2word=dictionary, passes=1000, decay =0.9, minimum_probability=0)
#Save the model (creates 5 files all starting with the name inside the function
lda_model.save('docs_es_25T_750p')

#https://pyldavis.readthedocs.io/en/latest/ pyLDAvis is a library for creating a visualization for a Topic Modelling
#Beware that the order of topics is not kept as it was in Gensim
import pyLDAvis.gensim
lda_display = pyLDAvis.gensim.prepare(lda_model, corpus, dictionary)
pyLDAvis.display(lda_display)
pyLDAvis.save_html(lda_display, 'docs_pt_25T_1000p.html')

#doctop will store the probability of each document to belonging to a certain topic
doctop=[None] * (len(corpus))
th=0.2
import numpy as np
topicdocs = np.empty(25, dtype=np.object)
#Initialize the numpy array of topics
topicdocs[:] = [1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14], [15], [16], [17], [18], [19], [20], [21], [22], [23], [24], [25]
j=0
#in the loop we will calculate which documents have a probability higher than a threshold of belonging to a certain topic
while j<len(corpus):
    #Save the probability of each topic corresponding to each document
    doctop[j]=[lda_model.get_document_topics(corpus[j], minimum_probability=None, minimum_phi_value=None, per_word_topics=False)]
    i=0
    #only keep the documents above a certain probability threshold(0.2) for the top documents of each topic
    while i<len(doctop[j][0]):
       if doctop[j][0][i][1]>th:
            topicdocs[doctop[j][0][i][0]].append([doctop[j][0][i][1], float(j)])  
       i+=1
    j+=1
    
    

#Top 10 Documents for each topic
for i in range (len(topicdocs)):
    copy=topicdocs[i]#make an auxiliary copy of the list in each iteration
    copy.remove(copy[0])#remove the mark of the topic number
    copy.sort()
    copy.reverse();#sorting in reverse orders them from most probable document to least probable document
    while len(copy)>10:#cut documents until only the top 10 are left
        copy.pop()
    topicdocs[i]=copy
    topicdocs[i] = [[int(topicnumber) for topicprobability,topicnumber in topicdocs[i]]]#return the numbers to integers
    copy=None

#random permutations of a percentage of documents from the corpus will be used as validation for calculating the perplexity metric
perplexity= []
import random
percentage = round(len(corpus)*20/100)
for i in range (100):
    rand = random.randint(0,len(corpus)-percentage)#get random starting points for the validation corpus
    val_corpus = corpus[rand:rand+percentage]#validation corpus goes from the random starting point until that  plus the percentage of the collection that will be used as validation 
    perplexity.append(lda_model.log_perplexity(val_corpus, total_docs=None))#add to the array of perplexities calculated

import numpy as np 
meanperp = np.mean(perplexity)#return the mean of the 100 iterations performed on random validation corpus
print(meanperp)
#Finish time
ts2 = time.time()
print(ts)
print(ts2)
st2 = datetime.datetime.fromtimestamp(ts2).strftime('%Y-%m-%d %H:%M:%S')
print(st)
print(st2)

