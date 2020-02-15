# PractRand

# 1).BCFN
checks for long range linear correlations (bit counting); in practice this often detects Fibonacci style RNGs that rely upon large lags to defeat other statistical tests. Two integer parameters are used - the first is the minimum "level" it checks for bias at (it checks all higher levels that it has enough data for), higher values are faster but can miss shorter range correlations.  The recommended minimum level is 2, as that helps it skip the slowest parts and avoids redundancy with DC6 checking for the shortest range linear correlations, while still doing a reasonable amount of work for how much memory it has to scan. The second integer parameter helps determine the amount of memory and cache it will use in testing.  It is the log-base-2 of the size of the tables it uses internally. Each individual "level" of this is a frequency test on overlapping sets of hamming weights.  
	
	
# 2).DC6
checks for short range linear correlations (bit counting); takes several parameters that determine the size of integers it operates on internally, the number of adjacent such integers it looks for correlations between, and which information it uses for each such integer; This is a frequency test on overlapping sets of hamming weights.  
	
	
# 3).Gap16
A variation on the classic "Gap" test. 
  
	
# 4).BRank
A fairly standard binary matrix rank test.  The most original part of it is the control logic that decides when data should be taken from the RNG output stream to make a matrix and what size matrix it should be.  The parameter is a log-scale amount of time per gigabyte it spends calculating matrix ranks. Due to the coarse-grained nature of the results it produces, precise p-values are impossible for many of its subtests. 
	
	
# 5).FPF-"floating point frequency" test
this test does a frequency test applied to the binary format of floating point numbers storing the integer values of overlapping windows of the original data stream.  


### Source: http://pracrand.sourceforge.net/
