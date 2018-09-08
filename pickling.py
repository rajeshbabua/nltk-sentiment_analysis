import pickle
import numpy as np
import scipy as sp
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.naive_bayes import MultinomialNB, GaussianNB, BernoulliNB
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import SVC,LinearSVC, NuSVC
from nltk.classify import ClassifierI
tra =  fs[:1900]
test = fs[1900:]


############## pickling the classifier and dumping the model#####################
save_cls= open("naivebayes.pickle","wb")
pickle.dump(cls,save_cls)
save_cls.close()


################# loading the classifier 
cls_f = open("naivebayes.pickle","rb")
cls = pickle.load(cls_f)
cls_f.close()

#print ("original:", nltk.classify.accuracy(cls,test)*100)
#cls.show_most_informative_features(15)
