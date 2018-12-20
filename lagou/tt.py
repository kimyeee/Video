import random


def random_color(*args, **kwargs):
    r = random.randrange(0, 255)
    g = random.randrange(0, 255)
    b = random.randrange(0, 255)
    return (r, g, b)


print(random_color())
