MAX =  100
MIN = -100

class ALPHA_BETA_PRUNING(object):
    def __init__(self):
        self.DEPTH = 3

    # Returns optimal value for current player  
    def minimax(self, depth, nodeIndex, maximizingPlayer, values, alpha, beta):  
        # Terminating condition (leaf node is reached)
        if depth == self.DEPTH:  
            return values[nodeIndex]  

        if maximizingPlayer:  
            best = MIN 

            # Recur for left and right children  
            for i in range(0, 2):
                val = self.minimax(depth + 1, nodeIndex * 2 + i, False, values, alpha, beta)  
                best = max(best, val)  
                alpha = max(alpha, best)  

                # Alpha Beta Pruning  
                if beta <= alpha:  
                    break

            print(best)
            return best  

        else: 
            best = MAX

            # Recur for left and right children  
            for i in range(0, 2):  
                val = self.minimax(depth + 1, nodeIndex * 2 + i, True, values, alpha, beta)  
                best = min(best, val)  
                beta = min(beta, best)  

                # Alpha Beta Pruning  
                if beta <= alpha:  
                    break 
            
            print(best)
            return best  

if __name__ == "__main__":  
    values = [3, 7, 9, -1, 8, -4, 5, 7, -9, 2, 3, 1, -7, 8, 1, 3, 2]
    print('Input data:\n{}'.format(values))
    values.sort()
    print('Sorted data:\n{}'.format(values))

    alpha_beta_pruning = ALPHA_BETA_PRUNING()
    optimal_value = alpha_beta_pruning.minimax(0, 0, True, values, MIN, MAX)

    print("The optimal value is :", optimal_value)  