# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 20:14:39 2019

@author: nEW u
"""
import json
import pandas as pd



data=[]
file1=open("C:/Users/nEW u/Documents/GitHub/project_data/primevideo.txt",'r')

for line in file1:
    data.append(json.loads(line))

twitter_dataset=pd.DataFrame(data)

twitter_dataset.to_csv("C:/Users/nEW u/Documents/GitHub/project_data/primevideo_twitter_csv.csv",index=False,encoding='utf-8')

extracted_twitter_dataset=twitter_dataset.iloc[:,[8,2,26]]

extracted_twitter_dataset.to_csv("C:/Users/nEW u/Documents/GitHub/project_data/primevideo_extracted_csv.csv",index=False,encoding='utf-8')


