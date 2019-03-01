import numpy
from numpy import tanh as tanh
LearnRate = 0.1


class Neuron():
    def __init__(self, inputs, weights, threshold, outputs = [], outputWeights = [], hidden = False):
        self.inputs = inputs
        self.weights = weights
        self.output = None
        self.outputs = outputs
        self.outputWeights = outputWeights
        self.threshold = threshold
        self.hidden = hidden

    def calc(self):
        result = 0
        for input in self.inputs:
            result += input[0] * input[1]
        if result < self.threshold:
            self.output = 0
        else:
            self.output = 1
        return self.output

    def updateInputs(self, newInputs):
        self.inputs = newInputs

    def update(self, desiredActivation):
        result = 0
        for i in range(len(self.inputs)):
            result += self.inputs[i] * self.weights[i]

        # for i in range(len(self.inputs)):
        #     self.weights[i] = (self.weights[i]+LearnRate*self.inputs[i]*(1-tanh(tanh(result)))
        # 
        #                        * (desiredActivation-tanh(result)))
        newWeights = []
        for i in range(len(self.inputs)):
            newWeights.append(self.weights[i]+LearnRate*self.inputs[i]*self.errorCalc(desiredActivation))
        self.weights = newWeights
        print(self.inputs)
        print(self.weights)

    def errorCalc(self, desiredActivation):
        result = 0
        if self.hidden:
            for i in range(len(self.inputs)):
                result += self.inputs[i] * self.weights[i]
            for i in range(len(self.outputs)):
                weightedError += self.outputWeights[i]* self.outputs[i].errorCalc(desiredActivation)
            error = (1-tanh(tanh(result)))*weightedError
            return error

            
        
        else:
            for i in range(len(self.inputs)):
                result += self.inputs[i] * self.weights[i]
            error = (1-tanh(tanh(result)))*(desiredActivation-tanh(result))
            return error
    

