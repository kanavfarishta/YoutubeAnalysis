# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 16:41:14 2019

@author: Kanav.R
"""

import re
import html
import xlwt
from xlwt import Workbook

read_file = open(r'C:\Users\Kanav.R\Desktop\Data\Takeout\YouTube\history\watch-history.html','r',encoding="utf-8")
data = read_file.read()
data = data.replace("\n","")
data = data.replace("\t","")
regex_output = re.findall(r'(?<=\<body\>)(.*)(?=\<\/body\>)',data)
read_file.close()
regex_output = regex_output[0]
list_of_vdata = re.findall(r'\<a.*?\<\/a\>\<br\>\<a',regex_output)
list_of_cdata = re.findall(r'\<\/a\>\<br\>\<a.*?\<\/a\>',regex_output)
list_of_dates = re.findall(r'\d{1,2}\s[A-Z][a-z]{2}\s\d{4}',regex_output)
list_of_data_sanitizing = re.findall(r'Watched\s\<a.*?\<\/a\>',regex_output)
#print(len(list_of_dates))
#print(len(list_of_cdata))
#print(len(list_of_vdata))
#print(len(list_of_data_sanitizing))
pure_dates=[]
pure_vdata=[]
pure_cdata=[]
counter=0
for i in list_of_data_sanitizing:
    pure_text = re.search(r'(?<=\"\>)(.*)(?=\<\/a\>)',str(i))
    pure_text = html.unescape(pure_text.group())
    try:
        pure_text2= re.search(r'(?<=\"\>)(.*)(?=\<\/a\>)',str(list_of_cdata[counter]))
        pure_text2 = html.unescape(pure_text2.group())
        pure_cdata.append(pure_text2)
    except IndexError:
        #Do nothing
        pass
    
    if(pure_text[0:24]=="https://www.youtube.com/"):
        counter+=1
        continue
    else:
        pure_vdata.append(pure_text)
        pure_dates.append(list_of_dates[counter])
        counter+=1

wb = Workbook()
sheet = wb.add_sheet("Youtube Data with Dates")
bold = xlwt.easyxf('font: bold 1')
sheet.write(0,0,'Video Name',bold) 
sheet.write(0,1,'Channel Name',bold)
sheet.write(0,2,'Date',bold)

for i in range(0,len(pure_dates)):
    sheet.write(i+1,0,pure_vdata[i])
    sheet.write(i+1,1,pure_cdata[i])
    sheet.write(i+1,2,pure_dates[i])

wb.save("youtubeDataWithDates.xls")
