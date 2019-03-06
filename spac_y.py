import re
import pandas as pd
import spacy
from nltk import word_tokenize
df=pd.read_csv("test_sih.csv - Sheet1.csv")

#data processing on table for converting to small letter
df["TAGS"]=df["DESCRIPTION"]
df["DESC_SMALL"]=df["DESCRIPTION"]
for i in range(len(df["DESCRIPTION"])):
    df["DESC_SMALL"][i]=df["DESC_SMALL"][i].lower()
    df["TAGS"][i]=df["TAGS"][i].lower()
    df["TAGS"][i]=re.sub('\W+',' ', df["TAGS"][i])
    df["TAGS"][i]=word_tokenize(df["TAGS"][i])

# Load English tokenizer, tagger, parser, NER and word vectors
nlp = spacy.load('en_core_web_sm')
#custom search for the given data below, so probably you can put a input() function here for search
new=word_tokenize("rubber part kit for 28vb control valve")
doc1 = nlp(str(new))
for i in range(len(df["TAGS"])):
    doc2 = nlp(str(df['TAGS'][i]))
    similarity = doc1.similarity(doc2)
    #Set the threshold based on your importance
    if(similarity>=0.99):
        print(doc1.text, doc2.text, similarity)

