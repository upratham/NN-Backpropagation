import numpy as np
class NN:
    def __init__(self,input_size,hidden_layer_size,output_layer_size):
        self.input_size=input_size
        self.hiddeen_layer_size=hidden_layer_size
        self.output_layer_size=output_layer_size
        ##Intialize weights with Uni~(i,p) , rand-- Uniform ,randn- Guassian Normal
        self.weights_input_hidden=np.random.rand(self.input_size,self.hiddeen_layer_size)
        self.weights_output_hidden=np .random.rand(self.hiddeen_layer_size,self.output_layer_size)

    def sigmoid(self,X):
        return 1/(1+np.exp(-X))
    def derivative_sigmoid(self,X):
        return X*(1-X)
