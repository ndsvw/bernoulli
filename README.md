# Bernoulli
Bernoulli is a small python program to calculate a bernoulli trial or a bernoulli process.

Just edit the *python file* and execute it:
```python
python bernoulli.py
```

## A coin is thrown 6 times. How is the probability that the result is exactly 5 times 'head' and 1 time 'tail':
```python
bernoulli_trial(6, 5, 0.5) # 0.09375
#or
bernoulli_trial(6, 1, 0.5) # 0.09375
```

## A default dice is thrown 5 times. How is the probability that the result is less than 2 times a '6'.
```python
bernoulli_process(5, 2, 1.0/6) # 0.96450617284
```

## A coins is thrown 10 times. How is the probability that the result is between 6 and 8 times 'head'?
```python
bernoulli_process_btw(10, 6, 8, 0.5) # 0.3662109375
```

## Inverse:
```python
inverse(0.01) # 100
inverse(0.1) # 10
inverse(0.5) # 2
inverse(0.99) # 1.0101010101
inverse(bernoulli_trial(6, 5, 0.5)) # 10.6666666667
```

## Percent:
```python
percent(0.5) # 50.00%
percent(1.0/6) # 16.67%
percent(bernoulli_trial(6, 5, 0.5)) # 9.38%
```