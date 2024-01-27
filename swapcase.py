def toggle():
    a=input('enter a string:-')
    b=''
    for i in a:
        if 'a'<=i<='z':
            b+=chr(ord(i)-32)
        elif 'A'<=i<='Z':
            b+=chr(ord(i)+32)
        else:
            b+=i
    return b
print(toggle())
