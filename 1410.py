def move(position, roll):
    return position + 2*roll

def set_alarm(employed, vacation):
    return employed and not vacation

def string_clean(s):
    return ''.join(x for x in s if not x.isdigit())

def say_hello(name, city, state):
  return "Hello, {}! Welcome to {}, {}!".format(" ".join(name), city, state)

def opposite(number):
    return -number

def no_boring_zeros(n):
    try:
        return int(str(n).rstrip('0'))
    except ValueError:
        return 0

  def rain_amount(mm):
    if mm < 40:
        return 'You need to give your plant {}mm of water'.format(40 - mm)
    return 'Your plant has had more than enough water for today!'

def mouth_size(animal): 
    return 'small' if animal.lower() == 'alligator' else 'wide'

def greet():
    return "hello world!"

def remainder(a,b):
    if min(a,b)!=0: return max(a,b)%min(a,b)
