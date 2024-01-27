import csv
# # with open('sample.csv','w')
# with open('sample.csv','w',newline='') as file:
#     data=[
#         [1,'chandan',23],
#         [2,'nanadan',34],
#         [3,'bandan',19]
#     ]
#     record=csv.writer(file)
#     record.writerow(['id','name','age'])
#     record.writerows(data)


# with open('sample.csv','a',newline='') as file:
#     record=csv.writer(file)
#     record.writerow([4,'sree',30])


# with open('sample.csv','r',newline='') as file:
#     record=csv.reader(file)
#     for i in record:
#         print(i)



with open('new.csv','w',newline='') as csvfile:
    fieldnames=['id','name','age']
    record=csv.DictWriter(csvfile,fieldnames)
    record.writeheader()
    data=[
        {'id':1,'name':'theja','age':18},
        {'id':2,'name':'sree','age':16},
        {'id':3,'name':'chandu','age':20},

    ]
    record.writerows(data)

with open('new.csv','r',newline='') as file:
    record=csv.DictReader(file)
    for i in record:
        print(i)

