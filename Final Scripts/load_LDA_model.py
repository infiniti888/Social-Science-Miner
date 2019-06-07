#Check the time at the start and at the end of the process, can be commented
import time
ts = time.time()
import datetime
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

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
lda_model= gensim.models.LdaMulticore.load('ES_TM25_750p')


#Calculate the Latent Dirichlet Allocation system for Topic Modelling, it takes about 4 hours to calculate in my case
#lda_model = gensim.models.LdaMulticore(corpus, num_topics=25, id2word=dictionary, passes=750, decay =0.9, minimum_probability=0)#workers = numero de cores -1
#lda_model.save('es_TM25_750p')
#import pyLDAvis.gensim
#lda_display = pyLDAvis.gensim.prepare(lda_model, corpus, dictionary)
#pyLDAvis.display(lda_display)
#pyLDAvis.save_html(lda_display, 'es_TM25_750p.html')


#doctop will store the probability of each document to belonging to a certain topic
doctop=[None] * (len(corpus))
Sorted_doctop=[None] * (len(corpus))
th=0.2
import numpy as np
topicdocs = np.empty(25, dtype=np.object)
topicdocs[:] = [1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14], [15], [16], [17], [18], [19], [20], [21], [22], [23], [24], [25]
j=0
#in the loop we will calculate which documents have a probability higher than a threshold of belonging to a certain topic
while j<len(corpus):
    doctop[j]=[lda_model.get_document_topics(corpus[j], minimum_probability=None, minimum_phi_value=None, per_word_topics=False)]
    i=0
    a =[None] * (25)
    while i<25:
        a[i]=doctop[j][-1][i][0:2]
        i+=1
    inverselist= sorted(a,key=lambda x: x[1],reverse = True)
    #Sorting the topics of each document by their probability
    Sorted_doctop[j] = [[topicnumber for topicnumber,topicprobability in inverselist]]
    i=0
    while i<len(doctop[j][0]):
       if doctop[j][0][i][1]>th:
            topicdocs[doctop[j][0][i][0]].append([doctop[j][0][i][1], float(j)])  
       i+=1
    j+=1

import csv

array=[]
fnames=[]	
# Load all the txt files in the directory and save their filenames in another array
import glob
for file in glob.glob("*.txt"): 
    print(file)
    with open(file, 'rt', encoding='ISO-8859-1') as a:
         array = array + [a.read()] 
         fnames = fnames + [a.name]
		 
#Top 10 Documents for each topic
for i in range (len(topicdocs)):
    copy=topicdocs[i]
    copy.remove(copy[0])
    copy.sort()
    copy.reverse();
    while len(copy)>10:
        copy.pop()
    topicdocs[i]=copy
    topicdocs[i] = [[int(topicnumber) for topicprobability,topicnumber in topicdocs[i]]]
    copy=None
         
i=0
while i<len(topicdocs):
    print('Topic'+str(i+1))
    j=0
    while j<str(topicdocs[i]).count(',')+1:
        docnum = fnames[topicdocs[i][0][j]][2:6]
        j+=1
        with open('GT_name.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            for row in csv_reader:
                if row[0] == docnum:
                    Titulo = row[2]
                    print(('Name of the document : '+str(Titulo)))
        csv_file.close()
    i+=1

#random permutations of a percentage of documents from the corpus will be used as validation for calculating the perplexity metric
#perplexity= []
#import random
#percentage = round(len(corpus)*5/100)
#for i in range (100=:
#    rand = random.randint(0,len(corpus)-percentage)
#	val_corpus = corpus[rand:rand+percentage]
#	perplexity.append(lda_model.log_perplexity(val_corpus, total_docs=None))

#import numpy as np 
#meanperp = np.mean(perplexity)
#print(meanperp)
#Finish time
ts2 = time.time()
print(ts)
print(ts2)
st2 = datetime.datetime.fromtimestamp(ts2).strftime('%Y-%m-%d %H:%M:%S')
print(st)
print(st2)









