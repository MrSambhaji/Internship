#!/usr/bin/env python
# coding: utf-8

# # Q1-Write a python program to display all the header tags from wikipedia.org and make data frame.
# 
# !pip install bs4
# !pip install requests

# In[2]:


from bs4 import BeautifulSoup
import requests


# In[17]:


page=requests.get('https://en.wikipedia.org/wiki/Main_Page')


# In[18]:


page


# In[19]:


soup= BeautifulSoup(page.content)
soup


# In[21]:


first_title=soup.find('span',class_="mw-headline")
first_title


# In[22]:


first_title.text


# In[32]:


header_tags= []    #empty list

for i in soup.find_all('span',class_="mw-headline"):
    header_tags.append(i.text)
header_tags


# In[36]:


import pandas as pd
pd=pd.DataFrame({'Header_Tags':header_tags})
pd


# # 2) Write s python program to display list of respected former presidents of India(i.e. Name , Term ofoffice)
# from https://presidentofindia.nic.in/former-presidents.htm and make data frame.
# 
# from bs4 import BeautifulSoup
# import requests

# In[37]:


page=requests.get('https://presidentofindia.nic.in/former-presidents')


# In[38]:


page


# In[39]:


soup= BeautifulSoup(page.content)
soup


# In[40]:


President_det= []    #empty list

for i in soup.find_all('div',class_="desc-sec"):
    President_det.append(i.text.replace('\n','  '))
    
President_det


# In[41]:


import pandas as pd
pd=pd.DataFrame({'President Name & Term':President_det})
pd


# # Qu.5)Write a python program to scrape mentioned news details from https://www.cnbc.com/world/?region=world and
# make data frame

# In[42]:


from bs4 import BeautifulSoup
import requests


# In[43]:


page1=requests.get('https://www.cnbc.com/world/?region=world')


# In[44]:


soup= BeautifulSoup(page1.content)
soup


# In[45]:


headlines= []  #empty list to store the Latest News headline

for i in soup.find_all('div',class_="LatestNews-container"):
    headlines.append(i.text.replace('Ago','  '))
    
    
headlines


# In[46]:


import pandas as pd
pd=pd.DataFrame({'Time & Head Line':headlines})
pd


# In[47]:


newslink= []  #empty list to store the Latest News link

for i in soup.find_all('span',class_="QuickLinks-quickLink"):
    newslink.append(i.text)
newslink


# In[48]:


import pandas as pd
pd1=pd.DataFrame({'News_Link':newslink})
pd1


# # Qu 6)Write a python program to scrape the details of most downloaded articles from AI in last 90..

# In[49]:


pap=requests.get('https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles')


# In[50]:


pap


# In[51]:


soup= BeautifulSoup(pap.content)
soup


# In[52]:


autho= []  #empty list to store the Authors name

for i in soup.find_all('span',class_="sc-1w3fpd7-0 dnCnAO"):
    autho.append(i.text)
    
    
autho


# In[53]:


pdate= []  #empty list to store the published dates
for i in soup.find_all('span',class_="sc-1thf9ly-2 dvggWt"):
    pdate.append(i.text)
    
    
pdate


# In[54]:


titels= []  #empty list to store the published Titels
for i in soup.find_all('h2',class_="sc-1qrq3sd-1 gRGSUS sc-1nmom32-0 sc-1nmom32-1 btcbYu goSKRg"):
    titels.append(i.text)
    
    
titels


# In[55]:


import pandas as pd
pd2=pd.DataFrame({'Paper Title':titels,'Authors':autho,'Published Date':pdate,})
pd2


# In[ ]:




