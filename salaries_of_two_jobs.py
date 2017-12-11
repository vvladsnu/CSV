import csv
import matplotlib.pyplot as plt

filename = {"2016_may_final.csv": [1, 6], "2016_dec_final.csv": [2, 7], "2017_jun_final.csv": [1, 6]}
for key in filename:
    with open(key) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        salary_of_senior, salary_of_junior = [], []
        avg_salary_senior, avg_salary_junior = [], []
        current_salary = 0
        sum_junior = 0
        sum_senior = 0
        for row in reader:
            try:
                current_list = filename[key]
                current_salary = int(row[current_list[1]])
            except ValueError:
                print(current_salary, 'missing data')
            else:
                if row[filename[key][0]] == "Senior Software Engineer":
                    sum_senior += current_salary
                    salary_of_senior.append(current_salary)
                elif row[filename[key][0]] == "Junior Software Engineer":
                    sum_junior += current_salary
                    salary_of_junior.append(current_salary)
        avg_salary_senior.append(sum_senior / len(salary_of_senior))
        avg_salary_junior.append(sum_junior / len(salary_of_junior))
        f.close()

dates = list(filename)
fig1 = plt.figure(dpi=128, figsize=(12, 6))
plt.bar(dates, avg_salary_senior, 0.25, color='red')
plt.title('Average salary for Senior Software Engineer, December 2016 - June 2017', fontsize=18)
plt.xlabel('', fontsize=5)
plt.ylabel('Salary ($)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=12)

plt.show()

fig2 = plt.figure(dpi=128, figsize=(12, 6))
plt.bar(dates, avg_salary_junior, 0.25, color='blue')
plt.title('Average salary for Junior Software Engineer, December 2016 - June 2017', fontsize=18)
plt.xlabel('', fontsize=5)
plt.ylabel('Salary ($)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=12)

plt.show()

