#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Importing numpy
import numpy as np


# In[2]:


#using the random function to get random values and randint to get the numbers as integers
vectors = np.random.randint(0,11, size=5)


# In[3]:


print(vectors)


# In[5]:


vector2 = np.arange(15,56)


# In[6]:


#This prints all numbers ranging from 15 to 55
print(vector2)


# In[7]:


#This prints all numbers ranging from 15 to 55, excluding 15 and 55. That is, value prints starts from 16 to 54
print(vector2[1:-1])


# In[13]:


#Creating a random array with 1000 elements 
myArray = np.random.rand(1000)
print(myArray)


# In[14]:


#computing the avaerage of the array element
avg = np.mean(myArray)


# In[15]:


#computing the vairance of the array element
vari = np.var(myArray)


# In[16]:


#computing the standard deviation of the array element
std_dev =np.std(myArray)


# In[18]:


#Printing results for average, variance and standard deviation
print("Average = ", avg)
print("Variance = ", vari)
print("Standard deviation = ", std_dev)


# In[19]:


#Creating a 3x3 array
arr = np.array([[2,4,5],[8,10,12],[14,16,18]])


# In[20]:


#Cumulative sum along the axis 0 (rows ) using the cumsum function
cumSum_rows = np.cumsum(arr, axis=0)


# In[21]:


#Sum over rows for each of the 3 columns
sumRows = np.sum(arr, axis=0)


# In[22]:


#Sum over columns for each of the 2 rows
sumCols = np.sum(arr, axis=1)


# In[24]:


#Printing results
print("The original array is:\n", arr)
print("Cumulative sum along rows is:\n", cumSum_rows)
print("Sum over rows for each column:\n", sumRows)
print("Sum over column for each row:\n", sumCols)


# In[25]:


#Defining the matrix
matrix1 = np.array([[2,4],[4,6]])
matrix2 = np.array([[3,1],[1,7]])


# In[26]:


#Computing the matrix using the dot function
result = np.dot(matrix1,matrix2)


# In[27]:


#printing the results
print(result)


# In[ ]:




