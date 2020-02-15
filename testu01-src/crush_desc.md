# Crush

| S.No. | Test | Parameters |
|-------|------|------------|
| 1. | smarsa__SerialOver | N=1, n=5*10^8, r=0, d=2^12, t=2.| 
| 2. | smarsa__SerialOver | N=1, n=3*10^8, r=0, d=2^6, t=4.|
| 3. | smarsa__CollisionOver | N=10, n=10^7, r=0, d=2^20, t=2.|
| 4. | smarsa__CollisionOver | N=10, n=10^7, r=10, d=2^20, t=2.|
| 5. | smarsa__CollisionOver | N=10, n=10^7, r=0, d=2^10, t=4.|
| 6. | smarsa__CollisionOver | N=10, n=10^7, r=20, d=2^10,t=4.|
| 7. | smarsa__CollisionOver | N=10, n=10^7, r=0, d=32, t=8.|
| 8. | smarsa__CollisionOver | N=10, n=10^7, r=25, d=32,t=8. |
| 9. | smarsa__CollisionOver | N=10, n=10^7, r=0, d=4, t=20.|
| 10.| smarsa__CollisionOver | N=10, n=10^7, r=28, d=4, t=20.|
| 11.| smarsa__BirthdaySpacings | N=5, n=2*10^7, r=0, d=2^31, t=2, p=1.|
| 12.| smarsa__BirthdaySpacings | N=5, n=2*10^7, r=0, d=2^21, t=3, p=1.|
| 13.| smarsa__BirthdaySpacings | N=5, n=2*10^7, r=0, d=2^16, t=4, p=1. |
| 14.| smarsa__BirthdaySpacings | N=3, n=2*10^7, r=0, d=2^9, t=7, p=1. |
| 15.| smarsa__BirthdaySpacings | N=3, n=2*10^7, r=7, d=2^9, t=7, p=1. |
| 16.| smarsa__BirthdaySpacings | N=3, n=2*10^7, r=14, d=2^8, t=8, p=1. |
| 17.| smarsa__BirthdaySpacings | N=3, n=2*10^7, r=22, d=2^8, t=8, p=1. |
| 18.| snpair__ClosePairs | N=10, n=2*10^6, r=0, t=2, p=0, m=30.|
| 19.| snpair__ClosePairs | N=10, n=2*10^6, r=0, t=3, p=0, m=30.|
| 20.| snpair__ClosePairs | N=5, n=2*10^6, r=0, t=7, p=0, m=30.|
| 21.| snpair__ClosePairsBitMatch | N=4, n=4*10^6, r=0, t=2.|
| 22.| snpair__ClosePairsBitMatch | N=2, n=4*10^6, r=0, t=4.|
| 23.| sknuth__SimpPoker | N=1, n=4*10^7, r=0, d=16, k=16. |
| 24.| sknuth__SimpPoker | N=1, n=4*10^7, r=26, d=16, k=16.|
| 25.| sknuth__SimpPoker | N=1, n=10^7, r=0, d=64, k=64.|
| 26.| sknuth__SimpPoker | N=1, n=10^7, r=24, d=64, k=64.|
| 27.| sknuth__CouponCollector | N=1, n=4*10^7, r=0, d=4.|
| 28.| sknuth__CouponCollector | N=1, n=4*10^7, r=28, d=4.|
| 29.| sknuth__CouponCollector | N=1, n=10^7, r=0, d=16.|
| 30.| sknuth__CouponCollector | N=1, n=10^7, r=26, d=16.|
| 31.| sknuth__Gap | N=1, n=10^8, r=0, Alpha=0, Beta=1/8.|
| 32.| sknuth__Gap | N=1, n=10^8, r=27, Alpha=0, Beta= 1/8.|
| 33.| sknuth__Gap | N=1, n=5*10^6, r=0, Alpha=0, Beta=1/256.|
| 34.| sknuth__Gap | N=1, n=5*10^6, r=22, Alpha=0, Beta=1/256.|
| 35.| sknuth__Run | N=1, n=5*10^8, r=0, Up=TRUE.|
| 36.| sknuth__Run | N=1, n=5*10^8, r=15, Up=FALSE.|
| 37.| sknuth__Permutation | N=1, n=5*10^7, r=0, t=10.|
| 38.| sknuth__Permutation | N=1, n=5*10^7, r=15, t=10.|
| 39.| sknuth__CollisionPermut | N=5, n=10^7, r=0, t=13.|
| 40.| sknuth__CollisionPermut | N=5, n=10^7, r=15, t=13.|
| 41.| sknuth__MaxOft | N=10, n=10^7, r=0, d=10^5, t=5.|
| 42.| sknuth__MaxOft | N=5, n=10^7, r=0, d=10^5, t=10.|
| 43.| sknuth__MaxOft | N=1, n=10^7, r=0, d=10^5, t=20.|
| 44.| sknuth__MaxOft | N=1, n=10^7, r=0, d=10^5, t=30.|
| 45.| svaria__SampleProd | N=1, n=10^7, r=0, t=10.|
| 46.| svaria__SampleProd | N=1, n=10^7, r=0, t=30.|
| 47.| svaria_SampleMean | N=10^7, n=20, r= 0.|
| 48.| svaria__SampleCorr | N=1, n=5*10^8, r=0, k=1.|
| 49.| svaria__AppearanceSpacings | N=1, Q=10^7, K=4*10^8, r=0, s=30, L=15.|
| 50.| svaria__AppearanceSpacings | N=1, Q=10^7, K=10^8, r=20, s=10, L=15.|
| 51.| svaria__WeightDistrib | N=1, n=2*10^6, r=0, k=256, Alpha=0, Beta=1/8.|
| 52.| svaria__WeightDistrib | N=1, n=2*10^6, r=8, k=256, Alpha=0, Beta=1/8.|
| 53.| svaria__WeightDistrib | N=1, n=2*10^6, r=16, k=256, Alpha=0, Beta=1/8.|
| 54.| svaria__WeightDistrib | N=1, n=2*10^6, r=24, k=256, Alpha=0, Beta=1/8.|
| 55.| svaria__SumCollector | N=1, n=2*10^7, r=0, g=10.|
| 56.| smarsa__MatrixRank | N=1, n=10^6, r=0, s=30, L=k=60.|
| 57.| smarsa__MatrixRank | N=1, n=10^6, r=20, s=10, L=k=60.|
| 58.| smarsa__MatrixRank | N=1, n=50000, r=0, s=30, L=k=300.|
| 59.| smarsa__MatrixRank | N=1, n=50000, r=20, s=10, L=k=300.|
| 60.| smarsa__MatrixRank | N=1, n=2000, r=0, s=30, L=k=1200.|
| 61.| smarsa__MatrixRank | N=1, n=2000, r=20, s=10, L=k=1200.|
| 62.| smarsa__Savir2 | N=1, n=2*10^7, r=0, m=2^20, t=30.|
| 63.| smarsa__GCD | N=1, n=108, r=0, s=30.|
| 64.| smarsa__GCD | N=1, n=4*10^7, r=10, s=20.|
| 65.| swalk__RandomWalk1 | N=1, n=5*10^7, r=0, s=30, L0=L1=90.|
| 66.| swalk__RandomWalk1 | N=1, n=10^7, r=20, s=10, L0=L1=90.|
| 67.| swalk__RandomWalk1 | N=1, n=5*10^6, r=0, s=30, L0=L1=1000.|
| 68.| swalk__RandomWalk1 | N=1, n=10^6, r=20, s=10, L0=L1=1000.|
| 69.| swalk__RandomWalk1 | N=1, n=5*10^5, r=0, s=30, L0=L1=10000.|
| 70.| swalk__RandomWalk1 | N=1, n=10^5, r=20, s=10, L0=L1=10000.|
| 71.| scomp__LinearComp | N=1, n=120000, r=0, s=1.|
| 72.| scomp__LinearComp | N=1, n=120000, r=29, s=1.|
| 73.| scomp__LempelZiv | N=10, k=25, r=0, s=30.|
| 74.| sspectral__Fourier3 | N=50000, k=14, r=0, s=30.|
| 75.| sspectral__Fourier3 | N=50000, k=14, r=20, s=10.|
| 76.| sstring__LongestHeadRun | N=1, n=1000, r=0, s=30, L=107.|
| 77.| sstring__LongestHeadRun | N=1, n=300, r=20, s=10, L=107.|
| 78.| sstring__PeriodsInStrings | N=1, n=3*10^8, r=0, s=30.|
| 79.| sstring__PeriodsInStrings | N=1, n=3*10^8, r=15, s=15.|
| 80.| sstring__HammingWeight2 | N=100, n=10^8, r=0, s=30, L=106.|
| 81.| sstring__HammingWeight2 | N=30, n=10^8, r=20, s=10, L=106.|
| 82.| sstring__HammingCorr | N=1, n=5*10^8, r=0, s=30, L=30.|
| 83.| sstring__HammingCorr | N=1, n=5*10^7, r=0, s=30, L=300.|
| 84.| sstring__HammingCorr | N=1, n=10^7, r=0, s=30, L=1200. |
| 85.| sstring__HammingIndep | N=1, n=3*10^8, r=0, s=30, L=30, d=0.|
| 86.| sstring__HammingIndep | N=1, n=10^8, r=20, s=10, L=30, d=0.|
| 87.| sstring__HammingIndep | N=1, n=3*10^7, r=0, s=30, L=300, d=0.|
| 88.| sstring__HammingIndep | N=1, n=10^7, r=20, s=10, L=300, d=0.|
| 89.| sstring__HammingIndep | N=1, n=10^7, r=0, s=30, L=1200, d=0.|
| 90.| sstring__HammingIndep | N=1, n=10^6, r=20, s=10, L=1200, d=0.|
| 91.| sstring__Run | N=1, n=10^9, r=0, s=30.|
| 92.| sstring__Run | N=1, n=10^9, r=20, s=10.|
| 93.| sstring__AutoCor | N=10, n=10^9, r=0, s=30, d=1.|
| 94.| sstring__AutoCor | N=5, n=10^9, r=20, s=10, d=1.|
| 95.| sstring__AutoCor | N=10, n=10^9, r=0, s=30, d=30.|
| 96.| sstring__AutoCor | N=5, n=10^9, r=20, s=10, d=10.|



### Source: http://simul.iro.umontreal.ca/testu01/tu01.html
