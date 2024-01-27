def even(n):
    if len(str(n))==6:
        out=0
        for i in str(n):
            if int(i)%2==0:
                out+=int(i)
        return out
    else:
        print('enter 6 digit number')
print(even(123456))