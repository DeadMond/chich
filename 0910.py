def double_char(s):
    return ''.join(c * 2 for c in s)

def get_real_floor(n):
    if n <= 0: return n
    if n < 13: return n-1
    if n > 13: return n-2

def hello(name=''):
    return f"Hello, {name.title() or 'World'}!"

def warn_the_sheep(queue):
    n = len(queue) - queue.index('wolf') - 1
    return f'Oi! Sheep number {n}! You are about to be eaten by a wolf!' if n else 'Pls go away and stop eating my sheep'


def take(arr,n):
    return arr[:n]

def include(arr,item):
    return item in arr

def add_length(str_):
    return ["{} {}".format(i, len(i)) for i in str_.split(' ')]

def main(verb, noun): 
    return verb + noun

def area_or_perimeter(l, w):
    return l * w if l == w else (l + w) * 2

def unusual_five():
    return len("five!")

