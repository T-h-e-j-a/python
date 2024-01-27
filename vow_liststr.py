def vowel(n):
    out=[]
    for i in range(len(n)):
        if n[i] in 'aeiouAEIOU':
            out+=str(i)
    return out
print(vowel('theja'))