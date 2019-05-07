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
nlp  = spacy.load('es_core_news_sm') #One of the two Spanish models in Spacy trained using Wikipedia data

#Functions for preprocessing data for keyword extraction, got this two functions from: http://dsgeek.com/2018/02/19/tfidf_vectors.html 
#Keep only tokens with alphabetic characters, no spaces, no punctuation, no stop-words, and no numeric expressions
def keep_token_soft(t):
    return (t.is_alpha and 
            not (t.is_space or t.is_punct or 
                 t.is_stop ))

def lemmatize_doc_soft(doc):
    return [ t.lemma_ for t in doc if keep_token_soft(t)]
	
#Spacy misses some stop-words so I searched for a second set of Spanish stop-words to remove
from stop_words import get_stop_words
stop_words = get_stop_words('es')

#apply the nlp linguistic model and the first two functions 
docs = [lemmatize_doc_soft(nlp(doc)) for doc in array]

filtered_words = [None] * (len(array))
j = 0

while j < (len(array)):
    filtered_words[j] = [i for i in docs[j] if i not in stop_words] #second stop-words filter
    j += 1

#Tool for searching specific tokens in a document to determine where to start extracting
from spacy.matcher import PhraseMatcher
matcher = PhraseMatcher(nlp.vocab)
terminology_list = ['Palabras']
patterns = [nlp.make_doc(text) for text in terminology_list]
matcher.add('TerminologyList', None, *patterns)


matches = [None]* (len(array))
span = [None]* (len(array))
i=0
#After finding each starting point for the Keywords section extract until 3 nouns or proper nouns are found
while i < len(array):
    doc = nlp(str([(words) for words in filtered_words[i]]))
    matches[i] = matcher(doc)
    print('Documento: ' + str(i))
    for match_id, start, end in matches[i]:
        nouns = 0
        j = start
        j += 1
    while nouns < 3 or j<(end+30):
        j += 1
        if(doc.__getitem__(j).pos_ == "NOUN" or doc.__getitem__(j).pos_ == "PROPN"):
            nouns+=1
        span[i] = (doc[start+6:(j)])
    print(span[i])
    i += 1
