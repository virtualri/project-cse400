import numpy as np
import pandas as pd

class Neural_Network(object):
  def __init__(self):
  #parameters
    self.inputSize = 6
    self.outputSize = 6
    self.hiddenSize = 10 

  #weights
    self.W1 = np.random.randn(self.inputSize, self.hiddenSize) # (3x2) weight matrix from input to hidden layer
    self.W2 = np.random.randn(self.hiddenSize, self.outputSize) # (3x1) weight matrix from hidden to output layer

  def forward(self, X):
    #forward propagation through our network
    self.z = np.dot(X, self.W1) # dot product of X (input) and first set of 3x2 weights
    self.z2 = self.sigmoid(self.z) # activation function
    self.z3 = np.dot(self.z2, self.W2) # dot product of hidden layer (z2) and second set of 3x1 weights
    o = self.sigmoid(self.z3) # final activation function
    return o

  def sigmoid(self, s):
    # activation function
    return 1/(1+np.exp(-s))

  def sigmoidPrime(self, s):
    #derivative of sigmoid
    return s * (1 - s)

  def backward(self, X, y, o):
    # backward propagate through the network
    self.o_error = y - o # error in output
    self.o_delta = self.o_error*self.sigmoidPrime(o) # applying derivative of sigmoid to error

    self.z2_error = self.o_delta.dot(self.W2.T) # z2 error: how much our hidden layer weights contributed to output error
    self.z2_delta = self.z2_error*self.sigmoidPrime(self.z2) # applying derivative of sigmoid to z2 error

    self.W1 += X.T.dot(self.z2_delta) # adjusting first set (input --> hidden) weights
    self.W2 += self.z2.T.dot(self.o_delta) # adjusting second set (hidden --> output) weights

  def train(self, X, y):
    o = self.forward(X)
    self.backward(X, y, o)

  #def saveWeights(self):
    #np.savetxt("w1.txt", self.W1, fmt="%s")
    #np.savetxt("w2.txt", self.W2, fmt="%s")

  def predict(self,predict_resources):
    data1=""  
    pre = (self.forward(predict_resources).astype(np.float))
    #data1 = pd.DataFrame([pre.split(' ') for pre in pre.split(' ')])
    data1 = pd.DataFrame.from_records(pre)
    
    print("="*52)
    print("Results:");
    #print(data1)
    print("="*52)
    print("Will stay in the hotel:") 
    print(data1[0][0]);
    print("Will expense: ")
    print(data1[1][0]*1000);
    print("Client's life stle status: ")
    print(data1[2][0]*100);
    print("Room type: ")
    print(data1[3][0]*10);
    print("Client reputation score: ")
    print(data1[4][0]*100);
    print("Employee OEE score: ")
    print(data1[5][0]*100);
    print("="*52) 
