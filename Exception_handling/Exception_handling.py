# user defined exception
dv = 200

class RKError(Exception):
    '''new base class for custom exception'''
    pass

class FindsSmallValueError(RKError):
    '''to be raised only when runtime value is lesser than declared value'''
    pass

class FindsGreaterValueError(RKError):
    '''to be raised only when runtime value is greater than declared value'''
    pass

while True:
    rv = int(input('enter runtime value:'))
    try:
        if rv > dv:
            raise FindsGreaterValueError
        elif rv < dv:
            raise FindsSmallValueError
        elif rv == dv:
            print('both values are same')
            exit()

    except FindsSmallValueError as s:
        print(f'runtime value {rv} is lesser than declared value {dv}')

    except FindsGreaterValueError as w:
        print(f'runtime value {rv} is greater than declared value {dv}')

    finally:
        print('********************************************')