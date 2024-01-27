
# try:
#     a=10
#     a=10/0
# except TypeError:
#     print("exception handled")
# except ZeroDivisionError as e:
#     print(e)



try:
    a=10
    print(b)
except (TypeError,NameError) as e:
    print(e)
except ZeroDivisionError as e:
    print(e)
