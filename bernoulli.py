from b import *

x = bernoulli_trial(6, 5, 0.5) # 0.09375
print(x)

y = bernoulli_process(5, 2, 1.0/6)
print(y)

z = bernoulli_process_btw(10, 6, 8, 0.5)
print(z)