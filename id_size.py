import csv

filename = 'data.csv'
results_f = 'results.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    main_l = []
    for row in reader:
        temp_l = []
        for ind, head in enumerate(header_row):
            temp_l.append(row[ind])
        main_l.append(temp_l)
    f.close()

print(len(main_l))
new_l = []
clm1, clm2, clm3 = [], [], []
for i in range(len(header_row)-1):
    for row in main_l:
        clm1.append(row[0])
        clm2.append(header_row[i+1])
        clm3.append(row[i+1])

with open(results_f, mode='w') as results:
    writer = csv.writer(results, delimiter=',')
    for ind in range(len(clm1)):
        writer.writerow([clm1[ind], clm2[ind], clm3[ind]])
    results.close()
