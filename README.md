# batesste-primefun

A simple Python3-based library and command line program to experiment
and play with the generation and testing of large prime numbers.

## Motivation

Many libraries and tools already exist to generate very large
primes. However one of the best ways to learn something is to code it
oneself. With this in mind I developed this library and command line
tool. Note this work is based on [this tutorial][ref-tutorial].

## Usage

For a list of all options:
```
$ ./primefun.py -h
```
The following command generate 16 1024 bit prime number
candidates. These candidates have all passed a simple sieve test
followed by multiple trails of the probabilistic [Rabin Miller
Primality Test][ref-rabin]. It then writes these 16 numbers in ascii
hex format to a file called ```primes-1024.txt```.
```
./primefun.py -n 16 --num-bits=1024 --hex -o primes-1024.txt
```
The resultant candidates are prime with high probability.. For
reference this command takes about 14.4 seconds to execute on my 2022
M2-based MacBook Pro.

[ref-tutorial]: https://www.geeksforgeeks.org/how-to-generate-large-prime-numbers-for-rsa-algorithm/
[ref-rabin]: https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
