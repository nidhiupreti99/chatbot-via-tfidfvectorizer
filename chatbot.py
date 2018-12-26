# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 19:46:36 2018

@author: Nidhi
"""

import nltk
import numpy as np
import random
import string

f=open('chatbot.txt','r', errors='ignore')
raw=f.read()
raw=raw.lower()
nltk.download('punkt')
nltk.download('wordnet')
sent_tokens=nltk.sent_tokenize(raw)
word_tokens=nltk.word_tokenize(raw)
lemmer=nltk.stem.WordNetLemmatizer()
def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]
remove_punct_dict=dict((ord(punct),None) for punct in string.punctuation)
def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))
greeting_inputs=["hello","hi", "greetings", "sup", "what's up", "hey"]
greeting_responses = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]
def greeting(sentence):
    for word in sentence.split():
        if word.lower() in greeting_inputs:
           
            return random.choice(greeting_responses)
        
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
def response(user_response):
    robo_response=''
    sent_tokens.append(user_response)
    TfidfVec=TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf=TfidfVec.fit_transform(sent_tokens)
    vals=cosine_similarity(tfidf[-1],tfidf)
    idx=vals.argsort()[0][2]
    flat=vals.flatten()
    flat.sort()
    req_idf=flat[-2]
    if req_idf==0:
        robo_response+='sorry i cannot understand'
        return robo_response
    else:
        robo_response+=sent_tokens[idx]
        return robo_response
flag=True
print("ROBO:hello , my name is robo. how can i help you? to exit type tata")
while flag==True:
    user_response=input()
    user_response=user_response.lower()
    if(user_response!='bye'):
        
        if(user_response=='thanks' or user_response=='thank you'):
            print('ROBO: u r welcome')
        else:
            
            
            
           if(greeting(user_response)!=None):
                print("ROBO:"+ greeting(user_response))
           else:
                print("ROBO:"+response(user_response))
                sent_tokens.remove(user_response)

    else:
        flag=False
        print("ROBO: Bye take care!")

        
    
    
        
     
