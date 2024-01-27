import re
# data=re.findall('[0-9]','abcdef12gh45')
# print(data)


# data=re.findall('[^0-9]','abcdef12gh45')
# print(data)



# data=re.findall('.','abcdef12gh45')
# print(data)




# data=re.findall('[0-9]+','a12bc564def12gh45')
# print(data)



# data=re.findall('\d{2}','a564bcd785ef12gh45')
# print(data)


# data=re.findall('[^0-5][0-9]{9}','345678998765434567jnbv')
# print(data)


# data=re.findall('[A-Z]{5}[0-9]{4}[A-Z]','GHUST7654AGR8347YDGJH28978H')
# print(data)


# data=re.findall('[Aa][Pp] ?[0-3][1-9] ?[A-Za-z] ?[0-9]{4}','AP 2 A 6753 97AP6T3826')
# print(data)

# data=re.findall('\+91\-[6-9][0-9]{9}','765456789987654')
# print(data)




# data=re.findall('[a-z]{4}[0-9]{3}[.][a-z]{3}\w [a-z][.][a-z]','abcd123.xyz123@ gmail.com')
# print(data)


# data=re.findall('[A-Za-z0-9]+\.?[A-Za-z0-9]*\@gmail\.com','abcd123@gmail.com abcd123.xyz123@gmail.com')
# print(data)


data=re.sub('[aeiou]','*','happy republic day')
print(data)