import numpy as np
import math
from sympy import primerange
from scipy.stats import norm

# makes list of prime numbers between 1 and 100 (25 by default), more can be added if necessary
PRIME_RANGE_MAX = 101
primes = list(primerange(1, PRIME_RANGE_MAX))


# returns a concatenated string of the first n natural numbers (including 0), in binary
def binary_string(num):
    string = ""

    for i in range(num):
        string += str(bin(i)[2:])
        
    return string

# returns a concatenated string of the first n prime numbers (only works up to 25 because of
# PRIME_RANGE_MAX) I could increase that value if I wanted to, but it would make the program
# run for longer since prime numbers need to be generated
def prime_string(num):
    string = ""
    for i in range(num):
        string += str(bin(primes[i])[2:])

    return string 

# tests for randomness
def rand_test(s, threshold = .4):
    zero_count = 0
    one_count = 0
   
    for i in s:
        if(int(i) == 0):
            zero_count += 1
        elif(int(i) == 1):
            one_count += 1

    zero_ratio = zero_count/len(s)
    one_ratio = one_count/len(s)

    print("Zero ratio:", zero_ratio)
    print("One ratio:", one_ratio)
    
    if( abs(zero_ratio - one_ratio) < threshold):
        return True
    else:
        return False


binary_val = int(input("Binary String Input: "))
b_str = binary_string(binary_val)
print(b_str)

prime_val = int(input("Prime String Input: "))
p_str = prime_string(prime_val)
print(p_str)

# the treshold is how far apart the percentages of zeros and ones should be in a string
threshold = float(input("\nTreshold for Randomness Test: "))

print("Results for binary string:", rand_test(b_str, threshold))
print("\n")
print("Results for primes string:", rand_test(p_str, threshold), "\n")


# testing the same sequence but using the runs_test
# this original code was taken from this website: https://blogs.sas.com/content/iml/2013/10/09/how-to-tell-if-a-sequence-is-random.html
# before then being converted to Python from SAS 
def runs_test(seq):
    u, counts = np.unique(seq, return_counts=True)
    d = np.ones_like(seq)
    d[seq == u[0]] = -1

    n = np.sum(d > 0)
    m = np.sum(d < 0)

    dif = np.diff(np.sign(d))
    dif[0] = -2 if d[0] < 0 else 2

    R = np.sum((dif == 2) | (dif == -2))

    mu = 2 * n * m / (n + m) + 1
    var = 2 * n * m * (2 * n * m - (n + m)) / ((n + m) ** 2 * (n + m - 1))
    sigma = np.sqrt(var)

    if (n + m) > 50:
        Z = (R - mu) / sigma
    elif R - mu < 0:
        Z = (R - mu + 0.5) / sigma
    else:
        Z = (R - mu - 0.5) / sigma

    p_value = 2 * (1 - norm.cdf(np.abs(Z)))

    return Z, p_value

# # Samples
# flips = np.array(['H', 'T', 'T', 'H', 'H', 'H', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'H', 'H', 'H', 'T', 'H', 'T', 'H', 'H', 'H', 'T', 'H', 'H', 'H', 'T', 'H', 'T', 'H'])
# test_statistic, p_value = runs_test(flips)

# print(f"Runs Statistic: {test_statistic}")
# print(f"P-value: {p_value}")

# Now testing strings we have generated

"""
Some more jargon I learned:
Test statistic (Z): how far away calculated value is from expected num of runs
negative is less, positive is more

P-value: whether or not we can conclude if the sequence is random
if it is above threshold (typically .05) we can conclude that not enough evidence that Null Hypothesis (H_0)
is wrong. (Not us necessarily saying it is right either.) In this case, our Null Hypothesis is that the
sequence is random

"""

b_arr = np.array(list(b_str), dtype=int) 
print(b_arr)
test_statistic, p_value = runs_test(b_arr)
print(f"Runs Statistic: {test_statistic}")
print(f"P-value: {p_value}")

print('\n')

p_arr = np.array(list(p_str), dtype=int) 
print(p_arr)
test_statistic, p_value = runs_test(p_arr)
print(f"Runs Statistic: {test_statistic}")
print(f"P-value: {p_value}")

print('\n')

# this one obviously is not random
false_random = np.array([0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1])
print(false_random)
test_statistic, p_value = runs_test(false_random)
print(f"Runs Statistic: {test_statistic}")
print(f"P-value: {p_value}")

# Z: -2.33
# P: .0199



