import matplotlib.pyplot as plt
import numpy as np


def sieve_of_erathotenes(max_numbers):
    is_prime = []
    primes = []
    all_numbers = []
    #filling array with integers and crating second boolean array to indicate if n element is prime numer
    for i in range(max_numbers):
        all_numbers.append(i)

    for i in range(len(all_numbers)):
        is_prime.append(1)
    #setting first 2 elements into false and setting i to first prime number
    is_prime[0] = is_prime[1] = 0
    i = 2
    #setting values to false for every multiplication of prime number
    while i**2 <= len(all_numbers):
        if is_prime[i] == 1:
            for j in range(i**2,len(all_numbers),i):
                is_prime[j] = 0
        i += 1
    #creating array with results
    for i in range(len(all_numbers)):
        if is_prime[i] == 1:
            primes.append(all_numbers[i])

    return primes

max_numbers = 1000
polar_number_array = []
polar_prime_number_array = []
prime_numbers = sieve_of_erathotenes(max_numbers)

# converting numbers into polar form
for i in range(max_numbers):
    polar_number_array.append([i * np.cos(i),i * np.sin(i)])

for i in prime_numbers:
    polar_prime_number_array.append([i * np.cos(i),i * np.sin(i)])


#showing 3 seperate windows
plt.figure(figsize=(12,12))
plt.title("Prime numbers")
#zip unpacks elements from array along with *
plt.scatter(*zip(*polar_prime_number_array),color='green')
plt.axhline(y=0,color='black')
plt.axvline(x=0,color='black')


plt.figure(figsize=(12,12))
plt.title("all integers")
plt.scatter(*zip(*polar_number_array),color='red')
plt.axhline(y=0,color='black')
plt.axvline(x=0,color='black')


plt.figure(figsize=(12,12))
plt.title("Prime numbers and all integers in one  graph")
plt.scatter(*zip(*polar_number_array),color='red')
plt.scatter(*zip(*polar_prime_number_array),color='green')
plt.axhline(y=0,color='black')
plt.axvline(x=0,color='black')
plt.show()
