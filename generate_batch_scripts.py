import os
import itertools
import glob
import json


model_index = [0,1,2]
generator_index = [0,1]
low_shot_n = [1,2,5,10,20]
experiment_id = [1,2,3,4,5]
index = 0


for prod in itertools.product(model_index, generator_index, low_shot_n, experiment_id):
   listing = glob.glob('lowshot_results/*fileid_' + str(index) + '.json')
   print('model index', prod[0], ' gen index', prod[1], ' low shot n', prod[2], ' exp id', prod[3])
   for filename in listing:
       f = open(filename)
       json_dict = json.loads(f.read())
       accs = json_dict['accs']
       print('Top 5 Novel')
       print(accs[1])
       print('Top 5 base')
       print(accs[3])
       print('Top 5 All')
       print(accs[5]) 
   print('\n')
   index += 1 

   


