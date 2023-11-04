#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


df = pd.read_csv(r"C:\Users\Ajith\Desktop\train.csv")


# In[3]:


df


# In[4]:


df.columns


# In[5]:


df.info()


# In[6]:


df.describe()


# In[7]:


df.isnull().sum()


# In[8]:


df.duplicated().sum()


# In[9]:


df['Occupation'].value_counts().plot(kind='pie',autopct='%0.2f%%')
plt.title('Occupation')
plt.xlabel('Occupation',fontsize=10)
plt.show()


# In[10]:


df["Occupation"].value_counts()


# In[11]:


df['Occupation'].value_counts().plot(kind='bar')
plt.title('Occupation')
plt.xlabel('Occupation',fontsize=10)
plt.show()


# In[12]:


sns.countplot(df,x='Credit_Score',palette={'Poor':'red','Standard':'yellow','Good':'green'})


# In[13]:


df["Credit_Score"].value_counts()


# In[14]:


sns.countplot(df,x='Num_Bank_Accounts',hue='Credit_Score',palette={'Poor':'red','Standard':'yellow','Good':'green'})


# In[15]:


df["Num_Bank_Accounts"].value_counts()


# In[16]:


sns.countplot(df,x='Num_Credit_Card',hue='Credit_Score',palette={'Poor':'red','Standard':'yellow','Good':'green'})


# In[17]:


df["Num_Credit_Card"].value_counts()


# In[18]:


sns.countplot(df,x='Num_of_Loan',hue='Credit_Score',palette={'Poor':'red','Standard':'yellow','Good':'green'})


# In[19]:


df["Num_of_Loan"].value_counts()


# In[20]:


df["Num_of_Delayed_Payment"].value_counts()


# In[21]:


sns.countplot(df,x='Num_of_Delayed_Payment',hue='Credit_Score',palette={'Poor':'red','Standard':'yellow','Good':'green'})


# In[30]:


df['Num_of_Loan'].value_counts().plot(kind='bar')
plt.title('Total EMI based on Monthly loan')
plt.ylabel('Occupation',fontsize=10)
plt.xlabel('Num_of_Loan',fontsize=10)
plt.show()


# In[23]:


df['Payment_of_Min_Amount'].value_counts().plot(kind='bar')
plt.title('Total EMI based on Monthly loan')
plt.ylabel('Payment_of_Min_Amoun',fontsize=10)
plt.xlabel('Num_of_Loan',fontsize=10)
plt.show()


# In[24]:


df["Payment_of_Min_Amount"].value_counts()


# In[25]:


df["Payment_Behaviour"].value_counts()


# In[26]:


df['Payment_Behaviour'].value_counts().plot(kind='pie',autopct='%0.2f%%')
plt.title('Payment_Behaviour')
plt.xlabel('Payment_Behaviour',fontsize=10)
plt.show()


# In[27]:


df["Num_Bank_Accounts"].value_counts()


# In[41]:


df['Num_of_Loan'].value_counts().plot(kind='bar')
plt.title('Total EMI based on Monthly loan')
plt.ylabel('Monthly_Balance',fontsize=10)
plt.xlabel('Num_of_Loan',fontsize=10)
plt.show()


# In[49]:


sns.countplot(df,x='Credit_Mix')


# In[50]:


df['Num_of_Loan'].value_counts().plot(kind='bar')
plt.title('Total EMI based on Monthly loan')
plt.ylabel('Credit_History_Age',fontsize=10)
plt.xlabel('Num_of_Loan',fontsize=10)
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




