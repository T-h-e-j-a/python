# a=[4,9,'abc',[1,2,3,4]]
# out={i:a[i] for i in range(len(a))}
# print(out)


# a=[4,9,'abc',[1,2,3,4]]
# out={i:j for i,j in enumerate(a)}
# print(out)



# a='xyz'
# b=[1,2,3]
# out={a[i]:b[i] for i in range(len(b))}
# print(out)


# a='xyz'
# b=[1,2,3]
# out={i:j for i,j in zip(a,b)}
# print(out)



a={'a':'abc',1:1234,'b':'bcde',2:2345}
out={a[k]:k for k in a if isinstance(k,str)}
print(out)