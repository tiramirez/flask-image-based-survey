from full_img_data import IMAGES as FULL
from no_display_img import IMAGES as FILTER

# print(len(FILTER))

for i in range(len(FULL)):
	FULL[i] = FULL[i]["id"]
for i in range(len(FILTER)):
	FILTER[i] = FILTER[i]["id"]

file = open('data.py', 'w')

file.write('IMAGES = [')
for i in FULL:
	if i not in FILTER:
		file.write('{"id":"'+ i.replace('.jpg','') +'"},\n')
file.close()

