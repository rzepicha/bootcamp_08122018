def bold(funkcja):
    def wrapper_b(*args):
        return f"<b> {args} </b>"


def italic(funkcja):


@bold
@italic

def foo(arg):
    return f'To jest {arg}'


def test_decorated_foo():
    assert foo ("x")=='<b><i>To jest x</i></b>'