# Created By David Hatem
# Created at 25-1-2021

import random

def random_password(n_pass, n_digit, n_upper, n_lower, n_symbol):

  digits = [chr(i) for i in range(48, 58)]
  symbols = [chr(i) for i in range(33, 48)] + [chr(i) for i in range(91, 97)] + [chr(i) for i in range(123, 127)]
  uppers = [chr(i) for i in range(65, 65 + 26)]
  lowers = [chr(i) for i in range(97, 97 + 26)]
  all = digits + symbols + uppers + lowers

  if n_pass >= (n_digit + n_upper + n_lower + n_symbol) :
    d = random.sample(digits, n_digit)
    s = random.sample(symbols, n_symbol)
    u = random.sample(uppers, n_upper)
    l = random.sample(lowers, n_lower)
    p = l + u + d + s
    rest_n = n_pass - (n_digit + n_upper + n_lower + n_symbol)
    rest_p = random.sample(all, rest_n)
    p = p + rest_p
    random.shuffle(p)
    p = ''.join(p)
  else :
    return f'You must Enter {n_pass} letters & symbols & digits or less'

  return p



x = random_password(30, 5, 5, 5, 15)
print(x)

x = random_password(30, 5, 5, 5, 10)
print(x)

x = random_password(30, 5, 5, 5, 50)
print(x)
