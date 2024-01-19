import random
out=[]
while len(out)<6:
    out+=[str(random.randint(0,9))]
    out+=[chr(random.randint(97,123))]
    out+=[random.choice(['@','#','$','&','!','?'])]
random.shuffle(out)
captcha=''
for i in out:
    captcha+=i
print(captcha)