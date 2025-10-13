import sys
input = sys.stdin.readline
from math import comb
primes = [2, 3, 5, 7, 11, 13, 17]
a = int(input())/100
b = int(input())/100
team_a_probablity_that_scores_primes = 0
team_b_probablity_that_scores_primes = 0
for prime in primes:
    team_a_probablity_that_scores_primes += comb(18, prime)*(a**prime)*((1-a)**(18-prime))
    team_b_probablity_that_scores_primes += comb(18, prime)*(b**prime)*((1-b)**(18-prime))

answer = 1 - (1-team_a_probablity_that_scores_primes)*(1-team_b_probablity_that_scores_primes)
print(answer)