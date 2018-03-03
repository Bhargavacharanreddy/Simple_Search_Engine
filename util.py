
'''
   utility functions for processing terms

    shared by both indexing and query processing
'''
from nltk.corpus import stopwords
from nltk.stem import *
from nltk.stem.porter import *

def isStopWord(word):

      if word in open('stopwords').read():
         return True
      else:
         return False



def stemming(word):
    stemmer= PorterStemmer()
    return stemmer.stem(word)




