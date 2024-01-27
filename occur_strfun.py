# def String(st,cha):
#     i=0
#     count=0
#     while i<len(st):
#         if st[i] in cha:
#             count+=1
#         i+=1
#     print(count)
# String('thejasree','e') 

def String(st,cha):
    # count=0
    out=[]
    for i in st:
        if i not in out:
            out[i]=1
        else:
            out[i]+=1

    print(out)
String('thejasree','e') 