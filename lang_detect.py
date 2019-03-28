# pip install spacy-langdetect
# python -m spacy download en_core_web_sm
import spacy
from spacy_langdetect import LanguageDetector
nlp = spacy.load("en_core_web_sm")
nlp.add_pipe(LanguageDetector(), name="language_detector", last=True)
array = []
fnames = []

# Cargar todos los ficheros txt en el directorio
import glob, os
for file in glob.glob("*.txt"):
    with open(file, 'rt', encoding='utf-8') as a:
        text = a.read()
        if nlp(text)._.language['language'] == 'es':
            a.close()
            os.rename(file, 'es' + str(file))
        else:
            a.close()
            os.rename(file, 'pt' + str(file))
