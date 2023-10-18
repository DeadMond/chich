#1

def double_char(s):
    return ''.join(c * 2 for c in s)

#2

def get_real_floor(n):
    if n <= 0: return n
    if n < 13: return n-1
    if n > 13: return n-2

#3

def hello(name=''):
    return f"Hello, {name.title() or 'World'}!"

#4

def warn_the_sheep(queue):
    n = len(queue) - queue.index('wolf') - 1
    return f'Oi! Sheep number {n}! You are about to be eaten by a wolf!' if n else 'Pls go away and stop eating my sheep'

#5

def take(arr,n):
    return arr[:n]

#6

def include(arr,item):
    return item in arr

#7

def add_length(str_):
    return ["{} {}".format(i, len(i)) for i in str_.split(' ')]

#8

def main(verb, noun): 
    return verb + noun

#9

def area_or_perimeter(l, w):
    return l * w if l == w else (l + w) * 2

#10

def unusual_five():
    return len("five!")

