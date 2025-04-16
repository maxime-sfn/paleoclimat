import numpy as np

class InputLayer:
    def __init__(self, size):
        self.A = np.random.randn(size)
        
    def setActivator(self,input):
        self.A = input

class Layer:
    def __init__(self, previous_layer_size, size):
        self.A = np.zeros(size) # the activators 
        self.B = np.random.randn(size) # the biasis
        self.W = np.random.randn(previous_layer_size, size) # the weights
        self.Z = np.zeros(size) # W^T A + B
        self.nablaCW = np.zeros((previous_layer_size, size)) # cost function gradient per weight
        self.nablaCB = np.zeros(size) # cost function gradient per bias
    

class NeuralNetwork:
    def __init__(self, layers, eta = 1):
        self.layers = layers
        self.errors = np.array([np.zeros(np.size(self.layers[l].A)) for l in np.arange(0, np.size(self.layers))], dtype=object)
        self.eta = eta # learning rate
        
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))
    
    def sigmoid_prime(self, x):
        return self.sigmoid(x) * (1 - self.sigmoid(x))

    def output(self, x):
        self.layers[0].setActivator(x) # step 1
        
        for l in np.arange(1, np.size(self.layers)): # step 2
            self.layers[l].Z = np.dot(np.transpose(self.layers[l].W), self.layers[l-1].A) + self.layers[l].B
            self.layers[l].A = self.sigmoid(self.layers[l].Z)
        print(self.layers[-1].A)

    def backPropagation(self, training_data):
        '''
        y is a function that holds the desired output for all of the training_data x so y(x) is the desired output for the input x
        '''
        
        L = np.size(self.layers)
        
        weight_modification = np.array([np.zeros(np.shape(self.layers[l].W)) if l != 0 else np.zeros((1, 1))for l in np.arange(np.size(self.layers))], dtype=object)
        bias_modification = np.array([np.zeros(np.size(self.layers[l].A)) for l in np.arange(0, np.size(self.layers))], dtype=object)
        
        n = len(training_data)
        
        for (x,y) in training_data:
                        
            self.layers[0].setActivator(x) # step 1
            
            for l in np.arange(1, L): # step 2
                self.layers[l].Z = np.dot(np.transpose(self.layers[l].W), self.layers[l-1].A) + self.layers[l].B
                self.layers[l].A = self.sigmoid(self.layers[l].Z)
            
            self.errors[-1] = np.multiply(self.layers[-1].A - y, self.sigmoid_prime(self.layers[-1].Z)) # step 3
            
            for l in np.arange(L-2, 0, -1): # step 4
                # self.errors[l] = np.multiply(np.dot(np.transpose(self.layers[l+1].W), self.errors[l+1]), self.sigmoid_prime(self.layers[l].Z))
                self.errors[l] = np.multiply(np.dot(self.layers[l+1].W, self.errors[l+1]), self.sigmoid_prime(self.layers[l].Z))
                                
            for l in np.arange(1, L):
                weight_modification[l] += np.outer(self.layers[l-1].A, self.errors[l])
                bias_modification [l] += self.errors[l]
        
        for l in np.arange(1, L):
            self.layers[l].W = self.layers[l].W - (self.eta / n) * weight_modification[l]
            self.layers[l].B = self.layers[l].B - (self.eta / n) * bias_modification[l]
                                
        
myNeuralNetwork = NeuralNetwork(np.array([InputLayer(784), Layer(784,16), Layer(16,16), Layer(16,10)]),0.01)