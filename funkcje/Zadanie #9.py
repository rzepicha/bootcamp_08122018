import time

def log(funkcja):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = funkcja(*args, **kwargs)
        stop = time.time()
        duration=stop-start
        print(f"dlugość wywołania {funkcja.__name__} to {duration} sekund")
        return result
    return wrapper
@log
def foo(arg):
    return f'To jest {arg}'

print("-"*40)
foo('1')

def test_decxorated_foo():
    assert foo(1)== "dlugość wywołania {foo} to x sekund"