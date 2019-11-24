import numpy as np


# from dashtable import data2rst
#
#
# Before training
training_input = np.array([[0, 0, 1],
                           [1, 1, 1],
                           [1, 0, 1],
                           [0, 1, 1]])

# output dataset
training_outputs = [0, 1, 1, 0]

synaptic_weights_before = [-0.16595599,
                           0.44064899,
                           -0.99977125]

# After training
synaptic_weights_after = [9.67299303,
                          -0.2078435,
                          -4.62963669]

outputs_before = [0.2689864,
                  0.3262757,
                  0.23762817,
                  0.36375058]

outputs_after = [0.00966449,
                 0.99211957,
                 0.99358898,
                 0.00786506]

# table = [
# 	['Inputs', 'Outputs', '', 'Weights', ''],
# 	['', 'Before', 'After', 'Before', 'After'],
# 	[training_input[0], training_outputs[0], outputs_after[0]], synaptic_weights[0], synaptic_weights_after[0],
# 	[training_input[1], training_outputs[1], outputs_after[1]], synaptic_weights[1], synaptic_weights_after[1],
# 	[training_input[2], training_outputs[2], outputs_after[2]], synaptic_weights[2], synaptic_weights_after[2],
# 	[training_input[3], training_outputs[3], outputs_after[3]], synaptic_weights[3], synaptic_weights_after[3],
# ]
#
# # [Row, Column] pairs of merged cells
# span0 = ([0, 0], [1, 0])
# span1 = ([0, 1], [0, 2])
# span2 = ([0, 3], [0, 4])
#
# my_spans = [span0, span1, span2]
#
# print(data2rst(table, spans=my_spans, use_headers=True))

from terminaltables import SingleTable

data = []
data.append(['Row one column one'])
data.append(['Row two column one', 'Row two column two'])
data.append(['Row three column one', 'Row three column two'])


table = SingleTable(data)
table.inner_row_border = True

table.table_data[1][1] += '\nnewline'
table.outer_border = False

# print(table.table)

# from astropy.table import Table
# import numpy as np
# 
# print('\n')
# arr = np.arange(3000).reshape(100, 30)  # 100 rows x 30 columns array
# t = Table(arr)
# # print(t)
# # t.pprint_all()
# 
# # print(t.columns)
# # print(t.colnames)
# print(t[[]])


from astropy.table import Table

training_input_strings = [str(my_list).strip('[]') for my_list in training_input]
differences = outputs_after - np.array(outputs_before)
differences_sum = sum(differences)

print("Training iterations: " + str(10000))

data = {'Inputs': training_input_strings,
        'Expected Outputs': training_outputs,
        'Outputs before': outputs_before,
        'Outputs after': outputs_after,
        'Differences': differences}

print()
print(Table(data))
print("Differences sum: " + str(differences_sum))

data2 = {'Weights before': synaptic_weights_before,
         'Weights after': synaptic_weights_after}

print()
print(Table(data2))

# data = np.arange(24).reshape(4, 6)
# column_names = ['Inputs', 'Expected Outputs' 'Outputs before', 'Outputs after', 'Weights before', 'Weights after']
# t = Table(data, names=column_names)
# print(t['Inputs'].pformat())
# t['Inputs'].format = "5b"
# t['Inputs'] = training_input
#
# print("\n")
# t.pprint_all()
