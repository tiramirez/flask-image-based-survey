import numpy as np
import pandas as pd

file = pd.read_csv('features_imagenes.csv')

df = pd.DataFrame(file)

filter = df['NA']==1.0
error = df[filter]
list_error = error['ID'].values.tolist()

print(list_error)