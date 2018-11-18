
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


data = pd.read_csv(r'C:/Users/gunja/Desktop/loan_prediction/train.csv')


# # DataFrame Navigation

# In[5]:


data.head()


# In[36]:


data.index


# In[37]:


data.columns


# In[38]:


data.dtypes


# # Numerical_Value Exploration

# In[6]:


data.describe()


# # Categorical_Value Exploration

# In[103]:


data['Dependents'].unique()


# In[104]:


data['Dependents'].value_counts()


# In[8]:


data['Education'].value_counts()


# In[46]:


data['Education'].unique()


# In[9]:


data['Gender'].value_counts()


# In[47]:


data['Gender'].unique()


# In[10]:


data['Married'].value_counts()


# In[44]:


data['Married'].unique()


# In[11]:


data['Self_Employed'].value_counts()


# In[43]:


data['Self_Employed'].unique()


# In[12]:


data['Property_Area'].value_counts()


# In[41]:


data['Property_Area'].unique()


# In[13]:


data['Loan_Status'].value_counts()


# In[42]:


data['Loan_Status'].unique()


# # Distribution Analysis
# 

# In[24]:


sns.distplot(data['ApplicantIncome'], bins=100, hist= True)


# In[22]:


data['ApplicantIncome'].hist(bins=50)


# In[28]:


data.boxplot(column='ApplicantIncome')


# In[34]:


data.boxplot(column='ApplicantIncome', by='Education')
plt.show()


# In[35]:


sns.boxplot(x='Education', y='ApplicantIncome', data=data)
plt.show()


# In[48]:


sns.boxplot(x='Self_Employed', y='ApplicantIncome', data=data)
plt.show()


# In[59]:


sns.boxplot(x='Loan_Status', y='ApplicantIncome', data=data)
plt.show()


# In[61]:


sns.boxplot(data['CoapplicantIncome'], orient='v')
plt.show()


# In[62]:


sns.boxplot(x='Loan_Status', y='CoapplicantIncome', data=data)
plt.show()


# In[67]:


data['LoanAmount'].hist(bins=50)
plt.show()


# In[70]:


sns.boxplot(data['LoanAmount'], orient='v')
plt.show()


# # Categorical_Value Analysis 

# In[84]:


sns.barplot(y='Credit_History', x='Gender', hue='Loan_Status', data=data, palette='husl')
plt.show()


# In[85]:


sns.barplot(x='Loan_Status', y='Credit_History', data=data, palette='spring')
plt.show()


# In[92]:


sns.barplot(y='Credit_History', x='Education', hue='Loan_Status', data=data, palette='summer')
plt.show()


# In[93]:


sns.barplot(y='Credit_History', x='Self_Employed', hue='Loan_Status', data=data, palette='Set2')
plt.show()


# In[102]:


plt.figure(figsize=(15,5))
sns.countplot(x='Dependents', hue='Loan_Status', data=data, palette='cubehelix_r')
plt.show()


# In[106]:


sns.barplot(x='Property_Area', y='Credit_History', hue='Loan_Status', data=data, palette='coolwarm')
plt.show()


# In[110]:


sns.barplot(x='Property_Area', y='ApplicantIncome', hue='Loan_Status', data=data, palette='spring')
plt.show()


# In[112]:


sns.barplot(x='Property_Area', y= 'Credit_History', hue='Loan_Status', data=data, palette='summer')
plt.show()


# In[115]:


sns.barplot(x='Married', y='ApplicantIncome',hue='Loan_Status', data=data, palette='husl')
plt.show()


# In[116]:


sns.barplot(x='Married', y='Credit_History', hue='Loan_Status', data=data, palette='spring_r')
plt.show()


# In[118]:


sns.boxplot(x='Education',y='LoanAmount', hue='Self_Employed', data=data)
plt.show()


# In[123]:


data.boxplot(column='LoanAmount', by=['Education','Self_Employed'])
plt.xticks(rotation='vertical')
plt.show()


# # Data_Preprocessing/Munging

# In[117]:


data.isnull().sum()

