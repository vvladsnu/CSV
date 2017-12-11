import csv 
from datetime import datetime
import matplotlib.pyplot as plt

filename = {"2016_may_final.csv" : 6, "2016_dec_final.csv": 7, "2017_jun_final.csv" : 6} 
average_salary = []
for key in filename:
    with open(key) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        salary, current_salary = [], []
        sum = 0 
        for row in reader:
            try:
                current_salary = int(row[filename[key]])
                sum += current_salary
            except ValueError:
                print(current_salary, 'missing data')
            else:
                salary.append(current_salary)
        average_salary.append(sum / len(salary))
        f.close()
        
dates = list(filename)
fig = plt.figure(dpi=128, figsize=(12, 6))
plt.bar(dates, average_salary, 0.45, color='red')
plt.title('Average salary, December 2016 - June 2017', fontsize=24)
plt.xlabel('', fontsize=5)
plt.ylabel('Salary ($)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=12)

plt.show()

