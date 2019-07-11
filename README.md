# Social-Science-Miner
This is my final project for my bachelor's degree in Audiovisual Systems Engineering at Universitat Pompeu Fabra (Barcelona, Spain)

# Abstract
In this project a series of scientific articles in the social sciences domains will be
analyzed, using natural language processing.
The documents analyzed are from the ALAS(Latin American Sociology Association) congress of 2017 in Montevideo, Uruguay.
The aim of this project is to ease the task of scientists that want to study this
collection through a better access to the information contained in the papers from this congress.
The focus of the analysis will be in generating a set of tools based on natural
language processing for determining the main topics in the collection and for
doing information extraction.

# Comments on the Directories and what they contain
In the Script finals directory there is the Python code, it is not fully optimized and may take some time depending on the task.
In each of the Documents directories there are the two models used for topic modeling (which also include an HTML for displaying the topics), along with the corpus(in bag-of-words format) and dictionary files produced by the Gensim code from the documents corresponding to each directory's name. The documents in Spanish and Portuguese as how they were separated by Spacy's language detector module are included in each directory in a zip file.
In the Spanish document directories there is also a csv file with information about the authors of each paper and their workgroup.

# Before running the code
The programming language used is Python (version 3.7.2)
For the library and imports I used Anaconda (https://anaconda.org/) and I added this libraries apart from the default ones:
dill, ujson
The IDEs that I used were Spyder and Jupyter Notebook, Spyder is highly recommended for debugging and checking the variables' values. 
There were some imports that I could not find in Anacondo which I added directly from the system console:
pip install spacy
pip install stop_words
python -m spacy download es_core_news_sm
pip install wordcloud
pip install pyLDAvis
pip install spacy-langdetect 
python -m spacy download en_core_web_sm
pip install --upgrade gensim (gensim was in Anaconda but only up to version 3.4.2, and i needed to upgrade manually into version 3.7)
For each file different files need to be in the working directory and will be specified below.

# System description
There are 6 Python scripts 
-load_LDA_model : Loads the corpus and dictionary and trains or loads an LDA Topic Model, the latter is very fast because it does not require loading the whole collection. Also includes the log-perplexity measure of Gensim and topic coherence metric. Then, an array of topic to document relations and document to topics is produced, with an option of filtering only the top 10 documents in each topic and prinitng their titles.
This file only requires having in the working directory the Topic modeling model to be used(composed of a series of files with matching parameter names in the filename), the corpus and the dictonary files.

-load_topic (Doing the Topic Model process step by step from the documents to generate the files used in load_LDA_model).
This file requires having all the documens (unzipped) for either Spanish or Portuguese.

The scripts below use information extraction in a rule-based approach and have been adapted for Spanish only, at the moment.
So for executing them having all or some of the documens (unzipped) in Spanish is required.

-extract_bibliography (Extracting bibliography of each document, each year appearing there and comparing similarity between bibliographies).

-extract_intro (Extracting the introduction of each document).

-KeywordFinder3Nouns (Extracting the keyword section of each document).

-Metodo(classifying each document by its investigation method into 4 categories: qualitative, quantitative, mixt or undefined).
