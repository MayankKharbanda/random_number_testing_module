# 1).Frequency (Monobit) Test
The focus of the test is the proportion of zeroes and ones for the entire sequence.


# 2).Frequency Test within a Block
The focus of the test is the proportion of zeroes and ones for the entire sequence.


# 3).Runs Test
The focus of this test is the total number of runs in the sequence, where a run is an uninterrupted sequence of identical bits. A run of length k consists of exactly k identical bits and is bounded before and after with a bit of the opposite value. The purpose of the runs test is to determine whether the number of runs of ones and zeros of various lengths is as expected for a random sequence. In particular, this test determines whether the oscillation between such zeros and ones is too fast or too slow.


# 4).Test for the Longest Run of Ones in a Block
The focus of the test is the longest run of ones within M-bit blocks. The purpose of this test is to determine whether the length of the longest run of ones within the tested sequence is consistent with the length of the longest run of ones that would be expected in a random sequence.


# 5).Binary Matrix Rank Test
The focus of the test is the longest run of ones within M-bit blocks. The purpose of this test is to determine whether the length of the longest run of ones within the tested sequence is consistent with the length of the longest run of ones that would be expected in a random sequence.


# 6).Discrete Fourier Transform (Spectral) Test
The focus of this test is the peak heights in the Discrete Fourier Transform of the sequence. The purpose of this test is to detect periodic features (i.e., repetitive patterns that are near each other) in the tested sequence that would indicate a deviation from the assumption of randomness.


# 7).Non-overlapping Template Matching Test
The focus of this test is the number of occurrences of pre-specified target strings. The purpose of this
test is to detect generators that produce too many occurrences of a given non-periodic (aperiodic) pattern.
For this test and for the Overlapping Template Matching test of Section 2.8, an m-bit window is used to
search for a specific m-bit pattern. If the pattern is not found, the window slides one bit position. If the
pattern is found, the window is reset to the bit after the found pattern, and the search resumes.



# 8).Overlapping Template Matching Test
The focus of the Overlapping Template Matching test is the number of occurrences of pre-specified target
strings.


# 9).Maurer’s “Universal Statistical” Test
The focus of this test is the number of bits between matching patterns (a measure that is related to the length of a compressed sequence). The purpose of the test is to detect whether or not the sequence can be significantly compressed without loss of information.


# 10).Linear Complexity Test
The focus of this test is the length of a linear feedback shift register (LFSR).


# 11).Serial Test
The focus of this test is the frequency of all possible overlapping m-bit patterns across the entire sequence. The purpose of this test is to determine whether the number of occurrences of the 2m m-bit overlapping patterns is approximately the same as would be expected for a random sequence. Note that for m = 1, the Serial test is equivalent to the Frequency test.


# 12).Approximate Entropy Test
As with the Serial test of Section 2.11, the focus of this test is the frequency of all possible overlapping m-bit patterns across the entire sequence. The purpose of the test is to compare the frequency of overlapping blocks of two consecutive/adjacent lengths (m and m+1) against the expected result for a random sequence.


# 13).Cumulative Sums (Cusum) Test
The focus of this test is the maximal excursion (from zero) of the random walk defined by the cumulative sum of adjusted (-1, +1) digits in the sequence. The purpose of the test is to determine whether the cumulative sum of the partial sequences occurring in the tested sequence is too large or too small relative to the expected behavior of that cumulative sum for random sequences. This cumulative sum may be considered as a random walk. For a random sequence, the excursions of the random walk should be near zero. For certain types of non-random sequences, the excursions of this random walk from zero will be large.


# 14).Random Excursions Test
The focus of this test is the number of cycles having exactly K visits in a cumulative sum random walk. The purpose of this test is to determine if the number of visits to a particular state within a cycle deviates from what one would expect for a random sequence. This test is actually a series of eight tests (and conclusions), one test and conclusion for each of the states: -4, -3, -2, -1 and +1, +2, +3, +4.


# 15).Random Excursions Variant Test
The focus of this test is the total number of times that a particular state is visited (i.e., occurs) in a cumulative sum random walk. The purpose of this test is to detect deviations from the expected number of visits to various states in the random walk. This test is actually a series of eighteen tests (and conclusions), one test and conclusion for each of the states: -9, -8, …, -1 and +1, +2, …, +9.



### Source: https://csrc.nist.gov/projects/random-bit-generation/documentation-and-software
