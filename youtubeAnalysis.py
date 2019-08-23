# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 18:07:22 2019

@author: Kanav.R
"""

#Number of Videos watched Different Years
import matplotlib.pyplot as plt
import pandas as pd
import re
from collections import Counter
import numpy as np


def returnLimit(value,data_list):
    for i in range(0,len(data_list)):
        if(data_list[i]<=value):
            return i+1

def dailyVideos():
    limit = returnLimit(50,unique_list)
    
    plt.bar(keys[0:limit],unique_list[0:limit])
    plt.title("Days videos watched Maximum")
    plt.xlabel('Dates', fontsize=5)
    plt.xticks(rotation='vertical')
    plt.ylabel('Videos Watched', fontsize=5)
    plt.show()
    
yydates= [] #Global
mmdates= [] #Global
mmdict = {} #Global

def DataPrepare():
    month = {'Jan':'01','Feb':'02','Mar':'03','Apr':'04','May':'05','Jun':'06',
             'Jul':'07','Aug':'08','Sep':'09','Oct':'10','Nov':'11','Dec':'12'}
    for i in date:
        mm= re.search(r'[a-zA-Z]{3}\s\d{4}',str(i)) #This gives MM YYYY from DD MM YY
        mm=mm.group()
        yydates.append(mm[4:8])
        mon = mm[0:3]
        mm=mm.replace(mon,month[mon])
        wordsplit = mm.split(" ")
        wordsplit = wordsplit[-1::-1]
        mm = ' '.join(wordsplit) #This gives YYYY MM 
        mmdates.append(mm)
        
        #######This is for mmdict #######
        if mm[0:4] in mmdict.keys():
            if mm[5:7] in mmdict[mm[0:4]].keys():
                mmdict[mm[0:4]][mm[5:7]] = mmdict[mm[0:4]][mm[5:7]]+1
            else:
                #create a key of that month in that year
                mmdict[mm[0:4]][mm[5:7]] = 1
        else:
            #create a key of that year
            mmdict[mm[0:4]]={}
    #print(mmdict) # Checking all data are in descending order
 
def monthlyVideos():     
    mmdates.sort()
#    labels = X
#    sizes = Y
#    plt.pie(sizes,labels=labels,shadow=True,startangle=0)
#    plt.axis('equal')  
#    plt.tight_layout()
    plt.show()
    X=[]
    Y=[]
    for i in mmdict:
        plt.subplot(2,2,1)
        X=list(mmdict[i].keys())
        Y=list(mmdict[i].values())
        plt.title("Monthly Graph of Year %s"%i)
        plt.xticks(rotation='vertical')
        plt.plot(X,Y,'-o')
        
        plt.subplot(2,2,2)
        plt.pie(Y,labels=X,startangle=0)
        plt.axis('equal')  
        plt.tight_layout()
        plt.show()
def bars(bar_object,values):
    count=0
    for rect in bar_object:
        plt.text(x=rect.get_x(),y=rect.get_height()+0.2,s='%d'%int(values[count]),fontsize=8)
        count+=1
        
def yearlycomparison():
    yydates.sort()
    X =list(Counter(yydates).keys())
    Y =list(Counter(yydates).values())
    
    plt.subplot(2,2,1)
    bar1=plt.bar(X,Y)
    plt.xlabel('Year', fontsize=8)
    plt.ylabel('Videos Watched', fontsize=10)
    bars(bar1,Y)
    plt.subplots_adjust(left=0.1, right=0.9, bottom=0.01, top=0.99)
    
    y = [i/365 for i in Y[0:3]]    
    plt.subplot(2,2,2)
    bar2=plt.bar(X[0:3],y)
    plt.xlabel('Year', fontsize=10)
    plt.ylabel('Avg per Day', fontsize=8)
    bars(bar2,y)
    plt.subplots_adjust(left=0.1, right=0.9, bottom=0.01, top=0.99)
    plt.show()

def monthlycomparison():
   # Needs to be dynamic 
   vals = np.arange(12) #12 Months
   bar_width = 0.2
   fig,ax = plt.subplots()
   count=0
   for i in mmdict:
       if(str(i)=='2019'):
           continue #Becauuse the data for 2019 isn't complete .(4 Months more to go...)
       ax.bar(vals+(count*bar_width),(mmdict[i].values()),bar_width,label=i)
       count+=1
       
   ax.set_xlabel('Months')
   ax.set_ylabel('Videos Watched')
   ax.set_title('Monthly Comparison for Each Year')
   ax.set_xticks(vals+bar_width)
   ax.set_xticklabels((mmdict['2018'].keys()))
   ax.legend()
   #Confirming all are in Descending Order.
   #print(mmdict['2018'].keys(),mmdict['2017'].keys(),mmdict['2016'].keys())
   plt.show()
   
           

dataFrame = pd.read_excel('youtubeDataWithDates.xls',sheet_name='Youtube Data with Dates')
date = dataFrame['Date']
indx = pd.Index(date)
unique_list=(indx.value_counts())
keys=indx.value_counts().index.tolist()
print(len(keys))
# since the dates are arranged in descending orders. 

DataPrepare()
dailyVideos()
monthlyVideos()
yearlycomparison()
monthlycomparison()