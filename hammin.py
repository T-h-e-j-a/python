def ham(st,cha):
    out=0
    if len(st)==len(cha):
        for i in range(len(st)):
            if not st[i]==cha[i]:
                out+=1
        return out
    return 'string length not same '
print(ham('theja','ehtja'))
