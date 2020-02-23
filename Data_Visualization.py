#!/usr/bin/env python
# coding: utf-8

# In[28]:


import numpy as np 
import matplotlib .pyplot as plt 

data_file = np.loadtxt(r"C:\Users\marra\ws-data-spark\data\POI_requests.csv", dtype = "str", delimiter= "," )


# In[29]:


data_file[2][0]


# In[36]:


POI_ID = []
POI_values = []
#goal : get all values of POI ids + Total number of POIs : POI_values 
for  item in data_file : 
    POI_ID.append(item[0].strip('"'))
    POI_values.append(int(item[1].strip('"')))


# In[34]:


POI_values


# In[57]:

#computer population
def find_pop(req_list , i) : 
    s = sum(req_list)
    
    return ((i * 10)/s ) 


# In[58]:


POI_pop = []
for i in POI_values : 
    #get the population of every POI and save in a list : POI_pop
    POI_pop.append(find_pop(POI_values , i))


# In[59]:


print(POI_pop)


# In[63]:


#visualize ! 
ypos = np.arange(len(POI_ID))
plt.xticks(ypos, POI_ID)

plt.bar(ypos , POI_pop )


# In[ ]:




