#!/usr/bin/env python3

import random

firstPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
               31, 37, 41, 43, 47, 53, 59, 61, 67,
               71, 73, 79, 83, 89, 97, 101, 103,
               107, 109, 113, 127, 131, 137, 139,
               149, 151, 157, 163, 167, 173, 179,
               181, 191, 193, 197, 199, 211, 223,
               227, 229, 233, 239, 241, 251, 257,
               263, 269, 271, 277, 281, 283, 293,
               307, 311, 313, 317, 331, 337, 347, 349]

def nBitRandom(nBits):
    '''We are working in binary so we want to generate a n-bit random 
    number. This function returns a random number between 2**(n-1)+1 
    and 2**n-1.'''
    
    return(random.randrange(2**(nBits-1)+1, 2**nBits-1))

def getLowLevelPrime(nBits): 
    '''Generate a prime candidate by generating a random number of the
    appropriate length and then dividing by the first N primes looking
    for factoring.'''

    while True: 
        primeCandidate = nBitRandom(nBits) 
        for nPrime in firstPrimes:
            if primeCandidate % nPrime == 0 and nPrime**2 <= primeCandidate:
                break
        else:
            return primeCandidate

def rabinMiller(primeCandidate, nTrials = 20):
    '''Run a number of iterations of the Rabin Miller Primality test
    which is a probabilitic test for prime. If a number passes every
    time we can be pretty confident the candidate is a prime.'''

    maxDivisionsByTwo = 0
    evenComponent = primeCandidate-1

    while evenComponent % 2 == 0: 
        evenComponent >>= 1
        maxDivisionsByTwo += 1
    assert(2**maxDivisionsByTwo * evenComponent == primeCandidate-1) 

    def trialComposite(rTest): 
        if pow(rTest, evenComponent,  primeCandidate) == 1: 
            return False
        for i in range(maxDivisionsByTwo): 
            if pow(rTest, 2**i * evenComponent, primeCandidate) == primeCandidate-1: 
                return False
        return True

    for i in range(nTrials): 
        rTest= random.randrange(2, primeCandidate) 
        if trialComposite(rTest): 
            return False

    return True
        
if __name__=="__main__":

    import argparse

    parser = argparse.ArgumentParser(description='A prime number generator',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n', '--num', type=int, default=16,
                        metavar='NUM_PRIMES',
                        help='number of primes to generate')
    parser.add_argument('--num-bits', type=int, default=1,
                        metavar='NUM_BITS',
                        help='number of bits per prime.')
    parser.add_argument('-o', '--output-file', default=None,
                        metavar='OUTPUT_FILE',
                        help='when given, a file to dump the primes into')
    parser.add_argument('--hex', action='store_true',
                        help='print the primes in hex format')
    args = parser.parse_args()

    nCount = 1
    primeList = []
    while nCount <= args.num:
        while True:
            nBits = args.num_bits
            primeCandidate = getLowLevelPrime(nBits)
            if not rabinMiller(primeCandidate):
                continue
            else:
                if args.hex:
                    primeCandidateString = f'{primeCandidate:x}'
                else:
                    primeCandidateString = f'{primeCandidate}'
                    
                print("Prime %d: %d bit prime is: %s" % (nCount, nBits, primeCandidateString))
                primeList.append(primeCandidateString)
                break
        nCount+=1

    if args.output_file:
        f = open(args.output_file, 'w')
        for strPrime in primeList:
            f.write(f'{strPrime}\n')
        f.close()
