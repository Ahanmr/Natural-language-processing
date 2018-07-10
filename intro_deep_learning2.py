import numpy as np
from numpy import array
input_data=[array([0, 3]), array([1, 2]), array([-1, -2]), array([4, 0])]
weights={'node_0':array([1,2]), 'node_1':array([2,3]),'output':array([2,3])}
weights_1={'node_0':array([-1,2]), 'node_1':array([-2,3]),'output':array([2,3])}
target_actuals=[1,3,5,7]

def relu(input):
  return max(0, input)
 
def predict_network(input,weights):
  node_0_out=(input*weights['node_0']).sum()
  node_0_output=relu(node_0_out)
  node_1_out=(input*weights['node_1']).sum()
  node_1_output=relu(node_1_out)
  hidden_layer=array([node_0_output, node_1_output])
  output_final=(hidden_layer*weights['output']).sum()
  return output_final

results=[]

results1=[]

for input in input_data:
  results.append(predict_network(input, weights))
  results1.append(predict_network(input, weights_1))
  
print(results)
print(results1)

  
