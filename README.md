# Social-Science-Miner
This is my final project for my bachelor's degree in Audiovisual Systems Engineering at Universitat Pompeu Fabra (Barcelona, Spain)
Abstract
In this project the trends in Latin American social sciences investigation will be analyzed through natural language processing.
The documents analyzed are the Spanish ponencies from the ALAS(Latin American Sociology Association)congress of 2017 in Montevideo, Uruguay.
The framework for natural language processing the programming language Python and the libraries Spacy and gensim together with other tools 
The aim of this project is to ease the task of scientists that want to study this collection through a better access to the information contained in the ponencies from this congress.

Comments on the code itself
In the Script finals directory there is the Python code, it is not fully optimized and may take some time (about 4 hours or more the part on Topic Modelling).
In the docs_es directory there are the 1004 Spanish documents belonging to the colection and some already trained models for Topic Modelling (lda_1000p_10t, TM25_750p, TM25_1000p) along with an HTML file for displaying directly the result of the execution.
Also, the word dictionary and the corpus in bag-of-words format are already there too.

Before running the code
The programming language used is Python (version 3.7.2)
For the library and imports I used Anaconda (https://anaconda.org/) and I added this libraries apart from the default ones:
dill, ujson
The IDEs that I used were Spyder and Jupyter Notebook.
There were some imports that I could not find in Anacondo which I added directly from the system console:
pip install spacy
pip install stop_words
python -m spacy download es_core_news_sm
pip install wordcloud
pip install pyLDAvis
pip install spacy-langdetect 
python -m spacy download en_core_web_sm
pip install --upgrade gensim (gensim was in Anaconda but only up to version 3.4.2, and i needed to upgrade manually into version 3.7)

#System Description
There are 6 Python scripts 
extract_bibliography (Extracting bibliography of each document, each year appearing there and comparing similarity between bibliographies)
extract_intro (Extracting the introduction of each document)
KeywordFinder3Nouns (Extracting the keyword section of each document)
Metodo(classifying each document by its investigation method into 4 categories: qualitative, quantitative, mixt or undefined) 
load_LDA_model (Loading the corpus and dictionary already filtered and training or loading an LDA Topic Model)
load_topic (Doing the Topic Model process step by step)
