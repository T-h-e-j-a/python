import re
with open(r"C:\Users\sakep\OneDrive\Desktop\some.txt",'r+',encoding='utf-8') as file:
    data=file.read()
    out=re.sub(' ','_',data)
    file.seek(0)
    file.write(out)


# file=open(r"C:\Users\sakep\OneDrive\Desktop\sometext.txt",'w',encoding='utf-8')
# data=file.write()
# out=re.sub(' ','_',data)
# print(out)
# file.close() 