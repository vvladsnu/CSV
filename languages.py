import csv
import matplotlib.pyplot as plt

filename = {"2014.01.csv": [1, 3, 4], "2015.01.csv": [1, 3, 4], "2016.01.csv": [1, 3, 4]}
for key in filename:
    with open(key, encoding='utf-8') as f:
        reader = csv.reader(f)
        header_row = next(reader)
        first_language_l, main_language_l, current_language_l = [], [], []
        for row in reader:
            try:
                first_language_l.append(row[filename[key][0]])
                main_language_l.append(row[filename[key][1]])
                current_language_l.append(row[filename[key][2]])
            except ValueError:
                print('missing data')
        f.close()
first_language_d = dict.fromkeys(['Python','PHP','Pascal/Delphi','JavaScript','Java','C++','C#','C','Basic'], 0)
main_language_d = dict.fromkeys(['Python','PHP','Pascal/Delphi','JavaScript','Java','C++','C#','C','Basic'], 0)
current_language_d = dict.fromkeys(['Python','PHP','Pascal/Delphi','JavaScript','Java','C++','C#','C','Basic'], 0)

def analyze(param_1, param_2):
    for key in param_1:
        for item in param_2:
            if item == key:
                param_1[key] += 1

analyze(first_language_d, first_language_l)
analyze(main_language_d, main_language_l)
analyze(current_language_d, first_language_l)


def show(dictionary, title, color_of_diagram):
    fig1 = plt.figure(dpi=128, figsize=(12, 6))
    plt.bar(dictionary.keys(), dictionary.values(), 0.25, color=color_of_diagram)
    plt.title(title, fontsize=24)
    plt.xlabel('', fontsize=5)
    plt.ylabel('programmers', fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=12)
    plt.show()

show(first_language_d, 'Statistics \'What is your first language?\', 2014 - 2016', 'red')
show(main_language_d, 'Statistics \'What is your main language?\', 2014 - 2016', 'green')
show(current_language_d, 'Statistics \'What are you learning right now?\', 2014 - 2016', 'blue')
