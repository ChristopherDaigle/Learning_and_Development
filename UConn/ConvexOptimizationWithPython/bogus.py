print('floyd wtf')

def evenOddVendingMachine():
    x = int(input('Please enter an integer: '))
    y = list(range(x+1,x+19))

    even = [i for i in y if i%2==0]
    odd = [i for i in y if i%2==1]

    if x%2==0:
        print('The value {} is even and the next 9 even digits are {}'.format(x,even))
    else:
        print('The value {} is odd and the next 9 odd digits are {}'.format(x,odd))


evenOddVendingMachine()


for i in range(0,7):
    print('jackass')