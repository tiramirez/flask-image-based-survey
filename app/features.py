import numpy as np
import pandas as pd

file = pd.read_csv('features_imagenes.csv')

df = pd.DataFrame(file)

filter = df['NA']==1.0
error = df[filter]
list_error = error['ID'].values.tolist()


test = '50f42de0fdc9f065f0002285'

file = open('algo.py', 'w')

file.write('IMAGES = [')
for i in list_error:
	file.write('{"id":"'+ i.replace('.jpg','') +'"},\n')
file.close()

print(test in list_error)
