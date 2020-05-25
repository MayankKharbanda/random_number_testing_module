# Dieharder

# 0 Diehard Birthdays Test
Each test determines the number of matching intervals from 512 "birthdays" (by default) drawn on a 24-bit "year" (by default). Repeated intervals should be distributed in a Poisson distribution if the underlying generator is random enough, and a a chisq and p-value for the test are evaluated relative to this null hypothesis.


# 1 Diehard OPERM5(Overlapping 5 Permutation Test) Test
This is the OPERM5 test.  It looks at a sequence of one million 32-bit random integers.  Each set of five consecutive integers can be in one of 120 states, for the 5! possible orderings of five numbers.  Thus the 5th, 6th, 7th, ... numbers  each provide a state. As many thousands of state transitions  are observed,  cumulative counts are made of the number of  occurences of each state.  Then the quadratic form in the weak inverse of the 120x120 covariance matrix yields a test equivalent to the likelihood ratio test that the 120 cell counts came from the specified (asymptotically) normal distribution with the specified 120x120 covariance matrix (with rank 99). 


# 2 Diehard 32x32 Binary Rank Test
A random 32x32 binary matrix is formed, each row a 32-bit random integer.  The rank is determined. That rank can be from 0 to 32, ranks less than 29 are rare, and their counts are pooled with those for rank 29.  Ranks are found for 40,000 such random matrices and a chisquare test is performed on counts for ranks  32, 31, 30 and <=29.


# 3 Diehard 6x8 Binary Rank Test
From each of six random 32-bit integers from the generator under test, a specified byte is chosen, and the resulting six bytes form a 6x8 binary matrix whose rank is determined.  That rank can be from 0 to 6, but ranks 0,1,2,3 are rare; their counts are pooled with those for rank 4. A chi-square test is performed on counts for ranks 6,5 and <=4.


# 4 Diehard Bitstream Test
The file under test is viewed as a stream of bits. Call them b1,b2,... .  Consider an alphabet with two "letters", 0 and 1 and think of the stream of bits as a succession of 20-letter "words", overlapping.  Thus the first word is b1b2...b20, the second is b2b3...b21, and so on.  The bitstream test counts the number of missing 20-letter (20-bit) words in a string of 2^21 overlapping 20-letter words. There are 2^20 possible 20 letter words. For a truly random string of 2^21+19 bits, the number of missing words j should be (very close to) normally distributed with mean 141,909 and sigma 428. Thus (j-141909)/428 should be a standard normal variate (z score) that leads to a uniform [0,1) p value. 


# 5 Diehard OPSO(Overlapping Pairs Sparse Occupance) Test
The OPSO test considers 2-letter words from an alphabet of 1024 letters.  Each letter is determined by a specified ten bits from a 32-bit integer in the sequence to be tested. OPSO generates  2^21 (overlapping) 2-letter words  (from 2^21+1 "keystrokes")  and counts the number of missing words---that is 2-letter words which do not appear in the entire sequence. That count should be very close to normally distributed with mean 141,909, sigma 290. Thus (missingwrds-141909)/290 should be a standard normal variable.


# 6 Diehard OQSO(Overlapping Quadruples Sparce Occupancy) Test
Similar, to OPSO except that it considers 4-letter words from an alphabet of 32 letters, each letter determined by a designated string of 5 consecutive bits from the test file, elements of which are assumed 32-bit random integers. The mean number of missing words in a sequence of 2^21 four-letter words,  (2^21+3 "keystrokes"), is again 141909, with sigma = 295.  The mean is based on theory; sigma comes from extensive simulation.         


# 7 Diehard DNA Test
The DNA test considers an alphabet of 4 letters::  C,G,A,T, determined by two designated bits in the sequence of random integers being tested.  It considers 10-letter words, so that as in OPSO and OQSO, there are 2^20 possible words, and the mean number of missing words from a string of 2^21  (over-lapping)  10-letter  words (2^21+9 "keystrokes") is 141909. The standard deviation sigma=339 was determined as for OQSO by simulation.  (Sigma for OPSO, 290, is the true value (to three places), not determined by simulation.


# 8 Diehard Count the 1s (stream) Test
Consider the file under test as a stream of bytes (four per 32 bit integer).  Each byte can contain from 0 to 8 1's, with probabilities 1,8,28,56,70,56,28,8,1 over 256.  Now let the stream of bytes provide a string of overlapping  5-letter words, each "letter" taking values A,B,C,D,E. The letters are determined by the number of 1's in a byte::  0,1,or 2 yield A, 3 yields B, 4 yields C, 5 yields D and 6,7 or 8 yield E. Thus we have a monkey at a typewriter hitting five keys with various probabilities (37,56,70,56,37 over 256).  There are 5^5 possible 5-letter words, and from a string of 256,000 (overlapping) 5-letter words, counts are made on the frequencies for each word. The quadratic form in the weak inverse of the covariance matrix of the cell counts provides a chisquare test::  Q5-Q4, the difference of the naive Pearson sums of (OBS-EXP)^2/EXP on counts for 5- and 4-letter cell counts.


# 9 Diehard Count the 1s Test (byte)
This is the COUNT-THE-1's TEST for specific bytes. Otherwise similar to (stream) one.


# 10 Diehard Parking Lot Test
This tests the distribution of attempts to randomly park a square car of length 1 on a 100x100 parking lot without crashing.  We plot n (number of attempts) versus k (number of attempts that didn't "crash" because the car squares overlapped and compare to the expected result from a perfectly random set of parking coordinates.  This is, alas, not really known on theoretical grounds so instead we compare to n=12,000 where k should average 3523 with sigma 21.9 and is very close to normally distributed. 


# 11 Diehard Minimum Distance (2d Circle) Test
Choose n=8000 random points in a square of side 10000.  Find d, the minimum distance between the (n^2-n)/2 pairs of points.


# 12 Diehard 3d Sphere (Minimum Distance) Test
Choose  4000 random points in a cube of edge 1000.  At each point, center a sphere large enough to reach the next closest point. Then the volume of the smallest such sphere is (very close to) exponentially distributed with mean 120pi/3. 


# 13 Diehard Squeeze Test
Random integers are floated to get uniforms on [0,1). Starting with k=2^31=2147483647, the test finds j, the number of iterations necessary to reduce k to 1, using the reduction k=ceiling(k*U), with U provided by floating integers from the file being tested. 


# 14 Diehard Sums Test
Integers are floated to get a sequence U(1),U(2),... of uniform [0,1) variables.  Then overlapping sums, S(1)=U(1)+...+U(100), S2=U(2)+...+U(101),... are formed. The S's are virtually normal with a certain covariance matrix.  A linear transformation of the S's converts them to a sequence of independent standard normals, which are converted to uniform variables for a KSTEST.


# 15 Diehard Runs Test
This is the RUNS test.  It counts runs up, and runs down, in a sequence of uniform [0,1) variables, obtained by floating the 32-bit integers in the specified file. This example shows how runs are counted:  .123,.357,.789,.425,.224,.416,.95 contains an up-run of length 3, a down-run of length 2 and an up-run of (at least) 2, depending on the next values. The covariance matrices for the runs-up and runs-down are well known, leading to chisquare tests for quadratic forms in the weak inverses of the covariance matrices.


# 16 Diehard Craps Test
This is the CRAPS TEST. It plays 200,000 games of craps, finds the number of wins and the number of throws necessary to end each game.  The number of wins should be (very close to) a normal with mean 200000p and variance 200000p(1-p), with p=244/495.


# 17 Marsaglia and Tsang GCD Test
10^7 tsamples (default) of uint rands u, v are generated and two statistics are generated: their greatest common divisor (GCD) (w) and the number of steps of Euclid's Method required to find it (k). Two tables of frequencies are thus generated -- one for the number of times each value for k in the range 0 to 41 (with counts greater than this range lumped in with the endpoints).
The other table is the frequency of occurrence of each GCD w.


# 100 STS Monobit Test
Very simple.  Counts the 1 bits in a long string of random uints. Compares to expected number, generates a p-value directly from erfc().  Very effective at revealing overtly weak generators; Not so good at determining where stronger ones eventually fail.


# 101 STS Runs Test
Counts the total number of 0 runs + total number of 1 runs across a sample of bits.  Note that a 0 run must begin with 10 and end with 01. Note that a 1 run must begin with 01 and end with a 10. This test, run on a bitstring with cyclic boundary conditions, is absolutely equivalent to just counting the 01 + 10 bit pairs. It is therefore totally redundant with but not as good as the rgb_bitdist() test for 2-tuples, which looks beyond the means to the moments, testing an entire histogram  of 00, 01, 10, and 11 counts to see if it is binomially distributed with p = 0.25.


# 102 STS Serial Test (Generalized)
Accumulates the frequencies of overlapping n-tuples of bits drawn from a source of random integers.  The expected distribution of n-bit patterns is multinomial with p = 2^(-n) e.g. the four 2-bit patterns 00 01 10 11 should occur with equal probability.  The target distribution is thus a simple chisq with 2^n - 1 degrees of freedom, one lost due to the constraint that:
p\_00 + p\_01 + p\_01 + p\_11 = 1
This test does all the possible bitlevel tests from n=1 to n=24 bits (where n=1 is basically sts\_monobit, and n=2 IMO is redundant with sts\_runs).  However, if I understand things correctly it is not possible to fail a 2 bit test and pass a 24 bit test, as if 2 bits are biased so that (say) 00 occurs a bit too often, then 24 bit strings containing 00's MUST be imbalanced as well relative to ones that do not, so we really only need to check n=24 bit results to get all the rest for free, so to speak.


# 200 RGB Bit Distribution Test(Practrand - Similar to FPF test #5)
Accumulates the frequencies of all n-tuples of bits in a list of random integers and compares the distribution thus generated with the theoretical (binomial) histogram, forming chisq and the associated p-value.  In this test n-tuples are selected WITHOUT overlap (e.g. 01|10|10|01|11|00|01|10) so the samples are independent.  Every other sample is offset modulus of the sample index and ntuple_max.


# 201 RGB Generalized Minimum Distance Test
This is the generalized minimum distance test, based on the paper of M. Fischler in the doc directory and private communications. This test utilizes correction terms that are essential in order for the test not to fail for large numbers of trials.  It replaces both diehard\_2dsphere.c and diehard\_3dsphere.c, and generalizes the test itself so that it can be run for any d = 2,3,4,5. 


# 202 RGB Permutations Test(Dieharder - OPERM5 #1)
This is a non-overlapping test that simply counts order permutations of random numbers, pulled out n at a time.  There are n! permutations and all are equally likely.This is a poor-man's version of the overlapping permutations tests, which are much more difficult because of the covariance of the overlapping samples.


# 203 RGB Lagged Sum Test
One simply adds up uniform deviates sampled from the rng, skipping lag samples in between each rand used.  The mean of tsamples samples thus summed should be 0.5*tsamples.


# 204 RGB Kolmogorov-Smirnov Test
This test generates a vector of tsamples uniform deviates from the selected rng, then applies an Anderson-Darling or Kuiper KS test to it to directly test for uniformity. The real purpose of this test is to test ADKS and KKS, not to test rngs.


# 205 Byte Distribution
Extract n independent bytes from each of k consecutive words. Increment indexed counters in each of n tables. (Total of 256 * n counters.)


# 206 DAB DCT(Discrete Cosine Transform)(Frequency Analysis)
This test performs a Discrete Cosine Transform (DCT) on the output of the RNG. More specifically, it performs tsamples transforms, each over an independent block of ntuple words. If tsamples is large enough, the positions of the maximum (absolute) value in each transform are recorded and subjected to a chisq test for uniformity/independence. (A standard type II DCT is used.)


# 207 DAB Fill Tree Test
This test fills small binary trees of fixed depth with words from the the RNG. When a word cannot be inserted into the tree, the current count of words in the tree is recorded, along with the position at which the word would have been inserted.


# 208 DAB Fill Tree 2 Test
Bit version of Fill Tree test. This test fills small binary trees of fixed depth with "visited" markers.  When a marker cannot be placed, the current count of markers in the tree and the position that the marker would have been inserted, if it hadn't already been marked.
For each bit in the RNG input, the test takes a step right (for a zero) or left (for a one) in the tree. If the node hasn't been marked, it is marked, and the path restarts. Otherwise, the test continues with the next bit.


# 209 DAB Monobit 2 Test
Block-monobit test.



### Source: https://webhome.phy.duke.edu/~rgb/General/dieharder.php

