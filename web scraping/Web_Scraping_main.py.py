#!/usr/bin/env python
# coding: utf-8

# In[7]:


import requests
from bs4 import BeautifulSoup
url="https://www.coursera.org/"


# In[8]:


r= requests.get(url)
htmlcontent=r.content
#print(htmlcontent)


# In[34]:


soup = BeautifulSoup(htmlcontent,'html.parser')
print(soup.prettify)


# In[42]:


title= soup.title
#print(type(title)) #Tag
#print(type(soup))# BeautifulSoup
#print(type(title.string))#NavigableString 
paras= soup.find_all('p')# to find all the paragraphas from the website
anchor= soup.find_all('a')# to find all the anchors from the website 
#print(anchor)

#get first element in the HTML page 
print(soup.find('p'))


#get classes of any element in the html page 
print(soup.find('p')['class'])


# In[14]:


#find all the elements with class lead 
print(soup.find_all('p',class_="lead"))


# In[12]:


# get the text from the tags/soup
print(soup.find('p').get_text())


# In[28]:


#get all the links on the page :
for link in anchor:
    print("https://www.coursera.org"+link.get('href'))


# In[29]:


all_links=set()
for link in anchor:  
    if(link.get('href')!='#'):
        link="https://www.coursera.org"+(link.get('href'))
        all_links.add(link)
        print(link)


# In[51]:


for div in soup.find_all('div'):
    print(div)
    print('\n')


# In[40]:


div_ids=[] #creat an empty list to store the div ids 

for div in soup.find_all('div'):
    div_id= div.get('id') #get the id attribute of the div element 
    if div_id: #check if the the id attribute exists
        div_ids.append(div_id) #add the id to the list 
print(div_ids)    #print the list of div id     


# In[50]:


ids= soup.find(id="premiumProductHeaderDropdown")
#print(ids.contents)
for elem in ids.children:
    print(elem)
    print('\n')
    
    #.children= the tags are available as a generator ----- used for big pages 
    #.contents= the tags are availage as a list --- used for small pages 


# In[57]:



for items in ids.stripped_strings:
    print(items) # it print out all the strings  


# In[60]:


print(ids.parents)
for item in ids.parents:
    
    print(item.name) #it generates the parents tag from the very fast html to /html
    


# In[ ]:




