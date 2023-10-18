#1

def move(position, roll):
    return position + 2*roll

#2

def set_alarm(employed, vacation):
    return employed and not vacation

#3

def string_clean(s):
    return ''.join(x for x in s if not x.isdigit())

#4

def say_hello(name, city, state):
  return "Hello, {}! Welcome to {}, {}!".format(" ".join(name), city, state)

#5

def opposite(number):
    return -number

#6

def no_boring_zeros(n):
    try:
        return int(str(n).rstrip('0'))
    except ValueError:
        return 0

#7

  def rain_amount(mm):
    if mm < 40:
        return 'You need to give your plant {}mm of water'.format(40 - mm)
    return 'Your plant has had more than enough water for today!'

#8

def mouth_size(animal): 
    return 'small' if animal.lower() == 'alligator' else 'wide'

#9

def greet():
    return "hello world!"

#10

def remainder(a,b):
    if min(a,b)!=0: return max(a,b)%min(a,b)
