#!/usr/bin/env python
# coding: utf-8

# In[6]:


from selenium.webdriver.common.by import By
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager


# ## Set path for webdriver
# 

# In[7]:


driver = webdriver.Chrome(ChromeDriverManager().install())
#driver = webdriver.Chrome(executable_path=path)


# In[8]:


Website=("https://www.amazon.in")


# In[9]:




# Navigate to the website URL and maximize the browser window
driver.get(Website)
driver.maximize_window()

# Add some delay to allow the page to fully load before interacting with it
# Implicit Wait
time.sleep(3)


# In[10]:


input_search = driver.find_element(By.ID,'twotabsearchtextbox')
search_button = driver.find_element(By.XPATH,'//*[@id="nav-search-submit-button"]')


# In[11]:


#search=input("Search= ")


# In[12]:


input_search.send_keys('Gaming Laptop under 100000')
sleep(1)
search_button.click()


# In[32]:


product_class= 'a-size-mini a-spacing-none a-color-base s-line-clamp-2'


# ## Scrap Products From Amazon

# In[60]:


products= []


# In[66]:


for i in range(10):
    print('Scraping page ',i+1)
    product=driver.find_element(By.XPATH,"//h2[@class='a-size-mini a-spacing-none a-color-base s-line-clamp-2']/a[@class='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal']/span[@class='a-size-medium a-color-base a-text-normal']")
    products.append(product.text)
    button=driver.find_element(By.XPATH,"//a[contains(@href, 'Gaming+Laptop+under+100000') and contains(@class, 's-pagination-next')]")
    button.click()  

    sleep(2)

    


# In[67]:


len(products)


# In[70]:


products[:78]


# In[ ]:


#CA=Akarshan Ghosh 




