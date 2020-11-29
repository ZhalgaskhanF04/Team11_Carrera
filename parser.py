import random

file = open("thousand.csv",'r')
array = []
for i in range(160):
	array.append(random.randint(1,840))
file_write = open("final_data.csv","w")
for i in range(1000):
	text = file.readline()
	file_write.write(text)
	if i in array:
		file_write.write(text)



