import nltk
from nltk.corpus import wordnet
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize,word_tokenize

sys =wordnet.synsets("program")
sys[0].name()
sys[0].lemmas()
sys[0].examples()

synonyms=[]
antonyms=[]


for syn in wordnet.synsets("good"):
   for l in syn.lemmas():
      synonyms.append(l.name())
      if l.antonyms():
           antonyms.append(l.antonyms()[0].name())   
print (set(synonyms))
print (set(antonyms))


########### similarity
w1 = wordnet.synset("cat.n.01")
w2 = wordnet.synset("boat.n.01")
print (w1.wup_similarity(w2))


##################text classifier
from nltk.corpus import movie_reviews
import random

docu = [(list(movie_reviews.words(fileid)),cat)
     for cat in movie_reviews.categories()
     for fileid in movie_reviews.fileids(cat)]
########### shuffle words befor compiling
random.shuffle(docu)
#print(docu[1])


################ 
al_w=[]
for w in movie_reviews.words():
  al_w.append(w.lower())
  
  
al_w = nltk.FreqDist(al_w)
w_f = list(al_w.keys())[:3000]

#print(al_w.most_common(15)) 
#print(al_w["stupid"])

#################################### checking the fequency distrubution of words and its features################
al_w = nltk.FreqDist(al_w)
w_f = list(al_w.keys())[:3000]

def f_f(dcu):
    words = set(dcu)
    features = {}
    for w in w_f:
      features[w] = (w in words)
    return features
print((f_f(movie_reviews.words('neg/cv000_29416.txt'))))
fs = [(f_f(rev), cat) for (rev,cat) in docu]
