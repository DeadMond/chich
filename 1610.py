def chromosome_check(sperm):
    return 'Congratulations! You\'re going to have a {}.'.format('son' if 'Y' in sperm else 'daughter')

def two_sort(lst):
    return '***'.join(min(lst))

def how_much_i_love_you(nb_petals):
    return ["I love you", "a little", "a lot", "passionately", "madly", "not at all"][nb_petals % 6 - 1]

def enough(cap, on, wait):
    return max(0, wait - (cap - on))

def summation(num):
    return sum(xrange(num + 1))


def bmi(weight, height):
    bmeye = (weight/(height**2))
    if bmeye <= 18.5: return("Underweight")
    elif bmeye <= 25.0: return("Normal")
    elif bmeye <= 30.0: return("Overweight")
    elif bmeye > 30: return("Obese")

def duty_free(price, discount, holiday_cost):
    saving = price * discount / 100.0
    return int(holiday_cost / saving)

def replace_exclamation(s):
    return ''.join('!' if c in 'aeiouAEIOU' else c for c in s)

def pipe_fix(nums):
	return list(range(nums[0], nums[-1] + 1))

def people_with_age_drink(age):
    if age > 20: return 'drink whisky'
    if age > 17: return 'drink beer'
    if age > 13: return 'drink coke'
    return 'drink toddy'
