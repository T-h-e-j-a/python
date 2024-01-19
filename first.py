
a='python'
a[3:6:1]
'hon'
a[3:6]
'hon'
a[3:6:0]
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    a[3:6:0]
ValueError: slice step cannot be zero
a[0:2:1]
'py'
a[0:6:2]
'pto'
a[-4:-1:1]
'tho'

a[-4:0:1]
''
a[-4:1:1]
''
a[-4::1]
'thon'
b=[1,2,3,4,5,6,7,8,9,10]
b[1:10:3]
[2, 5, 8]
b[2:10:3]
[3, 6, 9]
b[4:7:1]
[5, 6, 7]

b[4:7]
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
b[4:7]
[5, 6, 7]
b[2:11]
[3, 4, 5, 6, 7, 8, 9, 10]
b[2:len(b)]
[3, 4, 5, 6, 7, 8, 9, 10]
b[2:]
[3, 4, 5, 6, 7, 8, 9, 10]
b[:7]
[1, 2, 3, 4, 5, 6, 7]
c=b[:]
c
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
id(c)
1943383341952
id(b)
1943351689408
c is b
False
b[4:1:1]
[]
b[4:1:-1]
[5, 4, 3]
b[6:3:-1]
[7, 6, 5]
a
'python'
b[6:3:-1]
[7, 6, 5]
b[-1:-5:-1]
[10, 9, 8, 7]

a
'python'
a[-2:-5:-1]
'oht'
a[11:17:1]
''
a="wlcome to ethnic day"
a[11:17:1]
'thnic '
a="welcome to ethnic day"
a[11:17:1]
'ethnic'
a[-15:-1:-1]
''
a[-15:-2:-1]
''
a[-15::-1]
'emoclew'
a[12:17:1]
'thnic'
a[-15:-22:-1]
'emoclew'
a[6:-1:1]
'e to ethnic da'
a[6::1]
'e to ethnic day'
a[-1::-1]
'yad cinhte ot emoclew'
a[::-1]
'yad cinhte ot emoclew'
a=121
a[::-1]
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    a[::-1]
TypeError: 'int' object is not subscriptable
a[::-1]
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    a[::-1]
TypeError: 'int' object is not subscriptable
TypeError: 'int' object is not subscriptable
SyntaxError: invalid syntax




>>> 
>>> a="1234"
>>> reverse(a)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    reverse(a)
NameError: name 'reverse' is not defined. Did you mean: 'reversed'?
>>> a.reverse()
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    a.reverse()
AttributeError: 'str' object has no attribute 'reverse'
>>> a=1234
>>> a.reverse()
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    a.reverse()
AttributeError: 'int' object has no attribute 'reverse'
>>> a[::-1]
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    a[::-1]
TypeError: 'int' object is not subscriptable
>>> a="thejasree"
>>> a[::-1]
'eersajeht'
>>> a=989
>>> b=str(a)
>>> del b
>>> b
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    b
NameError: name 'b' is not defined
>>> a==int(str(a)[::-1])
True
>>> a=1234
>>> a==int(str(a)[::-1])
False
