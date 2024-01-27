# file=open('sample.txt','w')
# data='happy republic day'
# file.write(data)
# file.close()


# file=open('append.txt','a')
# data='happy republic day'
# file.write(data)
# file.close()


# file=open('read.txt','w')
# data='''
# 1.thejasree
# 2.chandu
# 3.keshava
# 4.kalavathi
# 5.subbu
# '''
# file.write(data)
# file.close()



# file=open('read.txt','a')
# data='\n6.nani'
# file.write(data)
# file.close()

# file=open('read.txt','r')
# data=file.read()
# print(data)
# file.close()

import re
file=open(r"C:\Users\sakep\OneDrive\Desktop\index.txt",'r',encoding='utf-8')
data=file.read()
out=re.findall('[aeiouAEIOU]*',data)
print(len(out))
file.close() 