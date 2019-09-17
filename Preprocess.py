import gzip
import gensim 
import logging
import pickle
import os
import json
import pandas as pd
from gensim.models import KeyedVectors
from gensim.models import Word2Vec

class Process:
    def __init__(self, data_directory):
        self.directory = data_directory
        
    def clean(self,string):
    
        value=['़','ा','ि','ी','ु','ू', 'े','ै','ो','ौ','्','ঁ','ং','অ','আ','ই','ঈ','উ','ঊ','ঋ','ঌ','এ','ঐ','ও','ঔ',
              'ক','খ','গ','ঘ','ঙ','চ','ছ','জ','ঝ','ঞ','ট','ঠ','ড','ঢ','ণ','ত','থ','দ','ধ','ন','প','ফ','ব','ভ','ম','য',
              'র','ল','ৱ','ৰ','শ','ষ','হ', '়','া','ি','ী','ু','ূ','ূ','ৄ','ে','ৈ','ো','ৌ','্','ৎ','ৠ','ৡ','০','২','১',
              '৩','৪','৫','৬','৭','৮','৯',' ','স','য়']

        no_punct = ""
        for char in string:
            if char in value:
                no_punct = no_punct + char
        return no_punct

     
    def TextProcess(self):
        my_list=[]
        for p1,q1, file in os.walk(self.directory):
            for z in file:
                with open(self.directory+z,'rb') as f:
                    data = pickle.load(f)
                    p = self.clean(data)
                    my_list.append(p)

        li=[]
        for i in my_list:
            li.append(i.split())
        
        return li
            

