import csv
with open('SOCR-HeightWeight.csv', newline='') as f:
    reader=csv.reader(f)
    file_data=list(reader)
file_data.pop(0)
#print(file_data)
new_data=[]
for i in range(len(file_data)):
    n_num = file_data[i][1] 
    new_data.append(float(n_num))
m=len(new_data)
new_data.sort()
if m%2==0:
    median1 = float(new_data[m//2])
    median2 = float(new_data[m//2 - 1])
    median = (median1 + median2)/2
else:
    median = new_data[m//2]
print("Median is: " + str(median))