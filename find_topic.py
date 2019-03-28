topicid = dictionary.token2id.get("energético")
j = 0

while j < (len(corpus)):
 topic_docs = 0
 topic_docs = [idx for token, idx in corpus[j] if token == topicid]
 j += 1
 if (topic_docs):
  print("Aparece en el documento "+str(j-1))
  print(str(topic_docs)+"veces")
  
