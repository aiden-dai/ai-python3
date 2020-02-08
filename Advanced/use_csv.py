import csv

result = []
# result = set()  # Use to remove duplicates
with open('Data/ukmaint_m.csv', newline='', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        bank_cd = row[8]
        bank_name = row[6].strip() +row[7].strip()
        print('bank cd :{}, bank name: {}'.format(bank_cd, bank_name))
        result.append((bank_cd,bank_name))
        # result.add((bank_cd,bank_name))  # For set, Use to remove duplicates
        
        

with open('Data/Bank.csv','w', newline='') as output:
    csvwriter = csv.writer(output, delimiter='|')
    csvwriter.writerow(('BANK','BANK_NAME'))
    for row in result:
        csvwriter.writerow(row)  # Tuple


# DictReader and DictWriter

with open('Data/Bank.csv', newline='', encoding='utf-8') as csvfile:
    # csvreader = csv.DictReader(csvfile, delimiter='|', fieldnames=('bank', 'name'))
    csvreader = csv.DictReader(csvfile, delimiter='|')  # use first row as the header
    for row in csvreader:
        print(row)  # OrderedDict([('BANK', 'xxx'), ('BANK_NAME', 'xxx')])


with open('Data/Bank2.csv', 'w', newline='', encoding='utf-8') as output:
    csvwriter = csv.DictWriter(output, fieldnames=('bank', 'name'))
    csvwriter.writeheader()
    for row in result:
        csvwriter.writerow({'bank':row[0], 'name':row[1]})  # Dict