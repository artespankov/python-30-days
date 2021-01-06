from functools import wraps


def add_wrapping_with_style(style):
    def add_wrapping(item):
        @wraps(item)
        def wrapped_item(arg):
            return f"a {style} wrapped up box of {item(arg)}"
        return wrapped_item
    return add_wrapping


@add_wrapping_with_style('black')
def new_gpu(price):
    return f"a new Tesla x1000 GPU by ${price}"
