import numpy as np

class MINIMAX_ALPHA_BETA_PRUNING(object):
    # Initialize the parameters
    def __init__(self, nodes, num_layers):
        self.nodes = nodes
        self.num_layers = num_layers

	# To check the number of nodes and layers
        assert len(self.nodes) == 3 ** (self.num_layers - 1), \
               'The value of num_layers or the size of nodes is invalid.'

    def slover(self):
        result = []
        result = self.nodes

        for n in range(self.num_layers):
            temp = []	    

            # Skip at first layer
            if n != 0:
		# Reshape the list
                result = np.array(result)
                result = np.reshape(result, (-1, 3))
                result = result.tolist()
            print('Layer {}:\n{}'.format(n, result))

	    # Check which layer is, and decide that is max or min
            if n % 2 == 0:
                for i in range(len(result)):
                    temp.append(max(result[i]))
            else:
                for i in range(len(result)):
                    temp.append(min(result[i]))

            result = temp

	# Print the node of top layer
        print('Layer {}:\n{}'.format(self.num_layers, result))

if __name__ == '__main__':
    # Define the nodes of problem
    nodes = [[3, 7],
            [9, -1, 8],
            [-4],
            [5, 7],
            [-9],
            [2, 3],
            [1, -7],
            [8],
            [1, 3, 2]]

    # Define the number of layers
    num_layers = 3

    # Initialize the class
    algorithm = MINIMAX_ALPHA_BETA_PRUNING(nodes, num_layers)

    # Call the slover function
    algorithm.slover()
