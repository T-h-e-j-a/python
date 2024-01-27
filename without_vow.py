# def wout(n):
#     out=''
#     for i  in 'aeiouAEIOU':
#         if i not in n:
#             out+=i
#     return out

# print(wout('aeiouAEIOU'))
    


# def vowels(input_string):
#     vowels = "aeiouAEIOU"
#     pre = set(char for char in input_string if char in vowels)
#     mis = vowels - pre
#     return list(mis)
# print(vowels('theja'))


def filter(string):
    vowels='aeiouAEIOU'
    out=''
    for i in string:
        if i in vowels:
            out+=i
    return out
def extract(st):
    res=''
    for j in 'aeiouAEIOU':
        if j not in st:
            res+=j
    return res
print(extract(filter('hello')))