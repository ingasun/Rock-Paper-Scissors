def tagged(func):
    def wrapper(arg):
        x = func(arg)
        return f'<title>{x}</title>'

    return wrapper