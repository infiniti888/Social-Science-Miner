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

#Tool for searching specific tokens in a document to determine where to start extracting
from spacy.matcher import PhraseMatcher
matcher = PhraseMatcher(nlp.vocab)
terminology_list = ['Bibliografía', 'BIBLIOGRAFÍA', 'Bibliograf', 'bibliográficas']
patterns = [nlp.make_doc(text) for text in terminology_list]
matcher.add('TerminologyList', None, *patterns)

biblio= [None]* (len(array))
matches = [None]* (len(array))
years = [None]* (len(array))
i=0
#Extract from the start of the bibliography section until the end 
while i < len(array):
    doc = nlp(array[i])
    matches = matcher(doc)#search using the words that indicate the start of the bibliography section
    print('Documento: ' + str(i))
    if(matches):
        for match_id, start, end in matches:
            biblio[i] = doc[end:len(doc)]
        years[i] =[]
        #also will print the tokens corresponding to years, numbers with 4 digits
        for token in biblio[i]:
            if token.like_num and token.shape_ == 'dddd' and int(str(token))<2017:
                years[i].append(int(str(token)))
    else: 
        years[i]=0
        biblio[i]='Error'
    i +=1



