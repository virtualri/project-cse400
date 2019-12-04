# coding: utf-8

# In[1]:


# Title: Finding the sponsor from employee list
#
# CSE 400 - Dissertation: Implementation and Results
# Student    : Rashadul Islam
# Id         : 0301175301
# Department : Department of CSE
# Semester   : Spring 2019
# Written on : Wed Sep 10 10:00:00 BST 2019
#

# Library
import numpy as np
import pandas as pd
from numpy import genfromtxt

from NeuralNetworkFeedForwardBackpropagation import Neural_Network 

from matplotlib import pyplot as plt 


# In[2]:


# sample input append at the end
#
# data description
#                           stay,  expense,    social status,  reservation status, client's ranking score,     emmployee_oee_score), y = score on test
train = genfromtxt('labeledData.csv', skip_header=6, delimiter=',')
ranking = genfromtxt('ranking.csv', skip_header=1, delimiter=',')
inputs = genfromtxt('input.csv', delimiter=',')


#y1 = np.array(train[:,6])
ranking = np.vstack(ranking)
resourceStatus = np.vstack((train,inputs))


# In[3]:


# scale units
resourceStatus = resourceStatus/np.amax(resourceStatus, axis=0) # scaling input data
ranking = ranking/100 # scaling output data (max test score is 100 as ranking each row)

# split data
X = np.split(resourceStatus, [23])[0] # total row = resourceStatus row -1
pred = np.split(resourceStatus, [23])[1] # total row = resourceStatus row -1 


# In[ ]:


NN = Neural_Network()

average_cost =0 
cost_func = []
y_pred = []

epoch=1500

for i in range(epoch): # trains the NN 1000 times
  print("# " + str(i) + "\n")
  print("Input (scaled): \n" + str(X))
  print("Actual Output: \n" + str(ranking))
  print("Predicted Output: \n" + str(NN.forward(X)))
  pred1 = (NN.forward(X))
  y_pred.append(pred1)           
  print("="*52)
  error = np.mean(np.square(ranking - NN.forward(X)))  
  print("Loss: \n" + str(np.mean(np.square(ranking - NN.forward(X))))) # mean sum squared loss
  print("="*52)
  NN.train(X, ranking)
  cost_func.append(error)
  print ("epoch ")
  print (i)
  
epochQueue=[]  
for i in range(epoch):
    epochQueue.append(i)
    
plt.plot(epochQueue, cost_func)
plt.xlabel("Epoch")
plt.ylabel("Cost function")
plt.savefig("cost_function.png")
#plt.show()

#NN.saveWeights()

# Prediction
print("Predicted data based on trained weights: ");
print("Input (scaled): \n" + str(pred));
NN.predict(pred)


print ("Error or loss in 10000 epoch")
print ("="*52)
print (error)
print ("="*52)


# In[ ]:


# Accuracy or F1 Score
from numpy  import array
y_pred = array(y_pred)

pred2 = (y_pred[:23,-1])
pred = np.vstack(pred2[:,-1])

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(train,ranking,test_size=0.99)
#from sklearn.metrics import accuracy_score
#accuracy_score(y_test,pred)*100

from sklearn.metrics import r2_score
f1 = r2_score(y_test, pred)*100
print ("F1 score")
print (f1)

