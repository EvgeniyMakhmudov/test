#!/usr/bin/env python3

print('1')
print('2')
print('3')

def square(value=1):
    return value ** 2


def mprint(value, end='\n'):
    print(value, end=end)


def foo(bar):
    print('foo{}'.format(bar))


if __name__ == '__main__':
    mprint('Hello world', end='!\n')
