# TestU01



# 1).smarsa_BirthdaySpacings test(Dieharder - Birthdays test with n=512, d=2^24, t=1, r=0-9, #0)
Implements the birthday spacings test. This is a variation of the collision test. The points obtained can be viewed as n birth dates in a year of k days. Let I1≤I2≤ ··· ≤In be then cell numbers obtained, sorted in increasing order. The test computes the differences Ij+1−Ij, for 1≤j < n, and count the number Y of collisions between these differences.


# 2).smarsa_MatrixRank test(NIST - Binary Matrix rank #5, Dieharder - 32x32 Binary Rank Test #2, 6x8 Binary Rank Test #3, PractRand - BRank #4)
Applies the test based on the rank of a random binary matrix. It thus generates n matrices and counts how many there are of each rank.


# 3).smarsa_Savir2 test(Dieharder - Similar to squeeze test #13)
Applies a modified version of the Savir test. The test generates a random integer I1 uniformly in {1,...,m}, then a random integer I2 uniformly in{1,...,I1}, then a random integer I3 uniformly in{1,...,I2}, and so on until It. It thus generates n values of It and compares their empirical distribution with the theoretical one, via a chi-square test.


# 4).smarsa_GCD test(Dieharder - Similar to Marsaglia and Tsang GCD Test #17)
Applies the tests based on the greatest common divisor(GCD) between two random integers in [1,2^s]. The probability that the GCD takes the value j is Pj= 6/((π^2)(j^2)).


# 5).smultin_Multinomial test
This function applies the power divergence test, based on statistic Dδ, for each value of δ.


# 6).smultin_MultinomialOver test(Dieharder - OPSO test with n=2^21, d=1024, t=2, r=0-22 #5, OQSO with n=2^21, d=32, t=4, r=0-27 #6, DNA test with n=2^21, d=4, t=10, r=0-30 #7)
Similar to smultin_Multinomial, but where then cell numbers are generated using the overlapping serial approach.


# 7).smultin_MultinomialBitsOver test(NIST - Overlapping Template matching Test #8, Serial Test with delta=1 #11, Approxiamte Entropy with delta=0 #12, Dieharder - Similar to Bitstream Test with delta=-1, n=2^21, L=20 #4)
Similar to smultin_MultinomialBits, except that the n cell numbers are generated using the overlapping approach at the bit level. Then bits are placed in a circle and each block of L successive bits determines a cell number. L and s do not have to divide each other.


# 8).sknuth_Gap test
Applies the gap test. The test generates n values in [0,1) and, for s= 0,1,2,..., counts the number of times that asequence of exactly s successive values fall outside the interval [α,β] (this is the number of gaps of length s between visits to [α,β]). 


# 9).sknuth_SimpPoker test
Applies the simplified poker test described by Knuth. It generates n groups of k integers from 0 to d−1, by making nk calls to the generator, and for each group it computes the numbers of distinct integers in the group.


# 10).sknuth_CouponCollector test
Applies the coupon collector test. The test generates a sequence of random integers in {0,...,d−1}, and counts how many must be generated before each of the d possible values appears at least once.


# 11).sknuth_MaxOft test(Dieharder - RGB Kolmogorov-Smirnov Test #204)
Applies the maximum-of-t test. This test generates n groups of t values in [0,1), computes the maximum X for each group, and then compares the empirical distribution function of these n values of X with the theoretical distribution function of the maximum, F(x) =x^t, via a chi-square test and an Anderson-Darling (AD) test. 


# 12).sknuth_Run test(Dieharder - Runs test #15)
Applies the test of increasing or decreasing subsequences(runs up or runs down).


# 13).swalk_RandomWalk1 test(NIST - Similar to Cumulative Sums #13, ENT Arithmetic mean #3)
Applies various tests based on a random walk over the set of integers Z. The walk starts at 0 and at each step, it moves by one unit to the left with probability 1/2, and by one unit to the right with probability 1/2.


# 14).snpair_ClosePairs test(Dieharder - similar to Minimum Distance with N=100, n=8000, t=2, p=2, m=1 #201, similar to 3-D sphere with N=20, n=4000, t=3, p=2, m=1 #12, similar to minimum distance 2-d circle #11)
Applies the close-pairs tests NP,m-NP,m-NP1, and m-NP2, and m-NP2S by generating n points in the t-dimensional unit torus and computing the m nearest distinct pairs of points, where the distances between the points are measured using the Lp norm if p≥1, and the L∞ norm if p= 0.

 
# 15).snpair_ClosePairsBitMatch test
Generates n points in the unit hypercube in t dimensions as insnpair_ClosePairs and computes the closest pair, but using a different definition of distance. The distance between two points Xi and Xj is 2^(−bi,j), where bi,j is the maximal value of b such that the first b bits in the binary expansion of each coordinate are the same for both Xi and Xj. 


# 16).svaria_WeightDistrib test
Applies the test proposed by Matsumoto and Kurita. This test generates k uniforms, u1,...,uk, and computes,the number of uj’s falling in the interval [α,β).


# 17).svaria_SampleProd test
This test generates t nuniforms u1,...,utn and computes the empirical distribution of the products of n nonoverlapping successive groups of t values, {u(j−1)t+1,u(j−1)t+2,...,ujt:j=117 1,...,n}. This distribution is compared with the theoretical distribution of the product of t independent U(0,1) random variables.


# 18).svaria_SampleMean test(In ENT)
This test generates n uniforms u1,...,un and computes their average.


# 19).svaria_SampleCorr test
This test generates n uniforms u1,...,un and computes the empirical autocorrelation of lag k.


# 20).svaria_AppearanceSpacings test(NIST - Maurier's Universal Statistical test #9, ENT - Entropy #1)
Applies the “universal  test” proposed by Maurer. The goal of this test is to measure the entropy of a sequence of random bits.


# 21).svaria_SumCollector test
Applies a test proposed by Ugrin-Sparac. It generates a sequence of uniforms u0,u1,...adds them up until their sum exceeds g. It then defines J= min{`≥0 :u0+···+u`> g}.This is repeated n times, to obtain n copies of J, say J1,...,Jn, whose empirical distributionis compared to the theoretical distribution by a chi-square test.


# 22).scomp_LinearComp test(NIST - Linear Complexity #10)
This procedure applies simultaneously the jump complexity test and the jump size test.
The jump complexity test counts the number of jumps occurring in the linear complexity of the sequence. A jump occurs whenever adding the next bit to the sequence increases its linear complexity.
The jump size test looks at the size of the jumps (there is a jump of size h if the complexity increases by h when we consider thenext bit of the sequence), and counts how many jumps of each size have occurred.


# 23).scomp_LempelZiv test
Given a string of n=2^k bits, this test counts the number of distinct patterns in the string in order to determine its compressibility by the Lempel-Ziv compression algorithm.


# 24).sspectral_Fourier3 test
It compares emperical ditribution of fourier coefficient.


# 25).sspectral_Fourier1 test(NIST - Discrete Fourier Transform #6)
It works on fourier transformation of the input, and comparing it with normal distribution.


# 26).sstring_HammingIndep test
Applies two tests of independence between the Hamming weights of successive blocks of L bits. They use the s most significant bits from each generated random number(after dropping the firstrbits) to build 2n blocks of L bits. Let Xj be the Hamming weight (the numbers of bits equal to 1) of the jth block, for j=1,...,2n. Each  vector (Xi,Xi+1) can take (L+ 1)×(L+ 1) possible values. The test counts the number of occurrences of each possibility among the non-overlapping pairs.


# 27).sstring_LongestHeadRun test(NIST - Longest Run of Ones in a Block #4)
This test generates n blocks of L bits by taking s bits from each of n(L/s) successive uniforms. In each block, it finds the length of the longest run of successive 1’s, and counts how many times each value of has occurred.


# 28).sstring_PeriodsInStrings test(ENT - Serial Correlation Coefficient #5)
This function applies a test based on the distribution of the correlations in bit strings of lengths.


# 29).sstring_HammingWeight2 test(NIST - Monobit test #1 with L=n, Frequency test within a Block #2, Dieharder - STS Monobit Test #100)
Given a string of n bits, the test examines the proportion of 1’s within (non-overlapping) L-bit blocks. It partitions the bit string into K=(n/L) blocks. 


# 30).sstring_HammingCorr test(PractRand - similar to BCFN #1, DC6 #2)
Applies a correlation test on the Hamming weights of successive blocks of L bits. It is strongly related to the testsstring_HammingIndep. The test uses the s most significant bits from each generated random number (after dropping the first r bits) to build n blocks of L bits. Let Xj be the Hamming weight (the numbers of bits equal to 1) of the jth block, for j= 1,...,n. The test computes the empirical correlation between the successive Xj’s.


# 31).sstring_Run test(NIST - Run Test #3, PractRand - Similar to Gap16 #3, Dieharder - similar to STS Runs Test #101)
This is a version of the run test applicable to a bit string. It is also related to the gap test. In a bit string of length n, the runs of successive 1’s can be seen as gaps between the blocks of successive 0’s. These gap (or run) lengths are independent geometric random variables, plus 1;i.e., each run has lengthiwith probability 2−i, fori= 1,2,....

# 32).sstring_AutoCor test
This test measures the autocorrelation between bits with lag d.


# 33).sstring_HammingWeight test
This test is a one-dimensional version of sstring_HammingIndep. It generates n blocks of L bits and examines the proportion of 1’s within each (non-overlapping) L-bit block.


### Source: http://simul.iro.umontreal.ca/testu01/tu01.html
