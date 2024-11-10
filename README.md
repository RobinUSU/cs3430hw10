"In this assignment, we’ll experiment with the Linear Congruential, 32-bit Xorshift, and Mersenne
Twister pseudorandom number generators (PRNGs), do some random image art to visualize how
these generators work, and implement the Equidistribution Test of number sequence randomness.

You’ll code up your solutions to the three problems in this assignment in prng.py. 

Included in the zip is cs3430_s22_hw10_uts.py with unit tests for this assignment. 

Problem 1:
Review to become comfortable with the LCG, Xorshift, Mesenne Twister, χ (chi-square), mathematical expectation,
and the Equidistribution Test of sequence randomness.

Problem 2: LCG, XORSHIFT, Mersenne Twister (2 points)
Implement the static method lcg(a, b, m, n, x0=0) in prng.py that generates random numbers
with the LCG method discussed on Slides 7–13 in the Lecture 20 PDF in Canvas. This method
takes the parameters a, b, m explained on the slides. The parameter n specifies how many numbers
will be generated and the keyword x0 defines the seed. This method returns a generator (i.e., a
Python generator) that can generates n random numbers. 

Implement the static method xorshift(a, b, c, n, x0=1) in prng.py that generates random
numbers with the 32 xorshit method discussed on Slides 14–20 in the Lecture 20 PDF in Canvas.
This method takes the parameters a, b, c. The parameter n specifies how many numbers will be
generated and the keyword x0 defines the seed. This method returns a Python generator that
generates n random numbers."

... ] 
