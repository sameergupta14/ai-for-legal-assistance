import glob
import pandas as pd
import numpy as np
import resolve_abbrev
import nltk
from nltk.corpus import stopwords
import string
from tok import word_tokenize
import wordninja
import itertools

punctuations = list(string.punctuation)
stop_words = set(stopwords.words('english'))

def load_data():
  judgements = pd.DataFrame()
  names = ['supreme','calcutta','bombay','bengalore-district','andhra','allahabad']
  for x in names:
      temp = pd.DataFrame()
      txt_files = glob.glob('/data/{}/*.txt'.format(x))

      a = []
      for file in txt_files:
         with open(file) as f:
            text = f.read()
            a.append(text)

      temp['text'] = a
      courts = np.zeros(len(a))
      temp['court'] = courts
      temp['court'] = temp['court'].map(lambda y: x)

      judgements = judgements.append(temp)
  return judgements
  
  
def preprocess():
  judgements['preprocess'] = judgements['text'].map(lambda x: resolve_abbrev.preprocess(x))
  return judgements
    
def clean(x):
  temp = word_tokenize(x)
  temp = [w for w in temp if not w in punctuations]
  temp = [wordninja.split(x) if len(wordninja.split(x)) < 4 else [x] for x in temp]
  temp = list(itertools.chain.from_iterable(temp))
  temp = [w for w in temp if not w in list(stop_words)]
  temp = ' '.join(temp)
  temp = re.sub(r'\b\w{1,2}\b', '', temp)
  temp = word_tokenize(temp)
  return temp
    
 def prepare_data():
  load_data()
  preprocess()
  judgements['clean'] = judgements['preprocess'].map(lambda x: clean(x))
  return judgements

    
    
