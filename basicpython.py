import math
import datetime
def math_operations():
    print(math.sqrt(408))

def my_function(a,b):
    if(a>b):
        print(a)
    else:
        print(b)
def data_type_test():
    x=None
    if x is None:
        print("variable is None")
def type_conversion():
    a='408'
    print(a)
    b=int(a)
    print(b)
    c=408.508
    d=float(c)
    e=int(c)
    print(c,d,e)
def collection_type():
    name='Shiva'
    print(list(name))
    print(set(name))
    print(tuple(name))
def  user_input():
    name=input('What is your name ?')
    print(name)
def string_operations():
    s = """w'o"w"""
    print(str(s))
    print(repr(s))
def date_operations():
    today=datetime.datetime.now()
    print(today)
if __name__ == '__main__':
    math_operations()
