import numpy as np
from terminaltables import AsciiTable


# sigmoid function to normalize inputs
def sigmoid(x):
    return 1 / (1 + np.exp(-x))


# sigmoid derivatives to adjust synaptic weights
def sigmoid_derivative(x):
    return x * (1 - x)


if __name__ == "__main__":

    # seed random numbers to make calculation
    np.random.seed(1)

    # input dataset
    training_input = np.array([[0,0,1],
                               [1,1,1],
                               [1,0,1],
                               [0,1,1]])

    # output dataset
    training_outputs = np.array([[0,1,1,0]]).T
    # initialize weights randomly with mean 0 to create weight matrix, synaptic weights
    synaptic_weights = 2 * np.random.random((3, 1)) - 1

    print('Random starting synaptic weights: ')
    print(synaptic_weights)

    outputs = sigmoid(np.dot(training_input, synaptic_weights))
    print('Before training: ')
    # print(outputs)
    table_data = [
        ['input data', 'output'],
        [training_input[0], outputs[0]],
        [training_input[1], outputs[1]],
        [training_input[2], outputs[2]],
        [training_input[3], outputs[3]]
    ]
    table = AsciiTable(table_data)
    print(table.table)

    # Iterate learning 10 times (10000 times)
    for iteration in range(10000):
        # Define input layer
        input_layer = training_input

        # Normalize the product of the input layer with the synaptic weights
        outputs = sigmoid(np.dot(input_layer, synaptic_weights))

        # how much did we miss?
        error = training_outputs - outputs

        # multiply how much we missed by the
        # slope of the sigmoid at the values in outputs
        adjustments = error * sigmoid_derivative(outputs)

        # update weights
        synaptic_weights += np.dot(input_layer.T, adjustments)

    print('Synaptic weights after training')
    print(synaptic_weights)

    print('After training: ')
    # print(outputs)
    table_data = [
        ['input data', 'output'],
        [training_input[0], outputs[0]],
        [training_input[1], outputs[1]],
        [training_input[2], outputs[2]],
        [training_input[3], outputs[3]]
    ]
    table = AsciiTable(table_data)
    print(table.table)
