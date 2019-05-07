#Check the time at the start and at the end of the process, can be commented
import time
ts = time.time()
print(ts)
import datetime
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
print(st)

array=[]
fnames=[]
with open('0012_miguel_alexander_quintanilla.txt', 'rt', encoding='ISO-8859-1') as a:
    array = [a.read()]
    fnames = [a.name]
	
	
array=[]
fnames=[]	
# Load all the txt files in the directory and save their filenames in another array
import glob
for file in glob.glob("*.txt"): 
    print(file)
    with open(file, 'rt', encoding='ISO-8859-1') as a:
         array = array + [a.read()] 
         fnames = fnames + [a.name]#Comentar si no hace falta el nombre de los archivos

#array = array[1:len(array)]
#fnames = fnames[1:len(fnames)]

#import os dir_path = os.path.dirname(os.path.realpath(__file__))

#https://spacy.io The Spacy library for the dependency parser		 
import spacy
nlp  = spacy.load('es_core_news_sm') #One of the two Spanish models in Spacy trained using Wikipedia data

#Functions for preprocessing data the same as in Topic Modelling, got this two functions from: http://dsgeek.com/2018/02/19/tfidf_vectors.html 
#Keep only tokens with alphabetic characters, no spaces, no punctuation, no stop-words, and no numeric expressions
#proper nouns do not need to be filtered in this case
def keep_token(t):
    return (t.is_alpha and 
            not (t.is_space or t.is_punct or 
                 t.is_stop or t.like_num))

def lemmatize_doc(doc):
    return [ t.lemma_ for t in doc if keep_token(t)]
	
#Spacy misses some stop-words so I searched for a second set of Spanish stop-words to remove
from stop_words import get_stop_words
stop_words = get_stop_words('es')

#apply the nlp linguistic model and the first two functions 
docs = [lemmatize_doc(nlp(doc)) for doc in array]

filtered_words = [None] * (len(array))
j = 0
while j < (len(array)):
    filtered_words[j] = [i for i in docs[j] if i not in stop_words]#second stop-words filter
    j += 1
 
#Tool for searching specific tokens in a document to determine its method of investigation
#The document could use: qualitative method, quantitative method, both (mixt) or undefined given my system
from spacy.matcher import PhraseMatcher
nlp  = spacy.load('es_core_news_sm')
matcher = PhraseMatcher(nlp.vocab)
#The first gazeeteer lists the lemmas of words that determine a quantitative method
cuantiGaz = ['cuantitativo', 'encuestar', 'estadística', 'test', 'regresión', 'cuestionario']
patterns = [nlp.make_doc(name) for name in cuantiGaz]
matcher.add("Names", None, *patterns)

matcher2 = PhraseMatcher(nlp.vocab)
#The second gazeeteer lists the lemmas of words that determine a qualitative method
cualiGaz = ['cualitativo', 'entrevistar']
patterns2 = [nlp.make_doc(name) for name in cualiGaz]
matcher2.add("Names", None, *patterns2)

#two booleans for keeping track if qualitative or quantitative words were found
bool_cuali = 0
bool_cuanti = 0
#4 arrays with the numbers corresponding to its documents
docs_cuali = []
docs_cuanti = []
docs_mixto = []
docs_indefinido = []
i=0
#This loop could be optimized, in my case it took about one hour to finish everything
while i < len(filtered_words):
    bool_cuali = 0
    bool_cuanti = 0
    doc = nlp(str([(words) for words in filtered_words[i]]))
    matches = matcher(doc)
    print('Documento: ' + str(i))
    if(len(matches)>0):
        bool_cuanti = 1
        for match_id, start, end in matches:
            span = doc[start:end]
    matches2 = matcher2(doc)
    i +=1
    if(len(matches2)>0):
        bool_cuali = 1
        for match_id, start, end in matches2:
            span = doc[start:end]
    if(bool_cuali==1 and bool_cuanti==1):
        docs_mixto.append(i)
    else:
        if(bool_cuali):    
            docs_cuali.append(i)
        if(bool_cuanti):    
            docs_cuanti.append(i)
        if(bool_cuali==0 and bool_cuanti==0):
            docs_indefinido.append(i)


#finish time			
ts2 = time.time()
print(ts)
print(ts2)
st2 = datetime.datetime.fromtimestamp(ts2).strftime('%Y-%m-%d %H:%M:%S')
print(st)
print(st2)

