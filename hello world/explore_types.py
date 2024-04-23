from collections import namedtuple
from typing import Any


def main() -> None:
    some_var: Any = "Hello, World!"

    print(type(some_var))

    some_var = 42

    print(type(some_var))
    
    some_var=None
    print(type(some_var))
    
    some_var = my_func
    print(type(some_var))
    
    some_var=Person
    print(type(some_var))
    
    num_str = "8"
    num = int(num_str)
    print(type(num))
    print(num)

    num_str = "8.5"
    num = int(float(num_str))
    print(type(num))
    print(num)
    
    num_str = "8.5"
    num = float(num_str)
    print(type(num))
    print(num)

def my_func()->None:
    pass

class Person:...



if __name__ == "__main__":
    main()