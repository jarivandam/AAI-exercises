import numpy
from numpy import tanh as tanh
LearnRate = 0.1


class Neuron():
    def __init__(self, inputs, weights, threshold):
        self.inputs = inputs
        self.weights = weights
        self.output = None
        self.threshold = threshold

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

        for i in range(len(self.inputs)):
            self.weights[i] = (self.weights[i]+LearnRate*self.inputs[i]*(1-tanh(tanh(result)))
                               * (desiredActivation-tanh(result)))

        print(self.inputs)
        print(self.weights)
