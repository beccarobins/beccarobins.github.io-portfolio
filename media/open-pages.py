#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import webbrowser
import time


# In[6]:


# Collect URLs
urls = ['www.google.com', 
        'www.datacamp.com', 
        'www.twitter.com']


# In[10]:


count = 0

for url in urls:

    # Create URL that will work with webbrowser
    url = "https://" + url
    webbrowser.open(url)

    count += 1

    # Pause opening URLs after X seconds
    if count == 10:
        count = 0
        time.sleep(120)

