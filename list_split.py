def li(st):
   
    i=0
    temp=[]
    while i<len(st):
        
        if type(st[i]) in [str,list,tuple,set,dict]:
            temp+=st[i]
            
        
        i+=1
    return temp
print(li(['abcd',[1,2,3],'sree']))
        