class Neuron():
    """ Input in form of [value,weight]"""

    def __init__(self, inputs, threshold):
        self.inputs = inputs
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
