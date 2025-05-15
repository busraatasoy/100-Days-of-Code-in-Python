# random.randint(a, b): Return a random integer N such that a <= N <= b.
import random
random_integer = random.randint(1,10)
print(random_integer)

# random.random(): Return the next random floating-point number in the range 0.0 <= X < 1.0
import random
random_number_0_to_1 = random.random()
print(random_number_0_to_1)

# You can expand the range by multiplying by different numbers:
import random
random_number_0_to_1 = random.random() * 10
print(random_number_0_to_1)

# random.uniform(a, b)
''' Return a random floating-point number *N* such that `a <= N <= b` for `a <= b` and `b <= N <= a` for `b < a`.
The end-point value `b` may or may not be included in the range depending on floating-point rounding in the expression `a + (b-a) * random()`.'''
import random
random_float = random.uniform(1,10)
print(random_float)
