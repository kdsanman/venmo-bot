import csv

with open('third.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    transactions = 0
    payments_sent = 0
    payments_rcvd = 0
    for row in csv_reader: 
        if transactions == 0:
            print(f'Columns: {", ".join(row)}')
            transactions += 1
        else:
            if ("Transfer" not in row[3]):
                toadd = ''
                if "-" in row[8]:
                    toadd = row[8][3:]
                    payments_sent += float(toadd)
                
                elif "+" in row[8]:
                    toadd = row[8][3:]
                    payments_rcvd += float(toadd)
    
    print('Total payments sent:', round(payments_sent,2))
    print('Total payments rcvd:', round(payments_rcvd,2))

