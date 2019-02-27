from neuron import Neuron


def NorGateNeuron():
    NORGate = Neuron([[0, -0.5], [1, -0.5]], threshold=0)
    NORGate.calc()
    print(NORGate.output)


NorGateNeuron()


def Adder():
    A = 0
    B = 0

    weights = -0.5
    thresholds = -0.5

    gate1 = Neuron([[A, weights], [B, weights]], threshold=thresholds).calc()

    gate2 = Neuron([[A, weights], [gate1, weights]],
                   threshold=thresholds).calc()

    gate3 = Neuron([[gate1, weights], [B, weights]],
                   threshold=thresholds).calc()

    gate4 = Neuron([[gate2, weights], [gate3, weights]],
                   threshold=thresholds).calc()

    gate5 = Neuron([[gate1, weights], [gate1, weights]],
                   threshold=thresholds).calc()

    carry = gate5

    output = gate4

    print("Carry : " + str(carry))
    print("Output: " + str(output))


Adder()
