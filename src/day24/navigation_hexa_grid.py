def get_w(coordinates):
    x, y = coordinates
    return x, y-1


def get_e(coordinates):
    x, y = coordinates
    return x, y+1


def get_nw(coordinates):
    x, y = coordinates
    if x % 2 == 0:
        return x-1, y
    else:
        return x-1, y-1


def get_ne(coordinates):
    x, y = coordinates
    if x % 2 == 0:
        return x-1, y+1
    else:
        return x-1, y


def get_se(coordinates):
    x, y = coordinates
    if x % 2 == 0:
        return x+1, y+1
    else:
        return x+1, y


def get_sw(coordinates):
    x, y = coordinates
    if x % 2 == 0:
        return x+1, y
    else:
        return x+1, y-1
