def getNum():
    '''
    Request user input an integer, checks and ensures the value is an integer, returns the integer
    '''
    x = input('Enter an integer: ')
    try:
        if float(x).is_integer():
        # Using: if x.isdigit() is a better method as it checks a string and I'm requesting a string with input()
            return int(x)
    except:
        return getNum()

def evenOddVendingMachine(x):

    y = list(range(x+1,x+19))

    even = [i for i in y if i%2==0]
    odd = [i for i in y if i%2==1]

    if x%2==0:
        print('The value {} is even and the next 9 even digits are {}'.format(x,even))
    else:
        print('The value {} is odd and the next 9 odd digits are {}'.format(x,odd))

try:
    evenOddVendingMachine(getNum())
except:
    print('PROBLME')