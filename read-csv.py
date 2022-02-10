import csv
ips=[]
with open('ips.csv', newline='') as csvfile:
    content = csv.reader(csvfile, delimiter=',')
    for row in content:
        ips.append(row)
        info = f"IP:{row[0]}\tsubnet:{row[1]}\tinterface{row[2]}"
        print(info)
       
