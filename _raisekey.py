# name=input('enter a name:-')
# if len(name)<=4:
#     raise Exception
# else:
#     print('name is validated')





class ThejuError(Exception):
    pass
class MobilenoError(Exception):
    pass
try:
    name=input('enter a name:-')
    if len(name)<=4:
        raise ThejuError(f'name should be more than 4 characters but {len(name)} were given')
    else:
        print('name is validated')

    number=input('enter mobile no:-')
    if len(number)!=10:
        raise MobilenoError(f'number should be 10 digits but {len(number)} were given')
    else:
        print('number is validated')
except(ThejuError,MobilenoError) as e:
    print(e)