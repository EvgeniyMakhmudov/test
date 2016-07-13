print('init')


def square(value=1):
    return value ** 2


def mprint(value, end='\n'):
    print(value, end=end)

if __name__ == '__main__':
    mprint('Hello world', end='!\n')
