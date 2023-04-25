"""NLP utilities"""
import nltk
import itertools
import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt
from tqdm import tqdm
from wordcloud import WordCloud
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist

def process_text(path2):
    df = pd.read_csv(path2)
    descrip_lst = df['job_descrip'].tolist()
    return descrip_lst

def clean_lst(descrip_lst):
    clean_lst = []
    clean_lst_2 = []
    lemmatizer = WordNetLemmatizer()
    for i in tqdm(range(len(descrip_lst))):
        try:
            descrip_lst[i] = word_tokenize(descrip_lst[i])
            clean_lst.append(descrip_lst[i])
        except:
            continue
    clean_lst = list(itertools.chain.from_iterable(clean_lst))

    for i in tqdm(range(len(descrip_lst))):
        for j in descrip_lst[i]:
            if j.isalpha() and j not in stopwords.words('english'):
                clean_lst_2.append(lemmatizer.lemmatize(j))
    return clean_lst_2  

def wc(clean_lst_2):
    clean_lst_2 = " ".join(clean_lst_2)
    wordcloud = WordCloud(width = 800, height = 800, background_color = "white", min_font_size = 10).generate(clean_lst_2)
    plt.figure(figsize = (8, 8), facecolor = None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad = 0)
    plt.show()
