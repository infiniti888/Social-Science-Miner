
nlp  = spacy.load('es_core_news_sm')
from spacy.matcher import PhraseMatcher
nlp  = spacy.load('es_core_news_sm')
matcher = PhraseMatcher(nlp.vocab)
terminology_list = ['Bibliografía', 'BIBLIOGRAFÍA']
patterns = [nlp.make_doc(text) for text in terminology_list]
matcher.add('TerminologyList', None, *patterns)

biblio= [None]* (len(array))
matches = [None]* (len(array))

i=0
while i < len(array):
 doc = nlp(array[i])
 matches = matcher(doc)
 print('Documento: ' + str(i))
 for match_id, start, end in matches:
     biblio[i] = doc[start:len(doc)]
	 
 i +=1

from difflib import SequenceMatcher

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()
	
#para comparar las bibliografías 
similar(str(biblio[0]), str(biblio[1]))
referencia_ejemplo ="Arartekos  (2006).  Convivencia  y  conflictos  en  los  centros  educativos,  Informe  extraordinario  delArarteko  sobre  la  situación  en  los  centros  de  Educación  Secundaria  de  la  CAPV.  España,recuperado de http://www.ararteko.net/RecursosWeb/DOCUMENTOS/1/1_244_3.pdf"
similar(str(biblio[0]), str(referencia_ejemplo))



